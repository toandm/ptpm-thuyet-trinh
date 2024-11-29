# Int
a = 1
b = a

print("\n\nKet qua: \n\n")

print(f"a truoc khi doi: {a}")
print(f"b truoc khi doi: {b}")

a = 2

print(f"a sau khi doi: {a}")
print(f"b sau khi doi: {b}")

# Dictionary

d1 = {
    "chuoi": "vang",
    "nho": "tim",
    "dau": "do",
}

d2 = d1
d3 = d1.copy()

print("\n\nKet qua: \n\n")

print(f"d1 truoc khi doi: {d1}")
print(f"d2 truoc khi doi: {d2}")
print(f"d3 truoc khi doi: {d3}")

d1["chuoi"] = "den"

print(f"d1 sau khi doi: {d1}")
print(f"d2 sau khi doi: {d2}")
print(f"d3 sau khi doi: {d3}")
