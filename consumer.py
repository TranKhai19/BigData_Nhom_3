from flask import Flask, jsonify, render_template
from kafka import KafkaConsumer
import threading

app = Flask(__name__)
data_received = {'distance': None}

# Consumer Kafka
def consume_kafka():
    global data_received
    consumer = KafkaConsumer('parking_data', bootstrap_servers='localhost:9092')
    for message in consumer:
        data_received = eval(message.value.decode('utf-8'))

# Chạy consumer trong một luồng riêng biệt
threading.Thread(target=consume_kafka, daemon=True).start()

# Trang web hiển thị dữ liệu
@app.route('/')
def index():
    return render_template('index.html', distance=data_received['distance'])

if __name__ == '__main__':
    app.run(debug=True)
