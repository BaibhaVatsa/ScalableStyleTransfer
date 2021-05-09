from kafka import KafkaProducer, KafkaConsumer
import json

ip = "localhost"
producer = KafkaProducer(bootstrap_servers=f"{ip}:9062", acks=1, value_serializer = lambda v: json.dumps(v).encode('utf-8'))

consumer = KafkaConsumer(bootstrap_servers=f"{ip}:9092", api_version=(0,10,1), value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe('getResultUrl')

while True:
    for msg in consumer:
        print(msg.value)
        producer.send('postResultUrl', {'resultUrl': 'LALALALA'})
        producer.flush()

def style_transfer(styleUrl, imageUrl):
    r = requests.post(
        "https://api.deepai.org/api/fast-style-transfer",
        data={
            'content': imageUrl,
            'style': styleUrl,
        },
        headers={'api-key': 'b1c8c62e-1063-40d3-a56d-f5e3256a2237'}
    )
    return r.json()

producer.close ()
consumer.close()

