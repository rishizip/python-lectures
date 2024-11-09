# waf to convert USD to INR
def converter(usd_val):
    inr_val = usd_val * 84.13
    print(f"{usd_val} USD = {inr_val} INR")

usd_val = float(input("Enter amount in USD to convert to INR : "))

converter(usd_val)
