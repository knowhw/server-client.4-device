import socket
import json

# JSON formatında bir mesaj
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# JSON mesajını string formatına dönüştür
json_data = json.dumps(data)

# Sunucu bilgileri
host = 'localhost'  # veya sunucu IP adresi
port = 2440

# TCP istemci soketini oluştur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Sunucuya bağlan
    client_socket.connect((host, port))
    
    # JSON mesajını gönder
    client_socket.sendall(json_data.encode('utf-8'))
    
    # Sunucudan gelen cevabı al
    response = client_socket.recv(1024)
    print('Sunucudan gelen cevap:', response.decode('utf-8'))

finally:
    # Soketi kapat
    client_socket.close()

