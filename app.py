from flask import Flask, jsonify, request
import serial

app = Flask(__name__)

# Kết nối đến cổng nối tiếp của Arduino (COMx là cổng của bạn)
try:
    ser = serial.Serial('COM6', 9600, timeout=1)  # COM5 là cổng Arduino của bạn
    print("Kết nối thành công tới Arduino trên cổng COM5.")
except serial.SerialException:
    print("Không thể kết nối tới Arduino. Hãy kiểm tra lại cổng COM.")
    exit()


@app.route('/receive', methods=['POST'])
def receive_data():
    # Đọc dữ liệu từ cổng nối tiếp
    distance = None
    try:
        distance = ser.readline().decode('utf-8').strip()  # Đọc và giải mã dữ liệu
        print(f"Received distance: {distance}")  # In dữ liệu ra console để kiểm tra
    except serial.SerialException as e:
        return jsonify({"error": str(e)}), 500

    if not distance or distance == "Out of range":
        return jsonify({"error": "Invalid distance received"}), 400

    try:
        distance = int(distance)  # Chuyển đổi chuỗi thành số nguyên
    except ValueError:
        return jsonify({"error": "Invalid distance value"}), 400

    # Kiểm tra khoảng cách và trả về trạng thái
    if distance > 100:
        status = "Chỗ giữ xe còn trống"
    else:
        status = "Vị trí đã được đổ xe"

    return jsonify({"distance": distance, "status": status})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
