#https://github.com/s-getmanov/st_python7.git

s = input("Введите строку: ")

#Пока в строке есть последовательности из двух пробелов, заменим такие последовательности на один пробел
while "  " in s:
    s = s.replace("  ", " ")
    
print(s)
