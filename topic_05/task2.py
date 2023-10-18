import requests

def convert_currency(amount, currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    
    response = requests.get(url)
    data = response.json()
    
    if data:
        exchange_rate = data[0]["rate"]
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None

# Enter the amount and currency code (USD, EUR, or PLN)
amount = float(input("Enter the amount: "))
currency_code = input("Enter the currency code (USD, EUR, or PLN): ").upper()

converted_amount = convert_currency(amount, currency_code)

if converted_amount is not None:
    print(f"{amount} {currency_code} = {converted_amount} UAH")
else:
    print("Error retrieving currency exchange rate.")