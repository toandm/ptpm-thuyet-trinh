print("\n")

price = {
    "chuối": 100,
    "nho"  : 500,
    "dâu"  : 600,
}

print(f"\nThông tin trước khi đổi:\n{price}")

price.pop("dâu")

print(f"\nThông tin sau khi đổi:\n{price}")
