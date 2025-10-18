[CLASESTAREA.PY](https://github.com/user-attachments/files/22981690/CLASESTAREA.PY)

# "1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área 
# # del" rectángulo""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura



rect = Rectangulo(5, 3)
print("El área del rectángulo es:", rect.area())


# "2)Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener 
# como miembros....
# "

# class Mate:
#     def __init__(self, n):
#         self.n = n                        
#         self.cebadas_restantes = n        
#         self.lleno = False                

#     def cebar(self):
#         if self.lleno:
#             raise Exception("¡Cuidado! ¡Te quemaste!")
#         else:
#             self.lleno = True
#             print("Mate cebado.")

#     def beber(self):
#         if not self.lleno:
#             raise Exception("¡El mate está vacío!")
#         else:
#             self.lleno = False
#             if self.cebadas_restantes > 0:
#                 self.cebadas_restantes -= 1
#                 if self.cebadas_restantes == 0:
#                     print("Advertencia: el mate está lavado.")
#             else:
#                 print("Advertencia: el mate está lavado.")
#             print("Glup! Qué rico mate.")


# try:
#     mi_mate = Mate(3)
#     mi_mate.cebar()
#     mi_mate.beber()
#     mi_mate.cebar()
#     mi_mate.beber()
#     mi_mate.cebar()
#     mi_mate.beber()
#     mi_mate.cebar()
#     mi_mate.beber()  
# except Exception as e:
#     print(e)

# # "3) Botella y Sacacorchos "

# class Corcho:
#     def __init__(self, bodega):
#         self.bodega = bodega  

#     def __str__(self):
#         return f"Corcho de la bodega '{self.bodega}'"



# class Botella:
#     def __init__(self, corcho=None):
#         self.corcho = corcho  

#     def esta_tapada(self):
#         return self.corcho is not None

# class Sacacorchos:
#     def __init__(self):
#         self.corcho = None  

#     def destapar(self, botella):
#         if self.corcho is not None:
#             raise Exception("El sacacorchos ya tiene un corcho, primero hay que limpiarlo.")
#         if not botella.esta_tapada():
#             raise Exception("La botella ya está destapada.")
     
#         self.corcho = botella.corcho
#         botella.corcho = None
#         print("Botella destapada con éxito.")

#     def limpiar(self):
#         if self.corcho is None:
#             raise Exception("El sacacorchos no tiene ningún corcho que limpiar.")
#         print(f"Se limpió el {self.corcho}.")
#         self.corcho = None


# try:
#     corcho1 = Corcho("Bodega El Esteco")
#     botella1 = Botella(corcho1)
#     sacacorchos = Sacacorchos()

#     sacacorchos.destapar(botella1)  
#     sacacorchos.limpiar()           

# except Exception as e:
#         print("Error:", e)

# 4)"Una heladería es un tipo especial de restaurante.
# "Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:"""


# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida

#     def describir_restaurante(self):
#         print(f"El restaurante se llama '{self.restaurante_nombre}' y ofrece comida de tipo '{self.tipo_comida}'.")

#     def abrir_restaurante(self):
#         print(f"El restaurante '{self.restaurante_nombre}' ahora está abierto.")



# class Heladeria(Restaurante):
#     def __init__(self, restaurante_nombre, tipo_comida, sabores):
#         super().__init__(restaurante_nombre, tipo_comida)  
#         self.sabores = sabores  

#     def mostrar_sabores(self):
#         print("Sabores disponibles:")
#         for sabor in self.sabores:
#             print(f" {sabor}")



# heladeria1 = Heladeria("Dulce Frío", "postres helados", ["chocolate", "vainilla", "frutilla", "menta granizada"])

# heladeria1.describir_restaurante()
# heladeria1.abrir_restaurante()
# heladeria1.mostrar_sabores()


# # "5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que 
# # r"eduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover 
# # "que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.""

# class Personaje:
#     def __init__(self, vida, posicion, velocidad):
#         self.vida = vida
#         self.posicion = posicion  
#         self.velocidad = velocidad

#     def recibir_ataque(self, cantidad):
#         """Reduce la vida del personaje según la cantidad de daño recibida."""
#         self.vida -= cantidad
#         print(f"{self.__class__.__name__} recibió {cantidad} de daño. Vida restante: {self.vida}")
#         if self.vida <= 0:
#             raise Exception(f"{self.__class__.__name__} ha muerto.")  # Lanza excepción si la vida llega a 0 o menos

#     def mover(self, direccion):
#         """Mueve al personaje en la dirección indicada según su velocidad."""
        
#         if isinstance(self.posicion, tuple):
#             if direccion == "arriba":
#                 self.posicion = (self.posicion[0], self.posicion[1] + self.velocidad)
#             elif direccion == "abajo":
#                 self.posicion = (self.posicion[0], self.posicion[1] - self.velocidad)
#             elif direccion == "izquierda":
#                 self.posicion = (self.posicion[0] - self.velocidad, self.posicion[1])
#             elif direccion == "derecha":
#                 self.posicion = (self.posicion[0] + self.velocidad, self.posicion[1])
#         else:
            
#             if direccion == "adelante":
#                 self.posicion += self.velocidad
#             elif direccion == "atrás":
#                 self.posicion -= self.velocidad

#         print(f"{self.__class__.__name__} se movió hacia {direccion}. Nueva posición: {self.posicion}")



# class Soldado(Personaje):
#     def __init__(self, vida, posicion, velocidad, ataque):
#         super().__init__(vida, posicion, velocidad)
#         self.ataque = ataque

#     def atacar(self, otro_personaje):
#         """Ataca a otro personaje, reduciendo su vida según el valor de ataque."""
#         print(f"{self.__class__.__name__} ataca causando {self.ataque} de daño.")
#         otro_personaje.recibir_ataque(self.ataque)


# class Campesino(Personaje):
#     def __init__(self, vida, posicion, velocidad, cosecha):
#         super().__init__(vida, posicion, velocidad)
#         self.cosecha = cosecha

#     def cosechar(self):
#         """Devuelve la cantidad cosechada."""
#         print(f"{self.__class__.__name__} cosechó {self.cosecha} unidades.")
#         return self.cosecha


# if __name__ == "__main__":
#     soldado = Soldado(vida=100, posicion=(0, 0), velocidad=5, ataque=25)
#     campesino = Campesino(vida=50, posicion=(10, 0), velocidad=3, cosecha=10)

#     soldado.mover("derecha")
#     campesino.mover("izquierda")

#     try:
#         soldado.atacar(campesino)
#         soldado.atacar(campesino)
#         soldado.atacar(campesino)
#     except Exception as e:
#         print(e)

#     campesino.cosechar()

# "6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente 
# "se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del 
# "usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario. 
# "Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno. """"

# class Usuario:
#     def __init__(self, nombre, apellido, edad, correo, ciudad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.correo = correo
#         self.ciudad = ciudad

#     def describir_usuario(self):
#         """Muestra un resumen de la información del usuario."""
#         print(f"--- Perfil del usuario ---")
#         print(f"Nombre completo: {self.nombre} {self.apellido}")
#         print(f"Edad: {self.edad}")
#         print(f"Correo electrónico: {self.correo}")
#         print(f"Ciudad: {self.ciudad}")
#         print("--------------------------")

#     def saludar_usuario(self):
#         """Muestra un saludo personalizado."""
#         print(f"¡Hola, {self.nombre}! Bienvenido nuevamente 😄")



# usuario1 = Usuario("María", "Gómez", 28, "maria.gomez@example.com", "Salta")
# usuario2 = Usuario("Carlos", "Pérez", 35, "carlos.perez@example.com", "Buenos Aires")
# usuario3 = Usuario("Lucía", "Fernández", 22, "lucia.fernandez@example.com", "Córdoba")


# usuarios = [usuario1, usuario2, usuario3]

# for u in usuarios:
#     u.describir_usuario()
#     u.saludar_usuario()
#     print()  


