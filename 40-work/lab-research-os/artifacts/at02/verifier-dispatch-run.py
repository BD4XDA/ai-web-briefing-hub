import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VERIFY = ROOT / 'artifacts' / 'at02' / 'verify-pilots.py'
CAPTURE = ROOT / 'artifacts' / 'at02' / 'verifier-dispatch-execution.json'

def stamp():
    return datetime.now(timezone.utc).isoformat()

raw = VERIFY.read_bytes()
record = {
    'command': [sys.executable, str(VERIFY)],
    'working_directory': str(ROOT),
    'verifier_script': str(VERIFY),
    'verifier_script_sha256': hashlib.sha256(raw).hexdigest(),
    'started_at_utc': stamp(),
}
start = time.monotonic()
try:
    proc = subprocess.run(
        [sys.executable, str(VERIFY)],
        cwd=ROOT,
        capture_output=True,
        timeout=150,
        check=False,
    )
    record.update({
        'exit_code': proc.returncode,
        'stdout': proc.stdout.decode('utf-8', errors='replace'),
        'stderr': proc.stderr.decode('utf-8', errors='replace'),
    })
except subprocess.TimeoutExpired as exc:
    record.update({
        'exit_code': None,
        'timeout': True,
        'stdout': (exc.stdout or b'').decode('utf-8', errors='replace'),
        'stderr': (exc.stderr or b'').decode('utf-8', errors='replace'),
    })
record['finished_at_utc'] = stamp()
record['duration_seconds'] = time.monotonic() - start
CAPTURE.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8', newline='')
sys.stdout.buffer.write(record.get('stdout', '').encode('utf-8'))
sys.stderr.buffer.write(record.get('stderr', '').encode('utf-8'))
sys.exit(record['exit_code'] if record['exit_code'] is not None else 124)
