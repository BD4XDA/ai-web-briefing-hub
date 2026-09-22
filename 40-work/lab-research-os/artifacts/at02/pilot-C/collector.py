import hashlib, json, os, sys
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = Path(r"D:/A每日论文阅读_沉积物磷形态与生物地球化学")
AREA = ROOT / "00_总索引"
MAX_FILES = 30
MAX_DEPTH = 2

def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

def stat_record(path, base):
    st = path.stat()
    return {
        "relative_path": path.relative_to(base).as_posix(),
        "absolute_path": str(path),
        "entry_type": "directory" if path.is_dir() else "file",
        "extension": path.suffix,
        "bytes": st.st_size if path.is_file() else None,
        "mtime_utc": datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat().replace("+00:00", "Z"),
        "attributes": {"is_symlink": path.is_symlink()}
    }

captured_at = now()
top = []
for p in sorted(ROOT.iterdir(), key=lambda x: x.name):
    top.append(stat_record(p, ROOT))

files = []
dirs = []
for p in sorted(AREA.rglob("*"), key=lambda x: x.as_posix()):
    rel_depth = len(p.relative_to(AREA).parts)
    if rel_depth > MAX_DEPTH or p.is_symlink():
        continue
    rec = stat_record(p, AREA)
    (dirs if p.is_dir() else files).append(rec)
if len(files) > MAX_FILES:
    raise RuntimeError(f"bounded file budget exceeded: {len(files)} > {MAX_FILES}")

index_path = AREA / "总索引.md"
index_captured = False
index_sha = None
index_snapshot = None
if index_path.is_file() and index_path.stat().st_size <= 128 * 1024:
    raw = index_path.read_bytes()
    index_snapshot = OUT / "index-snapshot.md"
    index_snapshot.write_bytes(raw)
    index_sha = hashlib.sha256(raw).hexdigest()
    index_captured = True

payload = {
    "capture_id": "at02-pilot-C-capture-20260921",
    "task_id": "AT02-pilot-C",
    "captured_at": captured_at,
    "source_root": str(ROOT),
    "top_level_listing": top,
    "selection": {
        "selected_area": str(AREA),
        "selection_reason": "00_总索引 exists and is the packet-preferred index/manifest area; bounded to depth 2.",
        "max_files": MAX_FILES,
        "max_depth": MAX_DEPTH,
        "omissions": ["All areas other than 00_总索引", "symlinked entries", "files deeper than depth 2"]
    },
    "selected_area_directories": dirs,
    "selected_area_files": files,
    "safe_index": {
        "path": str(index_path),
        "captured": index_captured,
        "snapshot_path": str(index_snapshot) if index_snapshot else None,
        "bytes": index_path.stat().st_size if index_path.is_file() else None,
        "sha256": index_sha,
        "purpose": "explicit project association and structure only; no paper bodies or PDFs read"
    }
}
(OUT / "raw-capture.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"capture": str(OUT / "raw-capture.json"), "files": len(files), "index_captured": index_captured}, ensure_ascii=False))
