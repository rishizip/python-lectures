# waf to convert USD to INR
# 1 USD = 84.13 Indian Rupee 
def converter(usd_val):
    inr_val = usd_val * 84.13
    print(usd_val, "USD =", inr_val, "INR")

converter(1)
converter(5)