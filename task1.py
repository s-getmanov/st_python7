#https://github.com/s-getmanov/st_python7.git

s = input("Введите строку: ")

if s[len(s)::-1] == s:
    print("Yes!")
else:
    print("No.")