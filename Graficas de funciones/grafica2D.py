import numpy as np #libreria numérica de python
import matplotlib.pyplot as plt #libreria de gráficos

#Definimos la función a graficar
def f(x):
    return a*x**2+b*x+c

#definimos los límites de la ventana y el dominio del gráfico
# Valores de los coeficientes y=ax^2+bx+c
a=-1
b=4
c=0
#dominio [x0,xf]
vx=-b/(2*a)
k=3 # radio del intervalo
x0=vx-k
xf=vx+k
X=np.linspace(x0,xf,500)
Y=f(X)
plt.plot(X,Y,'#EAD51B',linewidth=1.5,label='$f(x)=ax^2+bx+c$')
plt.scatter(vx,f(vx),color='#EA631B',linewidths=2.0,label='Vértice') #marcamos el vértice de la parábola
plt.text(vx, f(vx)+0.2, '$V$', color="red",fontsize=12, ha='center', va='bottom') #etiqueta del vértice
plt.axhline(0, color='black', linewidth=1) #eje x
plt.text(5, -0.1, '$x$', fontsize=10, ha='left', va='top') #etiqueta del eje x
plt.axvline(0, color='black', linewidth=1) #eje y
plt.text(0, 5, '$y$', fontsize=10, ha='center', va='bottom') #etiqueta del eje x
plt.grid() #mallado
#plt.xticks(np.arange(-1,5,0.5)) #control mallado horizontal
#plt.yticks(np.arange(-6,5,1)) #control mallado vertical
#plt.xlabel('$x$')
#plt.ylabel('$y$')
plt.legend()
plt.xlim([-1,5])
plt.ylim([-6,5])
#plt.savefig('parabola.pdf',bbox_inches='tight',pad_inches=0) #para guardar la grafica
plt.show()