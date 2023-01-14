
a = int(input("Podaj liczbe: "))
while a:
    b=a
    a = int(input("Podaj liczbe: "))
    if abs(a-b) < 5:
        break

