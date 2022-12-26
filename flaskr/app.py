from flask import Flask, request

from main import process

app = Flask("Wealth Wizard")

@app.route("/processexpense", methods=["POST"])
def processExpense():
    
    body = request.get_json()
    
    if "text" not in body:
        
        return responseGenerator(
            400,
            "The text parameter MUST be included"
        )
        
    expense = process(body["text"])
    
    return responseGenerator(
        200,
        "Text succesfully processed!",
        "expense",
        expense
    )

def responseGenerator(status, message, contentName=False, content=False):
    response = {}
    response['status'] = status
    response['message'] = message

    if contentName and content:
        response[contentName] = content
        
    return response

app.run(debug=True)