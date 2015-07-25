from twilio.rest import TwilioRestClient 
a = '''Step 1 - Walk to Janpath
  Head 'southeast' on 'Connaught Circus' toward 'Baba Kharak Singh Marg'
  Turn 'right' after Palika Bazaar (on the left) - Pass by STC Bldg (on the left in 100 m) - Destination will be on the right

Step 2 - Metro rail towards Badarpur
  Total Stops: 10
  From: Janpath
  To: Govind Puri
  Line: Violet ( ITO - Badarpur )

Step 3 - Walk to E-43/1, Okhla Industrial Area II, Pocket D, Okhla Phase II, Okhla Industrial Area, New Delhi, Delhi 110020, India
  Head 'south' toward 'Guru Ravidas Marg'
  Slight 'left' onto 'Ma Anandmayee Marg'
  Turn 'left'
  Turn 'right' - Destination will be on the left
  ''' 
# put your own credentials here 
def send_text(data):
  ACCOUNT_SID = "AC643827145bf34449eaed29541061cb61" 
  AUTH_TOKEN = "d95e4350d5c7a08dd74ba98ae3f6b4cf" 
   
  client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
   
  client.messages.create(
    to="+14087580894", 
    from_="+12513339847", 
    body=data
  )
print a
send_text(a)
