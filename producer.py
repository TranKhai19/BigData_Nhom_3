import serial
from kafka import KafkaProducer

# Kết nối với Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Kết nối với Arduino
try:
    ser = serial.Serial('COM6', 9600, timeout=1)
    print("Kết nối thành công tới Arduino.")
except serial.SerialException:
    print("Không thể kết nối tới Arduino.")
    exit()

while True:
    try:
        # Đọc dữ liệu từ Arduino
        data = ser.readline().decode('utf-8').strip()

        if data.isdigit():
            distance = int(data)
            message = {
                'distance': distance
            }
            producer.send('parking_data', str(message).encode('utf-8'))
            print(f"Gửi dữ liệu: {message}")
    except KeyboardInterrupt:
        break

ser.close()
