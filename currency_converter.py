"""This program converts South African Rand(ZAR) to other currencies and 
vice versa. Market values were captured on 13/09/24.
"""

# Three lists that hold currency related details.
currency_descriptions = [
    "US Dollar",
    "British Pound",
    "Japanese Yen",
    "Canadian Dollar",
    "Euro",
    "Russian Rouble",
    "Chinese Yuan Renminbi"
]

currency_values = [
    17.8787,
    23.3666,
    0.12557,
    13.1635,
    19.7251,
    0.19672,
    2.51087
]

currency_code = [
    "USD",
    "GBP",
    "JPY",
    "CAD",
    "EUR",
    "RUB",
    "CNY"
]


def enter_amount():
    """Takes user input and checks if it meets the necessary 
    requirements.
    """
    while True:
            try:
                user_value = float(input("Please enter the amount to be \
converted: "))

                if user_value <= 0:
                    print("Please enter an appropriate amount.")

                else:
                    break

            except ValueError:
                print("Please enter a numerical amount.")

    return user_value


def currency_select():
    """Allows the user to select a currency from a list."""
    index = 1

    for value in currency_descriptions:
        print(f"{index}. {value}")
        index += 1

    while True:
        try:
            currency_select = int(input("Type a number to select an option: "))

            if currency_select < 1 or currency_select > 7:
                print("Please enter an appropriate value.")
                
            else:
                break

        except ValueError:
            print("Please enter an appropriate value.")

    currency_select -= 1

    return currency_select


def convert_from_ZAR(amount, currency):
    """Converts the amount from ZAR to another currency."""
    converted_amount = amount / currency_values[currency]

    converted_amount = round(converted_amount, 2)

    return converted_amount


def convert_to_ZAR(amount, currency):
    """Converts another currency to ZAR."""
    converted_amount = amount * currency_values[currency]

    converted_amount = round(converted_amount, 2)

    return converted_amount


while True:
    user_input = input("""Welcome to the Currency Converter. Type the number 
to select an option: 
1. Convert ZAR to another currency
2. Convert another currency to ZAR                       
3. Exit 
""")
    
    # Convert ZAR to another currency.
    if user_input == "1":
        user_value = enter_amount()

        user_currency = currency_select()
        
        result = convert_from_ZAR(user_value, user_currency)

        print(f"The amount is : {result} {currency_code[user_currency]}")

    # Convert another currency to ZAR.
    elif user_input == "2":
        user_value = enter_amount()

        user_currency = currency_select()
        
        result = convert_to_ZAR(user_value, user_currency)

        print(f"The amount is: {result} ZAR")

    # Exit the program.
    elif user_input == "3":
        break

    # Reenter an input.
    else:
        print("Please select an appropriate option.")