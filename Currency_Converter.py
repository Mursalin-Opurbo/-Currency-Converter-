#convert your currency
rates = {
    "USD": 1.0,
    "EUR": 0.91,
    "GBP": 0.78,
    "INR": 83.0,
    "JPY": 156.4,
    "AUD": 1.50,
    "CAD": 1.36,
    "CHF": 0.89,
    "CNY": 7.23,
    "SEK": 10.59,
    "NZD": 1.66,
    "MXN": 17.05,
    "BRL": 5.15,
    "ZAR": 18.40,
    "RUB": 91.00,
    "KRW": 1350.5,
    "SGD": 1.35,
    "HKD": 7.82,
    "MYR": 4.70,
    "THB": 36.5
}

amount = float(input("Enter amount in USD: "))
print("Available currencies: USD, EUR, GBP, INR, JPY, AUD, CAD, CHF, CNY, SEK, NZD, MXN, BRL, ZAR, RUB, KRW, SGD, HKD, MYR, THB")

currency = input("Convert to: ").upper()

if currency in rates:
    converted = amount * rates[currency]
    print(f"{amount} USD = {converted:.2f} {currency}")
else:
    print("Currency not supported.")
