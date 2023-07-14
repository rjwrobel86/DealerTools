jswr = "www.URL1.com"
jsof = "www.URL2.com"
sshi = "www.URL3.com"

srpurl = "VehicleSearchResults?search=new&model="

eq = "Equinox"
cr = "Cruze"
co = "Colorado"
ma = "Malibu"
tr = "Traverse"

fwdls = "&trim=FWD%20LS"
fwdlt = "&trim=FWD%20LT"
fwdpr = "&trim=FWD%20Premier"

dealers = [jswr, jsof, sshi]
models = [eq, cr, ma, tr]
trims = [fwdls, fwdlt, fwdpr]

list1 = []

for i in dealers:
  for j in models:
    for k in trims:
      print(i + srpurl + j + k)
      list1.append(i + srpurl + j + k)

outFile = open('urls.txt', 'w')
outFile.write("\n".join(list1))
outFile.close()