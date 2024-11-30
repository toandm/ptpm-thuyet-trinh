print("\n")
l = ["Hoa", "Anh", "Dung", "Cuong", "Binh"]

print("\n\nKet qua: \n\n")
print(f"Danh sách trước khi xếp: {l}")

l.sort()

print(f"Danh sách sau khi xếp: {l}")

l.sort(reverse=True)
print(f"Danh sách xếp ngược: {l}")

l.sort(key=len)
print(f"Danh sach xếp theo độ dài tên tăng dần: {l}")
