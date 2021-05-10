from kafka import KafkaProducer, KafkaConsumer
import json
import requests

ip = "localhost"
producer = KafkaProducer(bootstrap_servers=ip+":9062", acks=1, value_serializer = lambda v: json.dumps(v).encode('utf-8'))

consumer = KafkaConsumer(bootstrap_servers=ip+":9092", api_version=(0,10,1), value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe('getResultUrl')

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

while True:
    for msg in consumer:
        print("DEBUG: Message received with values " + str(msg.value))
        resultUrl = style_transfer(msg.value['styleUrl'], msg.value['imageUrl'])
        print("DEBUG: " + str(resultUrl))
        producer.send('postResultUrl', {'resultUrl': resultUrl['output_url']})
        producer.flush()
        print("DEBUG: Message replied to with values " + str(resultUrl))

producer.close()
consumer.close()

