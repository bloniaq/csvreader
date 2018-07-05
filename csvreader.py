import csv

# setting path

# main_path = 'E:/# PRACA/Geometric/Lokale Cyb/Lokale'
main_path = 'C:/WORKZONE/!Private/CsvReader'

# variables

result_dict = {}

def place_area_parser(string):
    place_area = float(string.split(';')[2])
    print(place_area)
    return(place_area)

def room_area_parser(string):
    room_area = float(string.split(';')[1])
    print(room_area)
    return(room_area)

def balcony_area_parser(string):
    parse1 = string.split(';')[1]
    balcony_area = float(parse1.split('}')[0])
    print(balcony_area)
    return(balcony_area)


def nofile():
    place_data = {}
    place_data['room_area'] = []
    place_data['place_area'] = 0.0
    place_data['balcony_area'] = []
    return place_data

def bricscadfile(filepath):
    with open(filepath, 'r', newline='\n') as file:
        reader = csv.reader(file, delimiter=';')
        csvFileArray = []
        for row in reader:
            csvFileArray.append(row)
        place_area = place_area_parser(csvFileArray[16][0])
        place_data = {}
        room_area = []
        balcony_area = []
        file.seek(0)
        for j in reader:
            # print(j)
            if j[0] != ' ':
                room_area.append(room_area_parser(j[0]))
            else:
                break
        # for h in csvFileArray[17:]:
        #     if h[0] != ' ' and h[0] != 'x':
        #         balcony_area.append(float(h[0]))
        #     elif h[0] != ' ':
        #         balcony_area.append(h[0])
        place_data['room_area'] = room_area
        place_data['place_area'] = place_area
        place_data['balcony_area'] = balcony_area
        return place_data

def autocadfile(filepath):
    with open(filepath, 'r', newline='\n') as file:
        reader = csv.reader(file, delimiter=';')
        csvFileArray = []
        for row in reader:
            csvFileArray.append(row)
        place_area = float(csvFileArray[16][0])
        place_data = {}
        room_area = []
        balcony_area = []
        file.seek(0)
        for j in reader:
            # print(j)
            if j[0] != ' ':
                room_area.append(float(j[0]))
            else:
                break
        for h in csvFileArray[17:]:
            if h[0] != ' ' and h[0] != 'x':
                balcony_area.append(float(h[0]))
            elif h[0] != ' ':
                balcony_area.append(h[0])
        place_data['room_area'] = room_area
        place_data['place_area'] = place_area
        place_data['balcony_area'] = balcony_area
        return place_data


for i in range(1, 130):
    # file_path = main_path + '/Tabelki/' + str(i) + '.csv'
    file_path = main_path + '/Examples/' + str(i) + '.csv'
    local_number = str(i)
    try:
        with open(file_path, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            sample = next(reader)[0]
            if sample[:3] == '\\C7':
                result_dict[local_number] = bricscadfile(file_path)
            else:
                result_dict[local_number] = autocadfile(file_path)
    except FileNotFoundError:
        result_dict[local_number] = nofile()

for i in result_dict:
    print(i, result_dict[i])

# for i in result_dict:
#     with open(main_path + '/zestawienie.csv', 'w', newline='\n') as result_file:
#         writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
