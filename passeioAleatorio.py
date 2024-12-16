import random
import matplotlib.pyplot as plt

# Caminhada aleatória
position = 0
walk = [position]
nsteps = 1000
for _ in range(nsteps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

# Plotando os 100 primeiros passos
plt.plot(walk[:100])
plt.title("Caminhada Aleatória")
plt.xlabel("Passos")
plt.ylabel("Posição")
plt.show()