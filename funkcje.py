def konwersja_str_int(s):
    for i in range(len(s)):
        s[i] = int(s[i])
    return s


def odczyt_pliku(nazwa_pliku):
    f = open(nazwa_pliku, 'r')
    r = []
    p = []
    q = []
    n = 0
    wszystkie_linie = f.readlines()
    for licznik, linia in enumerate(wszystkie_linie):
        if licznik == 0:
            n = linia.rstrip('\n')
        else:
            s = linia.rstrip('\n').split(' ')
            r.append(s[0])
            p.append(s[1])
            q.append(s[2])
    f.close()
    return int(n), konwersja_str_int(r), konwersja_str_int(p), konwersja_str_int(q)


def spr_wynik(nazwa_pliku, rzeczywisty_wynik):
    f = open(nazwa_pliku, 'r')
    poprawny_wynik = konwersja_str_int(f.readlines())[0]
    f.close()
    if poprawny_wynik == rzeczywisty_wynik:
        return True
    else:
        return False


class WITI():
    def __init__(self, n, p, w, d):
        self.n = n    # ilosc zadan
        self.p = p      # lista - czasy wykonywan zadan
        self.w = w      # lista - wspolczynniki kar
        self.d = d      # lista - żądany termin zakończenia zadan
        self.memory = [0] * (2 ** self.n)


    def PD(self):
        for D in range(0, 2 ** self.n):
            binary_D = bin(D)
            _sum = 0

            for j, val in enumerate(binary_D[:1:-1]):
                if val == '1':
                    _sum += self.p[j]

            temp_list = []

            for j, val in enumerate(binary_D[:1:-1]):
                if val == '1':
                    m = max(_sum - self.d[j], 0) * self.w[j] + self.memory[return_val_without_j(D, j)]
                    temp_list.append(m)

            if type(temp_list) == list and len(temp_list) != 0:
                self.memory[D] = min(temp_list)

        return self.memory

def return_val_without_j(D, j):
    binary_D = list(bin(D))
    binary_D[-j - 1] = 0
    s = ''

    for b in binary_D:
        s += str(b)
    return int(''.join(s), 2)
