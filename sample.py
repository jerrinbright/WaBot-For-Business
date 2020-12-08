from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():

    msg = request.form.get('Body').lower()

    if(msg == "hello"):
        reply = "Hi, hope you have a good day! \nHow may I help you?"

    elif(msg == "order"):
        reply = "Choose Product \n1. Cutters\n2. Tools Bit\n3. Shank Tools\n4. Reamers\n5. Carbide tipped"

    elif(msg == "finish"):
        reply = "Thanks for placing the order. \nNow, you can pay your bill here http://brainmagic.co.in/"    

    elif(msg == "exit"):
        reply = "The order process is terminated."

    elif(msg == "cart"):
        reply = "The list of orders added to cart are:"
    
    else:
        reply = "Sorry. Wrong response. \nKindly start from the beginning."

    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)