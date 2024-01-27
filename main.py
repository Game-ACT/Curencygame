import random
from forex_python.converter import CurrencyRates

print("Loading Rate...")

c = CurrencyRates()
cur_rate = int(c.get_rate("USD", "THB"))

print()
print("Loading Done!")
print()

while True:
    try:
        max_cur = int(input("Enter max number of USD for the game... : "))
        break
    except:
        print()
        print("Try again")
        print()

while True:

    while True:
        usd = random.randint(1, max_cur)
        lastusd = 0
        if lastusd != usd:
            break

    thb = usd * cur_rate
    print("What is the THB value of", usd, "USD ?")

    while True:
        try:
            ans = int(input("Enter Answer : "))
            break
        except:
            print()
            print("Try again")
            print()

    if ans - thb <= 0:
        print("The correct answer is", thb, "THB! You are off by", (ans - thb) * -1, "THB!")
    else:
        print("The correct answer is", thb, "THB! You are off by", ans - thb, "THB!")
    print("\n")
    lastusd = usd
