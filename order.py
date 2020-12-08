from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():

    incoming_msg = request.form.get('Body').lower()
    
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if "hello" in incoming_msg:
        msg.body("Hi, hope you have a good day! \nHow may I help you?")
        responded = True

    elif "order" in incoming_msg:
    	msg.body("Choose Product \n1. Cutters\n2. Tools Bit\n3. Shank Tools\n4. Reamers\n5. Carbide tipped")
    	responded = True

    elif(incoming_msg == "1"):
    	r = requests.get('')
    	if r.status_code == 200:
    		data = r.json()
    		res = "Choose your sub-category"
    	else:
    		res = "Not able to retrieve data. \n Please try again."
    	msg.body(res)
    	responded = True

    elif "finish" in incoming_msg:
        msg.body("Thanks for placing the order. \nNow, you can pay your bill here http://brainmagic.co.in/") 

    elif "exit" in incoming_msg:
    	msg.body("The order process is terminated.")

    elif "cart" in incoming_msg:
    	msg.body("The list of orders added to cart are:")
    
    else:
    	msg.body("Sorry. Wrong response. \nKindly start from the beginning.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)