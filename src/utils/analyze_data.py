import os
def cout_lines(file_path):
    
    file = open(file_path, "r", encoding="utf-8")
    header=file.readline()
    print(header)   
    a = 0
    for line in file:
        a += 1
    print("no of rows found are :", a)
    file.close()

file_path = os.path.join("data","raw","plastic_waste.csv")
cout_lines(file_path)