import json

from main import process

text = input("Insira o gasto: ")
expense = process(text)

print(json.dumps(expense, indent=2))