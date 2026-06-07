import os

def cout_lines(file_path):
    file = open(file_path, "r", encoding="utf-8")
    header = file.readline()
    print(header)   
    a = 0
    for line in file:
        a += 1
    print("no of rows found are :", a)
    file.close()

def count_high_waste(file_path):
    file = open(file_path, "r", encoding="utf-8")
    high_waste = 0
    header = file.readline()
    
    for line in file:
        linedata = line.split(",")
        volume = linedata[-1]
        try:
            float_volume = float(volume)
            if float_volume > 50:
                high_waste +=1
        except ValueError:
            continue
    print("number of high waste found are :", high_waste)
    file.close()

file_path = os.path.join("data", "raw", "plastic_waste.csv")
cout_lines(file_path)
count_high_waste(file_path)