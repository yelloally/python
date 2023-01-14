b = int(input('Podaj liczbę: '))

S = 0.0

K = 0
while b != 0:
    S += b
    K += 1
    b = int(input('Podaj liczbę: '))

if K != 0:
    s_a = S / K
else:
    s_a = 0

print((s_a))