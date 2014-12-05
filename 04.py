coldest_date = None
lowest_temp = 10.0

with open('klimadata.txt') as f:
    for line in f.readlines()[24:23402]:
        line = line.split()
        temp = float(line[3].replace(',', '.'))
        if temp < lowest_temp and line[1][3:5] == '12':
            lowest_temp = temp
            coldest_date = line[1]

print coldest_date, lowest_temp