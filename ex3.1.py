import matplotlib.pyplot as plt
import json

with open("internetdata.json", "r") as in_file:
    content = json.load(in_file)

countriesabove10k = []
countriesbelow10k = []
usageabove10k = []
usagebelow10k = []

for country in content:
    income = country["incomeperperson"]
    usage = country["internetuserate"]
    if income == None or income < 10000:
        countriesbelow10k.append(country)

        if usage == None:
            usagebelow10k.append(0)
        else:
            usagebelow10k.append(usage)
    else:
        countriesabove10k.append(country)

        if usage == None:
            usageabove10k.append(0)
        else:
            usageabove10k.append(usage)

plt.figure(0)
plt.hist(usagebelow10k)
plt.xlabel("Internet usage")
plt.ylabel("Frequency")
plt.title("Internet usage for countries with per person income less than 10k")
plt.savefig("hist1.png")

plt.figure(1)
plt.hist(usageabove10k)
plt.xlabel("Internet usage")
plt.ylabel("Frequency")
plt.title("Internet usage for countries with per person income at or above 10k")
plt.savefig("hist2.png")
