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

# price["chuối"] = 200
# price["dâu"] = 900


price.update({"chuối": 200, "dâu": 900})

print(f"\nThông tin sau khi đổi:\n{price}")
