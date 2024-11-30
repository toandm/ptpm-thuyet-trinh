print("\n")

email = "xinchao@hus.edu.vn"
mypassword = "Python5@"

valid_domain = "@hus.edu.vn"

if valid_domain in email:
    print(f"Email hợp lệ.")
else:
    print(f"Email chưa hợp lệ. Cần có domain {valid_domain}")
