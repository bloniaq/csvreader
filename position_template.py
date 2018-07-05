import csv

main_path = 'E:/# PRACA/Geometric/Lokale Cyb/'

with open(main_path + 'Template.csv', 'w', newline='\n') as result_file:
    write = csv.writer(result_file, delimiter=';')
    write.writerow([])
    for i in range(146):
        sentence = '=\'Input CSV\'!A' + str(i+2)
        expression = [sentence]
        difference_sent = '=A'+str(3*i+2)+'-A'+str(3*i+3)
        difference_expr = [difference_sent]
        write.writerow(expression)
        write.writerow([])
        write.writerow(difference_expr)