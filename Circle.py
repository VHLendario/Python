import math 
import matplotlib.pyplot as plt

class Circle:
    def __init__ (self, x = float, y = float, raio = float):
        if x < 0 or y < 0 or raio <= 0:
            print ("Erro, valor negativo.")
    
        self.x = x 
        self.y = y
        self.raio = raio 
        
    def Area (self) -> float:
        return math.pi * (self.raio ** 2)
    
    def Diametro (self) -> float:
        return 2 * self.raio
        
    def Comprimento (self) -> float:
        return math.pi*2*self.raio
    
    def Change_Position (self, new_x = float, new_y = float):
        if new_x < 0 or new_y < 0:
            print ("Erro, valor negativo.")
            return
        
        self.x = new_x
        self.y = new_y
    
    def __repr__(self) -> str:
        return (f"Círculo[centro=({self.x}, {self.y}), raio={self.raio}]")

    def plotar(self):

        fig, ax = plt.subplots()

        circulo_plot = plt.Circle((self.x, self.y), self.raio, color='blue', fill=False, linestyle='dashed', linewidth=2)
        ax.add_artist(circulo_plot)
        

        ax.set_xlim(0, max(self.x + self.raio, 10))
        ax.set_ylim(0, max(self.y + self.raio, 10))
        ax.set_aspect('equal', 'box')
        

        ax.plot(self.x, self.y, 'ro')  
        ax.text(self.x + 0.2, self.y, f'({self.x}, {self.y})', fontsize=12)
        
        plt.title('Plano Cartesiano - Círculo')
        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.grid(True)
        plt.show()
        
if __name__ == "__main__":
    circulo = Circle (x = 2, y = 9, raio = 4)
    print (circulo)

    circulo.plotar ()
    
    print (f"Área: {circulo.Area(): .2f}")
    print (f"Diametro: {circulo.Diametro(): .2f}")
    print (f"Comprimento: {circulo.Comprimento(): .2f}")

    circulo.Change_Position(new_x = 10, new_y = 15)
    print (f"Nova posição: {circulo}")

    circulo.plotar()