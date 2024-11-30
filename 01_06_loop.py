print("\n")

email = "xinchao@hus.edu.vn"
mypassword = "Python5@"

has_upper = False

for i in mypassword:
    if i.isupper():
        has_upper = True

if has_upper is False:
    print("Mật khẩu chưa hợp lệ.")
else:
    print("Mật khẩu hợp lệ.")


# islower()
# isdigit()
