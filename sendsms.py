from twilio.rest import TwilioRestClient 
import time
a = '''Head 'southwest' on 'Basai Rd'
Turn 'left' onto 'Railway Rd' - Pass by Nehru Stadium (on the left in 450 m)
Continue straight through 'Rajiv Chowk' to stay on 'Railway Rd'
At the roundabout, take the '1st' exit
Take the ramp on the 'right' onto 'NH8' - Partial toll road - Pass by Indira Gandhi International Airport (on the left in 15.0 km)
Keep 'left' to stay on 'NH8' - Pass by Air Force Museum (on the right in 1.4 km)
Continue straight to stay on 'NH8' - Drive along Manekshaw Centre (on the left for 280 m)
Continue onto 'Sardar Patel Marg' - Pass by ITC Maurya (on the right in 650 m)
Turn 'right' onto 'Mother Teresa Cres'
At 'Teen Murti Cir', take the '1st' exit onto 'South Ave'
Turn 'right' onto 'Dalhousie Rd' - Pass by Rashtrapati Bhavan (on the left)
At the roundabout, take the '2nd' exit and stay on 'Dalhousie Rd'
  ''' 
# put your own credentials here 
def send_text(data):
  ACCOUNT_SID = "AC643827145bf34449eaed29541061cb61" 
  AUTH_TOKEN = "d95e4350d5c7a08dd74ba98ae3f6b4cf" 
   
  client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
  
  n=120
  for j in [data[i:i+n] for i in range(0, len(data), n)]:
    print j
    client.messages.create(
      to="+919670663399", 
      from_="+12513339847", 
      body=j
    )
    time.sleep(10)
print a
send_text(a)
