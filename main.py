import funkcje as fu
import time

for i in range(1, 10):
    start = time.time()
    il_zadan, czas_wykonania_zadania, wspol_kary, termin_zakonczenia = fu.odczyt_pliku(f'input/WITI{i}.DAT')
    witi = fu.WITI(il_zadan, czas_wykonania_zadania, wspol_kary, termin_zakonczenia)
    witi_result = witi.PD()
    result = witi_result.pop()
    stop = time.time()

    if fu.spr_wynik(f'output/WITI{i}.dat', result) is True:
        print(f'WITI{i} ->', result, '\u2713', stop - start, 's')
    else:
         print(f'WITI{i} ->', result, '\u2717')