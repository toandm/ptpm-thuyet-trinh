d1 = {
    "chuoi": "vang",
    "nho": "tim",
    "dau": "do",
}

d2 = {
    "chuoi": 100,
    "nho": 500,
    "dau": 600,
}

print("\n\nKet qua: \n\n")

print(f"Thong tin gia ban truoc khi doi: {d2}")

# d2["chuoi"] = 200
# d2["dau"] = 900

d2.update({"chuoi": 200, "dau": 900})

print(f"Thong tin gia ban sau khi doi: {d2}")
