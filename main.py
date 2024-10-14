from flask import Flask, jsonify, request,Response

from telewbot.services.service import parse_msg, send_msg

app = Flask(__name__)

    
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        id, answer = parse_msg(msg)

        #if city is not found, asks to enter correct name
        if not answer:
            send_msg(id, "Проверьте написание города")
            return Response('ok', status=200)
        
        send_msg(id, answer)
        return Response('ok', status=200)
    else:
        return "Чтобы узнать погоду, введите название города на английском языке."
    

if __name__ == '__main__':
    app.run(debug=True)
