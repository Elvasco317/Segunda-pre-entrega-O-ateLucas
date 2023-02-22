class Cliente:
    def __init__(self, nombre, edad, email, telefono):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.telefono = telefono
    
    def ver_info(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nEmail: {self.email}\nTelefono: {self.telefono}")
    
    def cambiar_email(self, nuevo_email):
        self.email = nuevo_email
        print(f"El nuevo email para {self.nombre} es {self.email}")
    
    def __str__(self):
        return f"Cliente: {self.nombre} ({self.email})"
    

class Compra:
    def __init__(self, cliente, producto, precio, cantidad):
        self.cliente = cliente
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad
    
    def calcular_total(self):
        return self.precio * self.cantidad
    
    def agregar_cantidad(self, nueva_cantidad):
        self.cantidad += nueva_cantidad
        print(f"Se agregó {nueva_cantidad} unidades de {self.producto}. Cantidad total: {self.cantidad}")
    
    def __str__(self):
        return (f"Compra de {self.cantidad} unidad(es) de {self.producto} por {self.cliente}. Total: {self.calcular_total()} dolares")
