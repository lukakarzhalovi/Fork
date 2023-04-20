input = str(input("შეიყვანეთ მასის ერთეული T or KG: " ))
amount = float(input("Amount: "))
if input == "T":
    print(f"{amount * 1000}: KG")
elif input == "KG":
    print(f"{amount / 1000}: T")
