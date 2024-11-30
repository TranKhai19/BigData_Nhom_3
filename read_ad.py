import serial

# Kết nối đến cổng COM của Arduino (thay COM5 bằng cổng bạn đang sử dụng)
try:
    ser = serial.Serial('COM6', 9600, timeout=1)  # COM5 là cổng Arduino của bạn
    print("Kết nối thành công tới Arduino trên cổng COM6.")
except serial.SerialException:
    print("Không thể kết nối tới Arduino. Hãy kiểm tra lại cổng COM.")
    exit()

while True:
    try:
        # Đọc dữ liệu từ Arduino
        data = ser.readline().decode('utf-8').strip()  # Đọc và giải mã dữ liệu

        # Kiểm tra dữ liệu hợp lệ và hiển thị thông báo
        if data.isdigit():  # Nếu dữ liệu là số (khoảng cách)
            distance = int(data)
            if distance > 30:
                print(f"Khoảng cách: {distance} cm - Vị trí còn chỗ giữ xe.")
            else:
                print(f"Khoảng cách: {distance} cm - Vị trí đã có xe đỗ.")
        else:
            print(f"Dữ liệu nhận được: {data}")

    except KeyboardInterrupt:
        print("Dừng chương trình.")
        break

ser.close()
