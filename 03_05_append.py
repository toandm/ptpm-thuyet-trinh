print("\n")
l = ["Anh", "Bình", "Cường", "Dũng", "Hoa"]

print(f"Danh sách trước khi thêm:\n{l}")

l.append("Yến")
print(f"\nAppend:\n{l}")

l.extend(["Mai", "Lan"])
print(f"\nExtend:\n{l}")

l.insert(0, "Anh")
print(f"\nInsert:\n{l}")
