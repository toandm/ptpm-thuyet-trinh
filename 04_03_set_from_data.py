print("\n")
input = [
    {"timestamp": "08:00:00", "name": "Anh"},
    {"timestamp": "08:30:00", "name": "Anh"},
    {"timestamp": "08:40:00", "name": "Bình"},
    {"timestamp": "09:00:00", "name": "Cường"},
    {"timestamp": "09:50:00", "name": "Bình"},
]

# Cach 1
checkin_1 = []
for i in input:
    name = i["name"]
    if name not in checkin_1:
        checkin_1.append(name)
print(f"\nCách 1:\n{checkin_1}")

# Cach 2
checkin_2 = set()
for i in input:
    checkin_2.add(i["name"])
print(f"\nCách 2:\n{checkin_2}")

# Cach 3
checkin_3 = {i["name"] for i in input}
print(f"\nCách 3:\n{checkin_3}")
