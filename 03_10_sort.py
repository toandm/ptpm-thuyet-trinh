print("\n")
l = ["Hoa", "Anh", "Dũng", "Cường", "Bình"]

print(f"Danh sách trước khi xếp: {l}")

l.sort()
print(f"\nDanh sách sau khi xếp:\n{l}")

l.sort(reverse=True)
print(f"\nDanh sách xếp ngược:\n{l}")

l.sort(key=len)
print(f"\nDanh sach xếp theo độ dài tên tăng dần:\n{l}")
