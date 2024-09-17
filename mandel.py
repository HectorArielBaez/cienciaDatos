import matplotlib.pyplot as plt
import numpy as np

def sierpinski(ax, x, y, size, n):
    if n == 0:
        return
    
    # Dibujar el triángulo
    points = np.array([[x, y], [x+size, y], [x+size/2, y+size*np.sqrt(3)/2]])
    ax.fill(points[:,0], points[:,1], color='blue')

    # Llamar recursivamente para los subtriángulos
    sierpinski(ax, x, y, size/2, n-1)
    sierpinski(ax, x+size/2, y, size/2, n-1)
    sierpinski(ax, x+size/4, y+size*np.sqrt(3)/4, size/2, n-1)

# Función para actualizar el gráfico en cada iteración
def update(frame):
    plt.clf()
    sierpinski(plt.gca(), 0, 0, 512, frame)
    plt.axis('off')

# Crear la animación
import matplotlib.animation as animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=10, interval=500)
plt.show()
