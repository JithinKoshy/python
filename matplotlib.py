import matplotlib.pyplot as plt
xlist=[1,2,3,4,5]
ylist=list(map(lambda x:x*x,xlist))
plt.title("x raised to 2")
plt.xlabel("x values")
plt.ylabel("y=x raised to 2")
plt.plot(xlist,ylist)
plot.show()
