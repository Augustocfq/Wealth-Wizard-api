from flask import Flask, request

from keys import YAHOO_FINANCE_API_KEY
from responseModel import responseGenerator
from api.investmentApi import getInvestmentInfo

from main import process

app = Flask("Wealth Wizard")

@app.route("/process-expense", methods=["POST"])
def processRoute():
    
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

@app.route("/get-investment-info", methods=["POST"])
def getInvestmentInfoRoute():
    
    body = request.get_json()
    
    if "ticker" not in body:
        
        return responseGenerator(
            400,
            "The ticker parameter MUST be included"
        )
        
    ticker = body["ticker"]
    
    return responseGenerator(
        200,
        "investmentApi successfully called",
        "investmentApi response:",
        getInvestmentInfo(YAHOO_FINANCE_API_KEY, ticker)
    )
    

app.run(debug=True)