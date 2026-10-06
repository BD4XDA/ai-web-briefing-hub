# DSH Desktop boot animation installation

Date: 2026-10-06 (Asia/Shanghai)

## Result

`dsh-boot-animation` is installed for the DSH Desktop `desktop` profile. The plugin is pinned to upstream tag `v0.2.0` at commit `161d9abdace38430042df5ed0380c5e37031581b`. The installed DSH Desktop is `0.2.0-rc.2`, which is the version named by the plugin's installation contract.

This is an optional cosmetic extension, not a scientific or control-plane capability. It is therefore not admitted into `config/capability-registry.json` and is not part of the weekly core-capability update surface. Recheck it when DSH Desktop changes version or when the Human PI requests a plugin update.

## Source and local placement

- Upstream: https://github.com/lxj5820/dsh-boot-animation
- Install instructions: https://github.com/lxj5820/dsh-boot-animation/blob/main/INSTALL.md
- Local package: `C:/Users/ASUS/.dsh/plugins/dsh-boot-animation`
- Desktop profile link: `C:/Users/ASUS/.dsh/profiles/desktop/node_modules/dsh-boot-animation`
- Profile patch: `C:/Users/ASUS/.dsh/profiles/desktop/cordis.patch.yml`
- Automatic pre-install backup: `C:/Users/ASUS/.dsh/.dsh-rollback-dsh-boot-animation-20261006-142718`

## Proportional verification

- Reviewed the installer and uninstaller before execution. The installer backs up the profile patch, creates directory junctions, and appends one plugin row; it does not modify the DSH application package, run a package manager, read credentials, or replace existing research configuration.
- Static scan found only same-origin manifest/video requests in runtime code and no child-process or remote-network execution path.
- `verify-options.mjs`: PASS, 43/43 checks.
- Direct production-module import: PASS (`apply` exported and `Config` present).
- Required host schema was linked to the existing `@deepseek-ai/schemastery` 3.18.4 copy.
- After DSH Desktop launch, `http://127.0.0.1:19387/` returned the expected authenticated-root response (`401`) while the plugin manifest returned `200` and listed three enabled, fast-start video assets. This proves the host activated the plugin route without removing the application's authentication gate.
- DSH Desktop launched and retained a visible main window.

Two developer-oriented verification scripts could not finish because the published package does not include the development-only `@deepseek-ai/cosmokit` fixture expected by those scripts. No extra dependency was installed merely to satisfy the test harness. This does not negate the successful production import, route activation, manifest response, and 43/43 client-options test, but the final visual appearance remains a GUI observation for the Human PI.

## Rollback

Disable temporarily in DSH under Settings → Plugins → Plugin configuration → 启动动画, or uninstall while preserving the package:

`powershell -ExecutionPolicy Bypass -File C:\Users\ASUS\.dsh\plugins\dsh-boot-animation\tools\uninstall.ps1 -ProfileName desktop`

The uninstaller removes only the plugin patch row and the profile junction. The dated backup above remains available for manual recovery.
