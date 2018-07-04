import csv

# setting path

main_path = 'E:/# PRACA/Geometric/Lokale Cyb/Lokale'

# variables

result_dict = {}

def nofile():
    print(str(i)+'.csv', 'nie istnieje')

# def bricscadfile(filepath):
#     with open(file_path, 'r', newline='\n') as file:
#             reader = csv.reader(file, delimiter=';')
#             for j in reader:
#                 print(j)
#                 temp_list.append(eval(j[0]))
#             print(temp_list)

def autocadfile(filepath):
    with open(filepath, 'r', newline='\n') as file:
        reader = csv.reader(file, delimiter=';')
        csvFileArray = []
        for row in reader:
            csvFileArray.append(row)
        print(csvFileArray[16][0])
        place_area = csvFileArray[16][0]
        file.seek(0)
        # place_data = {}
        room_area = []
        balcony_area = []
        for j in reader:
            print(j)
            if j[0] != ' ':
                room_area.append(eval(j[0]))
            else:
                break
        print(next(reader))
        for h in csvFileArray:
            print(h)
        place_data['room_area'] = room_area
        place_data['place_area'] = place_area
        place_data['balcony_area'] = balcony_area
        return place_data


for i in range(1, 130):
    file_path = main_path + '/Tabelki/' + str(i) + '.csv'
    try:
        with open(file_path, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            sample = next(reader)[0]
            if sample[:3] == '\\C7':
                print('chuj')
            else:
                place_list = autocadfile(file_path)
                print(place_list)
    except FileNotFoundError:
        nofile()

for i in result_dict:
    with open(main_path + '/zestawienie.csv', 'w', newline='\n') as result_file:
        writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
