pens = int(input())
markers = int(input())
liters_chemicals = int(input())
percent_discount =  int(input())

pens_pack =  pens * 5.80
markers_pack = markers * 7.20
cleaner = liters_chemicals * 1.20
precent_discount = 1 - (percent_discount / 100)

total = (pens_pack + markers_pack + cleaner ) * precent_discount

print(total)





