import requests
import os

SERVER_URL = "http://192.168.1.101:5000"  # Termux IP adresi ve port

def send_message():
    phone = input("Alıcı numarası (+905xxxxxxxxx): ")
    message = input("Mesaj içeriği: ")

    data = {
        "type": "message",
        "phone": phone,
        "message": message
    }

    try:
        response = requests.post(f"{SERVER_URL}/", json=data)
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
            data = {"phone": phone}
            response = requests.post(f"{SERVER_URL}/file", files=files, data=data)
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
