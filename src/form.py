from flask import Flask,render_template,request
import requests
from kafka import KafkaProducer, KafkaConsumer
import json
## overlay network for swarm
app = Flask(__name__)

ip = "35.172.203.159"
producer = KafkaProducer(bootstrap_servers=ip+":9092", acks=1, value_serializer = lambda v: json.dumps(v).encode('utf-8'))

consumer = KafkaConsumer(bootstrap_servers=ip+":9062", api_version=(0,10,1), value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe('postResultUrl')

@app.route('/')
def form():
    return render_template('./form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return "The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_d = dict(request.form.lists())
        form_data = dict()
        form_data['Style Image: '] = form_d['styleUrl'][0]
        form_data['OG Image: '] = form_d['imageUrl'][0]

        producer.send('getResultUrl', {'styleUrl': form_d['styleUrl'][0], 'imageUrl': form_d['imageUrl'][0]})
        producer.flush()

        for msg in consumer:
            form_data['Result Image: '] = msg.value['resultUrl']
            break

        return render_template('./data.html',form_data = form_data)

app.run(host='0.0.0.0', port=5000)
producer.close ()
consumer.close()

