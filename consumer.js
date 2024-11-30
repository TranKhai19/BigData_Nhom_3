const express = require('express');
const { Kafka } = require('kafkajs');

const app = express();
const kafka = new Kafka({
  clientId: 'distance-app',
  brokers: ['localhost:9092']
});

const consumer = kafka.consumer({ groupId: 'distance-group' });
let latestMessage = 'No data received yet';

const startConsumer = async () => {
  await consumer.connect();
  await consumer.subscribe({ topic: 'distance-data', fromBeginning: false });

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      latestMessage = message.value.toString(); // Cập nhật message mới nhất
      console.log(`Received message: ${latestMessage}`);
    },
  });
};

startConsumer().catch(console.error);

app.get('/', (req, res) => {
  res.send(`Latest Distance Data: ${latestMessage}`);
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
