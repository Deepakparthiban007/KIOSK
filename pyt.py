# Flask Example
from flask import Flask, render_template, request
from twilio.rest import Client
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("voice_assistant.html")

@app.route('/twilio', methods = ['POST', 'GET'])
def message():
    if request.method == 'POST':
        # print('Hello')
        # Your Twilio Account SID and Auth Token
        account_sid = 'AC6e3f654be71de9db65962fed9ba40532'
        auth_token = '0d3fb65650a75da03a17c78c6025a327'

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+17438002348',
            to='+919962453227',
            body='for emergency follow the link below for the location See my real-time location on Maps: https://maps.app.goo.gl/LsrYb5Ye6E6HMmos8')

        print('Message Sent:',message.sid)

    return render_template('message.html')

if __name__ == "__main__":
    app.run(debug=True)
    
