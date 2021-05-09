from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('./form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_d = dict(request.form.lists())
        val = style_transfer(form_d['styleUrl'][0], form_d['imageUrl'][0])
        form_data = dict()
        form_data['Style Image: '] = form_d['styleUrl'][0]
        form_data['OG Image: '] = form_d['imageUrl'][0]
        form_data['Result Image: '] = val['output_url']
        return render_template('./data.html',form_data = form_data)

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

app.run(host='0.0.0.0', port=5000)
