import spacy
import language_tool_python as ltp

from categories.list import categoriesList
from currencies.list import currencyList

nlp = spacy.load("pt_core_news_sm")
dictionary = ltp.LanguageTool('pt-BR')

def correctSpelling(text: str) -> str:
    try:
        correctedText = ltp.correct(text, dictionary)
    except Exception as e:
        correctedText = text
    return correctedText

def classifyExpense(text):
    processedText = nlp(text)
    lemmas = [token.lemma_ for token in processedText]

    for category, keywords in categoriesList.items():
        if any(keyword in lemmas for keyword in keywords):
            return category
        
    return "Other"
        
def extractValue(text: str) -> str:
    processedText = nlp(text)
    value = 0
    
    for token in processedText:
        if token.like_num and not token.is_alpha:
            value = int(token.text)
            break

    return value

def specifyCurrency(text: str) -> str:
    processedText = nlp(text)
    lemmas = [token.lemma_ for token in processedText]

    for currency, keywords in currencyList.items():
        if any(keyword in lemmas for keyword in keywords):
            return currency
        
    return "Real"


def process(text: str) -> dict:
    correctedText = correctSpelling(text)
    category = classifyExpense(correctedText)
    value = extractValue(correctedText)
    currency = specifyCurrency(correctedText) 
    
    expense = {
        "category": category,
        "value": value,
        "currency": currency
    }
    
    return expense