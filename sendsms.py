from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
def send_text(data):
  ACCOUNT_SID = "AC643827145bf34449eaed29541061cb61" 
  AUTH_TOKEN = "d95e4350d5c7a08dd74ba98ae3f6b4cf" 
   
  client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
   
  client.messages.create(
    to="+12513339847", 
    from_="+12513339847", 
    body=data
  )

send_text("Hola!")
