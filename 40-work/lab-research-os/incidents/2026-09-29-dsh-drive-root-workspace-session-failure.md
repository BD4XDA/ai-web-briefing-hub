# Incident — DSH Web session creation failed twice in one episode

Date: 2026-09-29. Reported by Human PI (two screenshots of the Web UI banner). Both causes repaired
the same day. The file name reflects the first cause only; the record covers both.

## Symptom (first cause)

Creating a new session in the DSH Web UI failed with:

    gateway/internal: failed to create session "session-c291ec65-e64f-4308-b13a-32e7119e4525":
    Error: failed to ensure project directory "C:\":
    Error: EPERM: operation not permitted, mkdir 'C:\'

## Source evidence

- Emitting code: `dsh-api-session-controller/lib/index.js` line 445 —
  `await mkdir(cwd, { recursive: true })` inside `createOrAdopt`, wrapped at line 447 by
  `failed to ensure project directory "${cwd}"`.
- `cwd` is a caller-supplied parameter; the Web client sends the selected Workspace's path.
- Reproduced directly: `fs.mkdirSync("C:\\", { recursive: true })` throws
  `EPERM: operation not permitted, mkdir 'C:\'` — byte-identical to the reported message. Node
  rejects a recursive mkdir of a Windows drive root, so any Session whose directory is a drive root
  fails at creation.
- The only DSH state naming a drive root was Workspace registry entry
  `b279c108-1076-4b8e-abb6-05f44faf1151` in `~/.dsh/storages/workspace.json`:
  `path "C:\\"`, `title ""`, `sessionIds []`, created 2026-09-10. It held no session, so it was
  selectable in the sidebar but could never be created in.

## Attempted actions

- Confirmed the defect is data-triggered, not a code defect introduced here; DSH 0.1.7-rc.2 vendor
  code was left unmodified.
- Checked for a supported removal path: `dsh-api-workspace-controller` exposes
  `delete(request)` — "Remove one Workspace registration while retaining files and Sessions".
  The registry edit below performs the same removal semantically.
- Backed up `~/.dsh/storages/workspace.json` to
  `workspace.json.bak-20260929-pre-cdrive-workspace-removal` before editing.
- Stopped the DSH Web server first so the live storage domain could not rewrite a stale in-memory
  copy over the edit; edited the JSON (removing the entry from `global.workspaceIds` and
  `tables.workspaces`, diff = those lines only); restarted the server.

## Outcome

- Repaired. Registry now holds 6 Workspaces, none a drive root.
- Verification: `mkdir(..., {recursive:true})` reproduces EPERM on `C:\` and returns OK for every
  remaining registered Workspace whose path exists; zero remaining Workspaces can raise this error.
- Server restarted and listening on `127.0.0.1:3080` with the fixed registry.
- No session, attachment or research data was deleted; the removed registration owned no session.

## Second cause, same episode — junction path fails workspace attach

After the drive-root repair, session creation advanced one step further and failed differently:

    session/workspace-attach-failed: session "session-a12cad3d-..." was created but could not
    attach to workspace "e4c2f3c7-0d47-4fbb-86d2-2e1ac0fae9d1":
    Error: cannot attach session 'session-a12cad3d-...' to workspace 'D:\20_代码项目\赛博课题组':
    its cwd resolves to 'D:\项目仓库\赛博课题组'

This is **not** a cache problem, and not a repeat of the first cause: the session was created
successfully, the `mkdir` succeeded, and the failure moved to the attach step.

- Emitting code: `dsh-workspace/lib/index.js:122`. `attachSession` computes
  `cwd = await realpathNormalize(header.cwd)` and then requires exact string equality with the
  registration: `if (cwd !== this.record.path) throw`. `realpathNormalize` is `fs.realpath`, so the
  session's directory is canonicalised while `record.path` is compared **unresolved**.
- The workspace `e4c2f3c7` was registered as `D:\20_代码项目\赛博课题组`, which is a `<JUNCTION>`
  (confirmed via `dir /AL`) to `\??\D:\项目仓库\赛博课题组`. `fs.realpathSync` of the junction and of
  the canonical path both return `D:\项目仓库\赛博课题组`, so the registered string could never match.
- The same string comparison backs `get sessionIds()`, so the workspace's three existing Sessions
  were being filtered out of the listing as well.
- This was already recorded as an open question in the previous checkpoint — "whether the DSH
  workspace registry entry should be repointed from the compatibility junction to the canonical
  repository path" — and is now confirmed by direct evidence rather than hypothesis.

Repair: repointed `record.path` for `e4c2f3c7` to the canonical `D:\项目仓库\赛博课题组`, derived from
`fs.realpathSync` of the old value rather than hardcoded. Backup
`workspace.json.bak-20260929-pre-junction-path-repoint`. Server stopped, registry edited (diff was
the one path line plus the `updatedAt` stamp the domain normally applies), server restarted.

**Confirmed end to end by the Human PI on 2026-09-29**: new-session creation in the Web UI now works.
This closes the only step of the repair that could not be exercised locally, since the Web API is a
WebSocket RPC requiring the browser session. Note the repair is cache-immune: the compatibility
junction path also resolves to the registered canonical path, so a client still holding the old path
attaches correctly too.

Outcome: verified that a newly created Session resolves to exactly `record.path`, and that all three
existing Sessions — whose headers still carry the junction path — now also resolve to it, so they are
attachable and visible again. Every remaining registered Workspace passes the same equality check;
none has a resolution mismatch.

## Unresolved conditions

- **Coverage correction.** The earlier same-day verification
  (`artifacts/DSH-DEEPSEEK-NATIVE-INDEPENDENCE-2026-09-29.md`) exercised the Web profile's *boot and
  app-shell serve* but not *session creation*. Its "no DSH defect found" conclusion was therefore
  scoped to the paths actually exercised and is superseded here for the Web session-creation path.
- **Five stale Workspace registrations** point at directories that no longer exist (they were moved
  into the Desktop ministry structure on 2026-09-28): `C:\Users\ASUS\Desktop\txtstage`,
  `C:\Users\ASUS\Desktop\txtstage\08其他（与本剧本无关）`, `C:\Users\ASUS\Desktop\stage`,
  `D:\Harness desktop`, `D:\项目仓库\01`. They do **not** error — selecting one silently recreates an
  empty directory. They hold 3–14 Sessions each and are historical, so they were deliberately left
  registered rather than cleaned up.
- **Upstream robustness:** DSH treats an existing drive root as a directory to create. A defensive
  `mkdir` that tolerates an existing path (or validates against drive roots) would remove the whole
  failure class. Not patched locally — vendor code, would be overwritten by updates.
