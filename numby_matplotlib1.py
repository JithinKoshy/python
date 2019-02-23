import matplotlib.pyplot as plt
labels="abc","def","ghi"
sizes=[15,30,45,10]
explode(0,0.1,0,0)
fig1,ax1=plt.subplots()
ax1.pie(sizes,expode=explode,labes=labels,shadow=true,startange=90)
ax1.axis("equal")
plt.show()

