import matplotlib.pyplot as plt

filename = 'E:\python\demo1.txt'
Y,X1,X2 = [],[],[]
with open(filename,'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        Y.append(value[0])
        X1.append(value[1])
        X2.append(value[2])
l1, = plt.plot(Y,X1)
l2, = plt.plot(Y,X2)
plt.legend([l1,l2],['training accuracy','testing accuracy'])

plt.xlabel('step')
plt.ylabel('accuracy')
plt.title('task 1')
plt.show()