from flask import Flask, request, redirect
from flask import make_response, current_app, abort, jsonify
from datetime import timedelta
from functools import update_wrapper
import os, urllib
import twilio.twiml
from twilio.rest import TwilioRestClient 
import requests
from directions import *
import time

app = Flask(__name__)
 
def crossdomain(origin=None, methods=None, headers=None,
        max_age=21600, attach_to_all=True,
        automatic_options=True):
  if methods is not None:
    methods = ', '.join(sorted(x.upper() for x in methods))
  if headers is not None and not isinstance(headers, basestring):
    headers = ', '.join(x.upper() for x in headers)
  if not isinstance(origin, basestring):
    origin = ', '.join(origin)
  if isinstance(max_age, timedelta):
    max_age = max_age.total_seconds()

  def get_methods():
    if methods is not None:
      return methods

    options_resp = current_app.make_default_options_response()
    return options_resp.headers['allow']

  def decorator(f):
    def wrapped_function(*args, **kwargs):
      if automatic_options and request.method == 'OPTIONS':
        resp = current_app.make_default_options_response()
      else:
        resp = make_response(f(*args, **kwargs))
      if not attach_to_all and request.method != 'OPTIONS':
        return resp

      h = resp.headers

      h['Access-Control-Allow-Origin'] = origin
      h['Access-Control-Allow-Methods'] = get_methods()
      h['Access-Control-Max-Age'] = str(max_age)
      if headers is not None:
        h['Access-Control-Allow-Headers'] = headers
      return resp

    f.provide_automatic_options = False
    return update_wrapper(wrapped_function, f)
  return decorator

#------------------------------------------------------------------------------
def send_text(data,from_):
    ACCOUNT_SID = "AC643827145bf34449eaed29541061cb61" 
    AUTH_TOKEN = "d95e4350d5c7a08dd74ba98ae3f6b4cf" 
     
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
    
    n=120
    for j in [data[i:i+n] for i in range(0, len(data), n)]:
        print j
        client.messages.create(
            # to=from_, 
            to='+919670663399', 
            from_="+12513339847", 
            body=j
        )
        time.sleep(10)


def translation(text,destination,source='auto'):
    lang = {
        'spanish':'es',
        'french': 'fr',
        'german': 'de',
        'russian': 'ru',
        'hindi': 'hi'
    }

    url = 'https://translate.google.com/translate_a/single?client=t&sl='+source+'&tl='+lang[destination]+'&hl=en&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&ie=UTF-8&oe=UTF-8&ssel=0&tsel=4&otf=1&kc=3&tk=522173|238876&'+urllib.urlencode({'q':text})

    data = requests.get(url).text

    while data.find(',,')>0:
        data = data.replace(',,',',')

    while data.find('[,')>0:
        data = data.replace('[,','[')

    while data.find(',]')>0:
        data = data.replace(',]',']')

    print data
    data = json.loads(data)

    return data[0][0][0]


def directions(body,mode):
    source = body[body.index('from')+4:body.index('to')]
    destination = body[body.index('to')+2:]
    if mode=='metro':
        message = getDirectionsMetro(source,destination)
    elif mode=='driving':
        message = getDirectionsDriving(source,destination)
    elif mode=='walking':
        message = getDirectionsWalking(source,destination)
    return message
 
@app.route("/", methods=['GET', 'POST'])
@crossdomain(origin='*')
def hello_monkey():
    """Respond and greet the caller by name."""
 
    for i in request.args:
        print i,'\t\t', request.args[i]
    body = request.args['Body']
    from_ = request.args['From']
    
    try:
        if body.split()[0].lower() == 'directions' or body.split()[1].lower() == 'directions':
            if body.split()[0].lower() == 'driving':
                message = directions(body,'driving')
            elif body.split()[0].lower() == 'walking':
                message = directions(body,'walking')
            else:
                message = directions(body,'metro')

        elif body.split()[0].lower() == 'translate':
            message = translation(' '.join(body.split()[3:]),body.split()[2].lower())

        elif ( body.split()[0].lower() == 'place' or body.split()[0].lower() == 'places' ) and body.split()[1].lower() == 'search':
            message = placeSearch(' '.join(body.split()[2:]))

        resp = twilio.twiml.Response()
        resp.message(message)
        # send_text(message,from_)
        print str(resp)
        return str(resp)
    except Exception as e:
        print 'error occured'
        print e
        return "Can't make sense of the text. try clearifying it."

port = int(os.environ.get('PORT', 5000))
if __name__ == "__main__":
    print 'PORT: ',port
    app.run(debug=True,port=port,host='0.0.0.0')
