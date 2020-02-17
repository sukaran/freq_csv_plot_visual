
import random
import string
import pandas as pd
import numpy as np
import csv
import sys

print(sys.argv[1],sys.argv[2],sys.argv[3])
def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

charss = ['C','D','N','B','A','S','G']# + string.punctuation
#charss = chars.upper()
size = int(sys.argv[1])
#size = 12
#print(chars)
x=[]
with open('employee_file.csv', mode='w',newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['count','String','number of C','sigma'])
    for i in range(int(sys.argv[2])):
        stra = random_string_generator(size, charss)
        x.append(stra.count(sys.argv[3]))
        xp = stra.count(sys.argv[3])
        #print(stra,xp,sigma)
        if xp > 1:
            sigma = '+'
        else:
            sigma = '-'
        s = ''.join(stra)
        print(s)
        employee_writer.writerow([i,stra,xp,sigma])

        #print(stra,xp,sigma)
        #d= dict(zip(stra,x))
        #dd  = dict(zip(d,sigma))

        #d

import matplotlib.pyplot as plt


res = csv.reader(open('employee_file.csv'), delimiter=',')
next(res) # do not read header

mut = []
tot = [] 
a = 0
width = 0.2

for col in res:
    mut.append(col[0])
    tot.append(int(col[2]))
    a += 1

ind = np.arange(a)

p1 = plt.bar(ind,tot,width,color='r')
labs = plt.xticks(ind+width,mut)

plt.show()
  