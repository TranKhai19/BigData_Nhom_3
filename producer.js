const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'my-producer',
  brokers: ['localhost:9092']
});

const producer = kafka.producer();

const run = async () => {
  await producer.connect();
  
  // Gửi dữ liệu
  setInterval(async () => {
    const message = {
      value: JSON.stringify({
        timestamp: new Date().toISOString(),
        message: 'Hello from Kafka!'
      })
    };
    await producer.send({
      topic: 'web-topic',
      messages: [message]
    });
    console.log('Message sent:', message);
  }, 5000); // Gửi dữ liệu mỗi 5 giây
};

run().catch(console.error);
