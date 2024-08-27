import socket
import threading


def handle_client(client_socket):
    try:
        
        data = client_socket.recv(1024)
        print(f"data: {data.decode('utf-8')}")
        
        if data:
            client_socket.sendall(data)
    finally:
        client_socket.close()

def start_server():
    
    # Sunucu için bir TCP/IP soketi oluştur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Sunucu IP adresi ve portu
    server_address = ('0.0.0.0', 2639)
    print(f"Sunucu başlatılıyor {server_address[0]}:{server_address [1]}")
    
    # Soketi belirtilen adrese ve porta bağla
    server_socket.bind(server_address)
    
    # Sunucu dinlemeye başlasın
    server_socket.listen(5)
    print("Bağlantı bekleniyor...")
    
    while True:
    
        # Gelen bağlantıyı kabul et
        client_socket, client_address = server_socket.accept()
        print(f"Bağlantı kuruldu: {client_address}")
        
        # Yeni bir iş parçacığında istemciyi işle
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()

