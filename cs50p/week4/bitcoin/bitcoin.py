'''
sys.argv is a list of command-line arguments.
sys.argv[0] is always the script name, sys.argv[1] is the first argument.
We check len(sys.argv) != 2 to ensure exactly one argument was passed.
sys.exit() terminates the program with an error message.

requests.get() fetches the URL and returns a response object.
response.json() converts the JSON response into a Python dictionary.
We navigate the dictionary with data["data"]["priceUsd"] to get the price.
priceUsd comes back as a string so we wrap it in float() before multiplying.

f"${amount:,.4f}" formats the number to 4 decimal places with a comma
as a thousands separator e.g. $97,845.0000.
'''

import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    arg = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}")
except requests.RequestException:
    sys.exit("Missing command-line argument")

dict = response.json()
price = float(dict["data"]["priceUsd"])
amount = price * arg

print(f"${amount:,.4f}")