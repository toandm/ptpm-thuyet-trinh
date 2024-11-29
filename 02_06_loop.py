d1 = {
    "chuoi": "vang",
    "nho": "tim",
    "dau": "do",
}

d2 = {
    "chuoi": 100,
    "nho": 500,
    "dau": 600,
}

print("\n\nKet qua: \n\n")

print("\nDanh sach ten hoa qua:")
for i in d1.keys():
    print(i)


print("\nDanh sach mau hoa qua:")
for i in d1.values():
    print(i)


print("\nDanh sach hoa qua va mau tuong ung:")
for k, v in d1.items():
    print(f"Qua {k} co mau {v}")
