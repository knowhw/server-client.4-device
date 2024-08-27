from device import state
# import device
import time
import datetime
import socket
import json

test_p=dict

data = state.devices()
dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#2024-08-27 12:34:56 INFO sda1: fstype=vfat, label=null, uuid=4A35-C66D, mountpoint=/media/linux/4A35-C66D, mounted=false, plugged=true
#2024-08-27 12:34:56 INFO mmcblk1p1: fstype=vfat, label=null, uuid=6335-3364, mountpoint=/media/linux/6335-3364, mounted=true, plugged=true
test_p=data
for item in test_p: test_p [item ] ['dt'] =  dt
# JSON mesajını string formatına dönüştür
json_data = json.dumps(test_p)

# Sunucu bilgileri
host = 'localhost'  # veya sunucu IP adresi
port = 2639

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
