def DataStat(x):
    jmlh = sum(x)
    bagi = len(x)
    a = jmlh/bagi
    b = max(x)
    c = min(x)
    return(a, b, c)

bil = (7, 4, 5, 6, 7, 1, 12, 5, 9)
print('(Rata-rata, nilai tertinggi, nilai terendah)')
print(DataStat(bil))
