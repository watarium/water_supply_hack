import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def preds():
    data = request.data.decode('utf-8')
    data = json.loads(data)

    hour = data['hour']
    temperature = data['temperature']
    humidity = data['humidity']
    water = data['water']

    result = 'Data is submitted correctly.\nhour= ' + str(hour) + ', tempetature= ' + str(temperature) + ', humidity=' + str(humidity) + ', water=' + str(water) + '\n'
    with open('./result.csv', mode='a') as f:
        f.write(str(hour) + ', ' + str(temperature) + ', ' + str(humidity) + ', ' + str(water) + '\n')

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0')