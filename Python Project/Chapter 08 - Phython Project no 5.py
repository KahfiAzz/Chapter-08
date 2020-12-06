def Kuadrat(bil):
    hasil = []
    for i in bil:
        hasil = hasil + [i**2]
    return hasil

bil = [2, 4, 5, 6]
print('Bilangan : ', bil)
hasil = Kuadrat(bil)
print('Hasil kuadrat bilangan adalah : ', hasil)
