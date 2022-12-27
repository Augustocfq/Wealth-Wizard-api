import requests

def getInvestmentInfo(key: str, ticker: str) -> dict:
    
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"
    
    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
    
    params = {
        "symbol": ticker + ".SA"
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        
        companyName = response.json()['price']['longName']
        marketPrice = response.json()['price']["regularMarketPrice"]['raw']
        
        investmentInfo = {
            "Company Name": companyName,
            "Market Price": marketPrice
        }
        
        return (investmentInfo)
        
    else:
        
        errorInfo = {
            "Message": "Yahoo Finance API request failed",
            "Status": {response.status_code}
        }
        
        return (errorInfo)
    