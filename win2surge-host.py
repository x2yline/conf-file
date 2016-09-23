f = open('F:\\host\\host-win','r')

lines = f.readlines()

f.close()

f = open('F:\\host\\host-surge','w')

#print(len(lines))

for i in lines:
	if i[0] == '1' or i[0] == '2' or i[0] == '3'or i[0] == '4'or i[0] == '5'or i[0] == '6'or i[0] == '7'or i[0] == '8'or i[0] == '9':
		all = i.split()
		j = all[1] + ' = ' + all[0] + '\n'
		f.write(j)
	else:
		f.write(i)

f.close()

