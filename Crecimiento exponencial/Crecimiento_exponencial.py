import numpy as np #libreria numérica de python
import matplotlib.pyplot as plt #libreria de gráficos

def p(t):
  y=p0*np.exp(k*t)
  return y

#parámetros
p0=2
k=0.12

#tiempo
t0=0 #tiempo inicial
tf=30 #tiempo final

#población en tiempo t
T=np.linspace(t0,tf,500)
P=p(T)
pmax=max(P)
plt.plot(T,P,'#EAD51B',linewidth=1.5)
plt.scatter(0,p0,color='#EA631B',linewidths=1.5, zorder=5) #marcamos condición incial
plt.axhline(0, color='black', linewidth=1) #eje x
plt.text(tf+0.1, -0.1, '$t$', fontsize=10, ha='left', va='top') #etiqueta del eje t
plt.axvline(0, color='black', linewidth=1) #eje y
plt.text(0, pmax, '$P(t)$', color="black",fontsize=10, ha='left', va='top') #etiqueta del eje x
plt.grid() #mallado
#plt.xticks(np.arange(-1,5,0.5)) #control mallado horizontal
#plt.yticks(np.arange(-6,5,1)) #control mallado vertical
plt.xlabel('tiempo (días)')
plt.ylabel('población')
plt.xlim([t0-1,tf])
#plt.savefig('bacterias.pdf',bbox_inches='tight',pad_inches=0) #para guardar la grafica
plt.show()