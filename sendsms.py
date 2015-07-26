from twilio.rest import TwilioRestClient 
a = '''Turn 'right' after Palika Bazaar (on the left) - Pass by STC Bldg (on the left in 100 m) - Destination will be on the right''' 
# put your own credentials here 
def send_text(data):
  ACCOUNT_SID = "AC643827145bf34449eaed29541061cb61" 
  AUTH_TOKEN = "d95e4350d5c7a08dd74ba98ae3f6b4cf" 
   
  client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
   
  client.messages.create(
    to="+919670663399", 
    from_="+12513339847", 
    body=data
  )
print a
send_text(a)
