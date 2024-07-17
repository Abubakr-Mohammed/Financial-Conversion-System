CURRENCIES = {
    'USD': 1,
    'EUR': 1.09,
    'YEN': 0.0064,
    'GBP': 1.30,
    'AUD': 0.67,
    'CAD': 0.73,
    'COP': 0.00025,
    'INR': 0.012,
    'RUB': 0.011,
    'CHF': 1.13
}

# Write code here
def to_usd(code: str, amount: float) -> float:
    if code not in CURRENCIES:
        raise ValueError(f"{code} is not supported")
    if amount < 0:
        raise ValueError("Invalid amount")
    exchange_rate = CURRENCIES[code]
    return amount * exchange_rate

def from_usd(code: str, usd_Amount: float) -> float:
    if code not in CURRENCIES:
        return code + " is not supported"
    if usd_Amount < 0:
        raise ValueError("Invalid amount")
    exchange_rate = CURRENCIES[code]
    return round(usd_Amount / exchange_rate, 2)

def convert(currency: str, amount: float, to_currency: str) -> str:
    try:
        if currency not in CURRENCIES:
            x = currency + " currency is not supported"
            print(x)
            return x
        elif to_currency not in CURRENCIES:
            res = to_currency + " currency is not supported"
            print(res)
            return res
        amount_in_usd = to_usd(currency, amount)
        
        # Convert from USD to the target currency
        converted_amount = from_usd(to_currency, amount_in_usd)
        # Print the result
        result = f"{amount} {currency} is equivalent to {converted_amount} {to_currency}"
        print(result)
        return result
    except ValueError as ve:
        print("Invalid amount")

user_inp = input("Enter the currency you want to be convert: ")
amount_inp = int(input("How much are you converting?: "))
second_inp = input("What currency should we convert it to ?: ")
user_amount = convert(user_inp, amount_inp, second_inp)