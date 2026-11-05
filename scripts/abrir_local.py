"""Open this source tree using its own or the existing Poupa Grana local runtime."""
import os
import subprocess
import sys
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
LOCAL = Path.home() / 'Music' / 'POSTAGEM' / 'poupa-grana'
load_dotenv(ROOT / '.env')
if not (ROOT / '.env').exists():
    load_dotenv(LOCAL / '.env')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
print('Poupa Grana: http://127.0.0.1:5090/entrar/', flush=True)
print('Mantenha esta janela aberta enquanto usa o sistema.', flush=True)
subprocess.run([sys.executable, str(ROOT / 'manage.py'), 'runserver', '127.0.0.1:5090', '--insecure', '--noreload'], cwd=ROOT, check=True)
