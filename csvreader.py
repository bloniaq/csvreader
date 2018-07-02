import csv

# setting path

main_path = 'E:/# PRACA/Geometric/CybLokale'

# variables

result_dict = {}

for i in range(130):
    file_path = main_path + '/Tabelki/' + str(i) + '.csv'
    temp_list = []
    with open(file_path, 'r', newline='\n') as file:
        reader = csv.DictReader(file, delimiter=';')
        for j in reader:
            temp_list.append(j)
    result_dict[str(i)] = temp_list

for i in result_dict:
    with open(main_path, 'w', newline='\n') as result_file:
        writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
