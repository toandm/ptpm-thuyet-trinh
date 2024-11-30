print("\n")

price = {
    "chuối": 100,
    "nho"  : 500,
    "dâu"  : 600,
}

print("Danh sách tên hoa quả:")
for k in price.keys():
    print(k)

print("Danh sách giá hoa quả:")
for v in price.values():
    print(v)

print("Danh sách tên và giá hoa quả tương ứng:")
for k, v in price.items():
    print(f"Quả {k} có giá {v}k/kg")
