from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello"

@app.route('/register')
def register_user():
    
    name = request.args.get("name")
    host = request.args.get("host")
    port = request.args.get("port")
    
    if not all([host, port, name]):
        return Response('Не хватает обязательного параметра', 404)
    
    
    with open('services.json', 'a') as fin:
        service_info = {'host': host, 'name': name, 'port': int(port)}
        json.dump(service_info, fin)
        fin.write('\n')
    
    return 'Регистрация прошла успешно'
