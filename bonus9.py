password = input("Enter your password: ")

result = []
digit = False

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

for i in password:
    if i.isdigit():
        digit = True
        result.append(True)
        break
for i in password:
    if i.isupper():
        result.append(True)
        break

print(result)
