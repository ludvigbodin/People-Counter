def start_socket():
    from flask import Flask, render_template
    from flask_restful import reqparse
    from flask_socketio import SocketIO

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    socket = SocketIO(app, cors_allowed_origins="*")

    @app.route('/trigger')
    def index():
        print("Hello")
        return {"ok": "200"}

    @socket.on('connect')
    def on_connect():
        print("NEW ONE")

    @socket.on('send')
    def handle_message(message):
        print('received message: ' + message)

    @socket.on('send_message')
    def on_chat_sent(data):
        emit('message_sent', data)


    if __name__ == '__main__':
        socket.run(app)
