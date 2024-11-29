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

print(f'Mau sac cua chuoi: {d1["chuoi"]}')
print(f'Gia ban cua chuoi: {d2.get("chuoi")}')

# Truy cap key khong ton tai
print(f'Gia ban cua chom chom: {d2.get("chom_chom", "Khong co")}')

print(f'Gia ban cua chom chom: {d2["chom_chom"]}')
