import matplotlib.pyplot as plt
import math

def f(x) : 
    return x * (1 - x) * (13811 / 73554 + 2380 / 12259 * x - 7 / 299 * x * x)
    
def g(x) : 
    return math.sin(x) / math.sin(1) - x
    
def h(x) : 
    return x * (1 - x) * (71 + 63 * x) / 369

arr1 = []
arr2 = []
k = []
for x in range(0, 1001) : 
    if x == 0 or x == 1000 : 
        arr1.append(0)
        arr2.append(0)
    else : 
        t = x / 1000
        arr1.append(abs(1.0 - f(t) / g(t)))
        arr2.append(abs(1.0 - h(t) / g(t)))
    k.append(x * 0.001)

plt.plot(k, arr2, label = "second-order approximation")
plt.plot(k, arr1, label = "third-order approximation")
plt.grid()
plt.xlabel("x", fontsize = 14)
plt.ylabel("error ratio", fontsize = 14)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.legend(fontsize = 12) 
plt.savefig("g.png")