import requests
import os

# TERMUX SERVER IP otomatik alınır ve PORT eklenir
ip = requests.get("https://api.ipify.org").text.strip()
SERVER_URL = f"http://{ip}:5000"  # Örneğin Termux sunucusu 5000 portunu dinliyor

def send_message():
    phone = input("Alıcı numarası (+905xxxxxxxxx): ")
    message = input("Mesaj içeriği: ")

    data = {
        "type": "message",
        "phone": phone,
        "message": message
    }

    try:
        response = requests.post(f"{SERVER_URL}/api/message", json=data)
        print("✅ Mesaj gönderildi. Sunucu cevabı:", response.text)
    except Exception as e:
        print("❌ Hata:", e)

def send_file():
    phone = input("Alıcı numarası (+905xxxxxxxxx): ")
    file_path = input("Gönderilecek dosya yolu: ")

    if not os.path.exists(file_path):
        print("❌ Dosya bulunamadı!")
        return

    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            data = {"type": "file", "phone": phone}
            response = requests.post(f"{SERVER_URL}/api/file", files=files, data=data)
            print("✅ Dosya gönderildi. Sunucu cevabı:", response.text)
    except Exception as e:
        print("❌ Hata:", e)

def main():
    print("CLOWNHACK — Yasal Dosya / Mesaj Gönderici\n")
    print("1 - Mesaj Gönder")
    print("2 - Dosya Gönder")
    secim = input("Seçimin (1/2): ")

    if secim == "1":
        send_message()
    elif secim == "2":
        send_file()
    else:
        print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    main()

