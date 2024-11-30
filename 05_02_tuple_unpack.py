print("\n")

hs = ("Bình", 22, "Hà Nội")

ten, tuoi, que_quan = hs

print(f"Học sinh {ten}, {tuoi} tuổi, quê ở {que_quan}")

# hs = {"name": "Bình"}
# ten = hs["name"]
# tuoi = hs["tuoi"]
# que_quan = hs["que_quan"]


# Bỏ qua 1 biến
ten, _, que_quan = hs

# Bỏ qua nhiều biến
ten, *_ = hs

# Dict items()
d = {"a": 1}
for i in d.items():
    print(i)
