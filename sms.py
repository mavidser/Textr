from flask import Flask, request, redirect
import os
# import twilio.twiml
 
app = Flask(__name__)
 
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+918982896363": "Sid",
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
 
    for i in request.args:
        print i,'\t\t', request.args[i]
    return 'sdfsf'
    # from_number = request.values.get('From', None)
    # if from_number in callers:
    #     message = callers[from_number] + ", thanks for the message!"
    # else:
    #     message = "Monkey, thanks for the message!"
 
    # resp = twilio.twiml.Response()
    # resp.message(message)
    # return str(resp)

port = int(os.environ.get('PORT', 5000))
if __name__ == "__main__":
    print 'PORT: ',port
    app.run(debug=True,port=port,host='0.0.0.0')
