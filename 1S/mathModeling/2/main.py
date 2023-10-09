import matplotlib.pyplot as plt 

x = [i * 0.01 for i in range(101)]
y = [i if i < 0.5 else 1 - i for i in x]
plt.plot(x, y)
plt.minorticks_on()
plt.grid(which="both")
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.xlabel("density", fontsize = 14)
plt.ylabel("traffic volume", fontsize = 14)
plt.savefig("g.png")
plt.clf()
