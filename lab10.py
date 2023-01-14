a = int(input("Podaj liczbe: "))
sum = a
while a:
    b=a
    a = int(input("Podaj liczbe: "))
    if b==a:
        break
    sum += a
    print("suma jest", sum)
