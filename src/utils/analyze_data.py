file = open("data/raw/plastic_waste.csv", "r", encoding="utf-8")
a = 0
for line in file:
    a += 1
print("no of rows found are :", a)
file.close()
