t = "Python5@"
email = "xinchao@gmail.com"
print("\n\nKet qua: \n\n")

has_upper = False
has_lower = False
has_digit = False
for i in t:
    if i.isupper():
        has_upper = True
    elif i.islower():
        has_lower = True
    elif i.isdigit():
        has_digit = True
if not has_upper:
    print("Mat khau phai co chu cai viet hoa")
elif not has_lower:
    print("Mat khau phai co chu cai viet thuong")
elif not has_digit:
    print("Mat khau phai co it nhat 1 chu so")
else:
    print("Mat khau hop le")
