from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'AC6e3f654be71de9db65962fed9ba40532'
auth_token = '0d3fb65650a75da03a17c78c6025a327'

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+17438002348',
    to='+919962453227',
    body='for emergency follow the link below for the location See my real-time location on Maps: https://maps.app.goo.gl/LsrYb5Ye6E6HMmos8')

print(message.sid)