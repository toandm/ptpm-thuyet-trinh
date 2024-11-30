print("\n")
l = ["Anh", "Bình", "Cường", "Dũng", "Hoa"]

ten_viet_hoa_1 = []
for ten in l:
    if ten != "Bình":
        ten_viet_hoa_1.append(ten.upper())

print(f"Cách 1: {ten_viet_hoa_1}")

# List Comprehension
ten_viet_hoa_2 = [ten.upper() for ten in l if ten != "Bình"]

print(f"Cách 2: {ten_viet_hoa_2}")