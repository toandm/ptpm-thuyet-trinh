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

print(f'\nMàu sắc của chuối:\n{color["chuối"]}')
print(f'\nGiá bán của chuối:\n{price.get("chuối")}')

# Truy cập key không tồn tại
print(f'\nGiá bán của xoài:\n{price.get("xoài", "Không có")}')

print(f'\nGiá bán của xoài:\n{price["xoài"]}')
