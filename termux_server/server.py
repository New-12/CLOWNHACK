from flask import Flask, request
import os

app = Flask(__name__)

# Dosyaların kaydedileceği klasör
RECEIVED_FILES_DIR = "received_files"
os.makedirs(RECEIVED_FILES_DIR, exist_ok=True)

@app.route("/", methods=["POST"])
def receive_message():
    data = request.get_json()
    if not data or "type" not in data:
        return "Geçersiz istek!", 400

    if data["type"] == "message":
        phone = data.get("phone", "")
        message = data.get("message", "")
        print(f"📩 Gelen mesaj [{phone}]: {message}")
        return f"Mesaj alındı: {message}", 200

    return "Bilinmeyen tür!", 400

@app.route("/file", methods=["POST"])
def receive_file():
    phone = request.form.get("phone", "")
    file = request.files.get("file")

    if file:
        file_path = os.path.join(RECEIVED_FILES_DIR, file.filename)
        file.save(file_path)
        print(f"📁 Gelen dosya [{phone}]: {file.filename} -> {file_path}")
        return f"Dosya kaydedildi: {file.filename}", 200
    else:
        return "Dosya bulunamadı!", 400

if __name__ == "__main__":
    # Flask sunucusu 0.0.0.0 üzerinden dış bağlantılara da açık olacak
    app.run(host="0.0.0.0", port=5000)
