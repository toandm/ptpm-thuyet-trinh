print("\n")
l = ["Hoa", "Anh", "Dung", "Cuong", "Binh"]

print("\n\nKet qua: \n\n")
print(f"Danh sach truoc khi xep: {l}")

l.sort()

print(f"Danh sach sau khi xep: {l}")

l.sort(reverse=True)
print(f"Danh sach xep nguoc: {l}")

l.sort(key=len)
print(f"Danh sach xep theo do dai ten tang dan: {l}")
