def cariMean(num):
    n       = len(num)
    jumlah  = sum(num)
    mean    = jumlah / n
    return mean

data_thn_2017 = [31250,25000,17050,17050,16000,14050,11150,9500,4750,4550]

print(cariMean(data_thn_2017))

#output = 15035.0
