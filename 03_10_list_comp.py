print("\n")
l = ["Anh", "Binh", "Cuong", "Dung", "Hoa"]

print("\n\nKet qua: \n\n")

ten_viet_hoa_1 = []
for ten in l:
    if ten != "Binh":
        ten_viet_hoa_1.append(ten.upper())

print(f"Danh sach hoc sinh khong co Binh, cach 1: {ten_viet_hoa_1}")

# List Comprehension
ten_viet_hoa_2 = [ten.upper() for ten in l if ten != "Binh"]

print(f"Danh sach hoc sinh khong co Binh, cach 2: {ten_viet_hoa_2}")
