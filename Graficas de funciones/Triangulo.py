import matplotlib.pyplot as plt #libreria de gráficos

#vertices del triangulo
ax=-1; ay=0 #punto A
bx=0; by=3 #punto B
cx=5; cy=0 #punto C

#grafico
plt.scatter(ax, ay, color='blue', zorder=5) #punto A
plt.scatter(bx, by, color='blue', zorder=5) #punto B
plt.scatter(cx, cy, color='blue', zorder=5) #punto C
#etiquetas a los vértices
plt.text(ax-0.1, ay, '$A$', color="red",fontsize=12, ha='right', va='top',fontweight='bold') #A
plt.text(bx, by, '$B$', color="red",fontsize=12, ha='right', va='bottom',fontweight='bold') #B
plt.text(cx+0.1, cy, '$C$', color="red",fontsize=12, ha='left', va='top',fontweight='bold') #C
#lineas que unen los vertices
plt.plot([ax,bx],[ay,by],'b')#linea que une A y B
plt.plot([ax,cx],[ay,cy],'b')#linea que une A y C
plt.plot([bx,cx],[by,cy],'b')#linea que une B y C

plt.show()