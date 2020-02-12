import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
siny=np.sin(x)
cosy=np.cos(x)
plt.plot(x,siny,linestyle='--',label="sin(x)")  # '-.',':','--','-'
plt.plot(x,cosy,color='red',label="cos(x)")
plt.xlim(-5,15 )
plt.ylim(-2,2)  # 等同于 plt.axis([-5,15,-2,2])
plt.xlabel('x axis')
plt.ylabel('y value')
plt.title("Welcome to Matplotlib")
plt.legend()
plt.show()
x=np.random.normal(0,1,100000)
y=np.random.normal(0,1,100000)
plt.scatter(x,y,alpha=0.25)   #alpha表示不透明度
plt.show()