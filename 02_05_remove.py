print("\n")

color = {
    "chuối": "vàng",
    "nho"  : "tím",
    "dâu"  : "đỏ",
}

price = {
    "chuối": 100,
    "nho"  : 500,
    "dâu"  : 600,
}

print(f"\nThông tin trước khi đổi:\n{price}")

color.pop("dau")

print(f"\nThông tin sau khi đổi:\n{price}")
