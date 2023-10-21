d = dict()
lst = list()

fname = input('enter the file name : ')
try:
    fopen = open(fname,'r')
except:
    print('wrong file name !!!')

for line in fopen:

    stline = line.strip()
    
    if stline.startswith('From:'):
        continue
    elif stline.startswith('From'):
        spline = stline.split()
        
        time = spline[5]
        tsplit = time.split(':')
        
        t1 = tsplit[0].split()
        
        for t in t1:
            if t not in d:
                d[t] = 1
            else:
                d[t] = d[t] + 1

for k,v in d.items():
    lst.append((k,v))
lst = sorted(lst)

for k,v in lst:
    print(k,v)