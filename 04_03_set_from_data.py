print("\n")
input = [
    {"timestamp": "08:00:00", "name": "Anh"},
    {"timestamp": "08:30:00", "name": "Anh"},
    {"timestamp": "08:40:00", "name": "Binh"},
    {"timestamp": "09:00:00", "name": "Cuong"},
    {"timestamp": "09:50:00", "name": "Binh"},
]

print("\n\nKet qua: \n\n")

# Cach 1
ds_diem_danh_1 = []
for i in input:
    name = i["name"]
    if name not in ds_diem_danh_1:
        ds_diem_danh_1.append(name)

print(f"Danh sach nhan vien tao theo cach 1: {ds_diem_danh_1}")

# Cach 2
ds_diem_danh_2 = set()
for i in input:
    ds_diem_danh_2.add(i["name"])

print(f"Danh sach nhan vien tao theo cach 2: {ds_diem_danh_2}")

# Cach 3
ds_diem_danh_3 = {i["name"] for i in input}

print(f"Danh sach nhan vien tao theo cach 3: {ds_diem_danh_3}")
