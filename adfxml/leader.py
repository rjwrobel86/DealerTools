import datetime

dt = datetime.datetime.now()

month = (dt.strftime("%m"))
day = (dt.strftime("%d"))
year = (dt.strftime("%Y"))
hour = (dt.strftime("%H"))
minute = (dt.strftime("%M"))
second = (dt.strftime("%s"))[:2]
time = (year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second)

lead_name = "Bob Smith"
lead_num = "13145555555"
lead_make = "Chevrolet"
lead_model = "Silverado 1500"
lead_year = "2022"
lead_dealer = "Friendly Autos"

f1 = open('adf-xml-template.txt','r')
f2 = open('adf-xml-lead.xml', 'w')

checkWords = ("MAKE", "MODEL", "YEAR", "FULLNAME", "PHONE", "DEALER", "DATETIME")
repWords = (lead_make, lead_model, lead_year, lead_name, lead_num, lead_dealer, time)

for line in f1:
    for check, rep in zip(checkWords, repWords):
        line = line.replace(check, rep)
    f2.write(line)
f1.close()
f2.close()