ni0 = 0
ni = 28
nj0 = 0
nj = 40
ff = open('04050607/square.txt','w')
for j in range(nj0,nj+1):
    for i in range(ni0,ni+1):
        c = 'x{:03}y{:03}.txt'.format(i,j)
        f = open('04/'+c)
        data4 = f.readlines()
        f.close()
        f = open('05/'+c)
        data5 = f.readlines()
        f.close()
        f = open('06/'+c)
        data6 = f.readlines()
        f.close()
        f = open('07/'+c)
        data7 = f.readlines()
        f.close()
        f = open('04050607/'+c,'w')
        ii = 0
        xx = 0.0
        for line4, line5, line6, line7 in zip(data4, data5, data6, data7):
            l4 = [float(x.strip()) for x in line4.split(',')]
            l5 = [float(x.strip()) for x in line5.split(',')]
            l6 = [float(x.strip()) for x in line6.split(',')]
            l7 = [float(x.strip()) for x in line7.split(',')]
            f.write(str(l4[0])+', '+str(l4[1]+l5[1]+l6[1]+l7[1])+'\n')
            if (ii > len(data4)*0.2 and ii < len(data4)*0.8):
                x = l4[1]+l5[1]+l6[1]+l7[1]
                xx+= (x*x)
            ii+=1
        f.close()
        ff.write(str(i)+', '+str(j)+', '+str(xx/ii)+'\n')
    ff.write('\n')
ff.close()
'''
a = 'am05bm15wlt'
b = '03.txt'
f = open(a+b)
data3 = f.readlines()
f.close()
b = '04.txt'
f = open(a+b)
data4 = f.readlines()
f.close()
b = '05.txt'
f = open(a+b)
data5 = f.readlines()
#print(len(data5))
f.close()
#b = '345.txt'
#f = open(a+b,'w')
i = 0
max = 0.0
min = 0.0
xx = 0.0
nn = 0
for line3, line4, line5 in zip(data3, data4, data5):
    l3 = [float(x.strip()) for x in line3.split(',')]
    l4 = [float(x.strip()) for x in line4.split(',')]
    l5 = [float(x.strip()) for x in line5.split(',')]
    #print(str(l3[0])+', '+str(l3[1]+l4[1]+l5[1]))
    #f.write(str(l3[0])+', '+str(l3[1]+l4[1]+l5[1])+'\n')
    if (i > len(data3)*0.2 and i < len(data3)*0.8):
        x = l3[1]+l4[1]+l5[1]
        if (max < x):
            max = x
        if (min > x):
            min = x
        nn+=1
        xx+= (x*x)
    i+=1
#f.close()
#print('max = '+ str(max))
#print('min = '+ str(min))
print(max-min)
print(xx/nn)
'''
