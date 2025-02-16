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

print(f"\nThông tin màu sắc:\n{color}")
print(f"\nThông tin giá bán:\n{price}")

# Check giá trị trùng lặp
color_2 = {
    "chuối": "vàng",
    "nho"  : "tím",
    "dâu"  : "đỏ",
    "dâu"  : "đen",
}

print(f"\nGiá trị của color_2 là:\n{color_2}")
