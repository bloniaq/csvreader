import csv

# setting path

main_path = 'E:/# PRACA/Geometric/Lokale Cyb/'
# main_path = 'C:/WORKZONE/!Private/CsvReader'

# variables

result_dict = {}

def place_area_parser(string):
    place_area = string.split(';')[2]
    return(place_area.replace('.', ','))

def room_area_parser(string):
    room_area = string.split(';')[1]
    return(room_area.replace('.', ','))

def balcony_area_parser(string):
    parse1 = string.split(';')[1]
    balcony_area = parse1.split('}')[0]
    return(balcony_area.replace('.', ','))


def nofile():
    place_data = {}
    place_data['room_area'] = []
    place_data['place_area'] = '0,0'
    place_data['balcony_area'] = []
    return place_data

def bricscadfile(filepath):
    print('bricscad')
    print('\n\n')
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
        for h in csvFileArray[17:]:
            print
            # if h[0] != ' ' and h[0] != '{\\C7;x}':
            if h[0] != ' ':
                balcony_area.append(balcony_area_parser(h[0]))
                print(balcony_area)
        #     elif h[0] != ' ':
        #         balcony_area.append(h[0])
        place_data['room_area'] = room_area
        place_data['place_area'] = place_area
        place_data['balcony_area'] = balcony_area
        print('\n\n')
        return place_data

def autocadfile(filepath):
    print('acad')
    with open(filepath, 'r', newline='\n') as file:
        reader = csv.reader(file, delimiter=';')
        csvFileArray = []
        for row in reader:
            csvFileArray.append(row)
        place_area = csvFileArray[16][0].replace('.', ',')
        place_data = {}
        room_area = []
        balcony_area = []
        file.seek(0)
        for j in reader:
            # print(j)
            if j[0] != ' ':
                room_area.append(j[0].replace('.', ','))
            else:
                break
        for h in csvFileArray[17:]:
            if h[0] != ' ':
                balcony_area.append(h[0].replace('.', ','))
        place_data['room_area'] = room_area
        place_data['place_area'] = place_area
        place_data['balcony_area'] = balcony_area
        return place_data


for i in range(1, 146):
    file_path = main_path + 'Lokale/Tabelki/' + str(i) + '.csv'
    # file_path = main_path + '/Examples/' + str(i) + '.csv'
    local_number = str(i)
    print(local_number)
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

with open(main_path + 'Plik_zbiorczy.csv', 'w', newline='\n') as result_file:
    writer = csv.writer(result_file, delimiter=';')
    for i in result_dict:
        expression = []
        print(i, result_dict[i])
        expression.append(i)
        expression.append(result_dict[i]['place_area'])
        room_counter = 0
        for j in result_dict[i]['room_area']:
            expression.append(j)
            room_counter += 1
        for k in range(room_counter, 10):
            expression.append(' ')
        for l in result_dict[i]['balcony_area']:
            expression.append(l)
        print(expression)
        writer.writerow(expression)
