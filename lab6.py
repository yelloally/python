numb = int(input("Podaj liczbę: "))

# zbiór dzielników danej liczby
delitellist = {1}
#jest pierwszym dzielnikiem dowolnej liczby naturalnej
sumlist = 1

i = 2 # następny możliwy dzielnik danej liczby

# obliczaj tak długo, aż kwadrat dzielnika będzie większy od danej liczby
# suma łączna dzielników nie jest większa od danej liczby
while i * i <= numb and sumlist <= numb:
    # czy dana liczba jest podzielna przez "dzielnik" bez reszty
    if (numb % i == 0):
        # następnie dodajemy do skumulowanej sumy dzielników
        # "dzielnik" i iloraz "liczba"/"dzielnik",
        # if they're not equal
        sumlist += i + (numb // i if i != numb // i else 0)
        # dodać "dzielnik" i "iloraz" do zbioru dzielników
        # Jeśli są takie same, zestaw "dostanie" jedną wartość
        delitellist.update({i, numb // i})
    i += 1

if sumlist == numb:
    print(*sorted(delitellist))
else:
    print("Liczba nie doskonala")