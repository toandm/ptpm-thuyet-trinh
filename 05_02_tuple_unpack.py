print("\n")

hoc_sinh = ("Bình", 22, "Hà Nội")

ten, tuoi, que_quan = hoc_sinh

print(f"Học sinh {ten}, {tuoi} tuổi, quê ở {que_quan}")

# Bỏ qua 1 biến
ten, _, que_quan = hoc_sinh

# Bỏ qua nhiều biến
ten, *_ = hoc_sinh


print("\n")
# Dict items()
d = {"a": 1}
for i in d.items():
    print(i)
    k, v = i
    

# hs = {"name": "Bình"}
# ten = hs["name"]
# tuoi = hs["tuoi"]
# que_quan = hs["que_quan"]

