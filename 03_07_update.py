print("\n")
l = ["Anh", "Bình", "Cường", "Dũng", "Hoa"]
#      0       1       2        3      4
#     -5      -4      -3       -2     -1

print(f"Danh sách trước khi sửa:\n{l}")

l[0] = "An"
print(f"\nDanh sách sau khi sửa:\n{l}")

l[-3:] = ["Quân", "Tiến", "Vương"]
print(f"\nDanh sách sau khi sửa:\n{l}")
