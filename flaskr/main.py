import spacy

from categories.list import categoriesList
from currencies.list import currencyList

nlp = spacy.load("pt_core_news_sm")

def classifyExpense(text):
    processedText = nlp(text)
    lemmas = [token.lemma_ for token in processedText]

    for category, keywords in categoriesList.items():
        if any(keyword in lemmas for keyword in keywords):
            return category
        
    return "Other"
        
def extractValue(text):
    processedText = nlp(text)
    value = 0
    
    for token in processedText:
        if token.like_num and not token.is_alpha:
            value = int(token.text)
            break

    return value

def specifyCurrency(text):
    processedText = nlp(text)
    lemmas = [token.lemma_ for token in processedText]

    for currency, keywords in currencyList.items():
        if any(keyword in lemmas for keyword in keywords):
            return currency
        
    return "Real"


def process(text):
    category = classifyExpense(text)
    value = extractValue(text)
    currency = specifyCurrency(text)
    
    expense = {
        "category": category,
        "value": value,
        "currency": currency
    }
    
    return expense