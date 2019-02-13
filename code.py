import numpy as np
import matplotlib.pyplot as plt 

O = np.array([0,0])
t = np.linspace(-15,15,1000)
X1 = np.array([t,(t**2)/8.0])
Q1 = np.array([8,8])
P1 = (1*Q1 + 3*O)/4.0
k = np.linspace(0,1,10)
x = np.linspace(-50,50,1000)
y = np.zeros((2,1000))
A = np.linspace(-50,50,1000)
x_OQ = np.zeros((2,10))
for i in range(0,10):
	temp = O+k[i]*(Q1-O)
	x_OQ[:,i]=temp
for i in range(0,1000):
	Q = np.array([A[i],(A[i]**2)/8.0])
	y[0][i] = (1*Q[0]+3*O[0])/4.0
	y[1][i] = (1*Q[1]+3*O[1])/4.0

plt.title('Locus of P')
plt.plot(P1[0], P1[1], 'o')
plt.plot(Q1[0], Q1[1], 'o')
plt.text(P1[0]*1.2,P1[1],'P1')
plt.text(Q1[0]*1.2,Q1[1],'Q1')
plt.plot(x_OQ[0,:],x_OQ[1,:])
plt.plot(y[0],y[1],label = 'x^2-2y=0')
plt.plot(X1[0],X1[1],label='x^2-8y=0')
plt.grid()
plt.legend(loc='best')
plt.show()
