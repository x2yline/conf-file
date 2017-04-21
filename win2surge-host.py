f = open('F:\\host\\host-win','r')

lines = f.readlines()

f.close()

f = open('F:\\host\\host-surge','w')

#print(len(lines))
all_host_sit = []
for i in lines:
    if i[0] == '1' or i[0] == '2' or i[0] == '3'or i[0] == '4'or i[0] == '5'or i[0] == '6'or i[0] == '7'or i[0] == '8'or i[0] == '9':
        all = i.split()
        all_host_sit.append(all[1].strip().lower())
        j = all[1] + ' = ' + all[0] + '\n'
        f.write(j)
    else:
        f.write(i)

f.close()

f2 = open('F:\\host\\surge_merg','w', encoding='utf-8')




with open('F:\\host\\surge-2.conf', 'r', encoding='utf-8') as all_f:
    for i in all_f:
        if len(i.split(',')) == 3:
            if i.split(',')[1].strip().lower() in all_host_sit and i.split(',')[-1].strip().lower() != 'REJECT':
                i = ','.join(i.split(',')[:-1])+','+'DIRECT\n'
        f2.write(i)
f2.close()
