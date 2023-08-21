class asiento:
    def _init_(self,color,registro,precio):
        self.color = color
        self.registro = registro
        self.precio = precio
    
    def cambiarColor(self,color):
        if color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco":
            self.color = color

class Motor:
    def _init_(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,registro):
        self.registro = registro

    def asignarTipo(self,tipo):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo = tipo

class Auto:
    def _init_(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados
    
    def cantidadAsientos(self):
        nasientos = 0
        for i in range(self.asientos.length):
            if self.asientos[i] != None:
                nasientos += 1
        return nasientos


    def verificarIntegridad(self):
        if self.registro == Motor.registro:
            for i in range(self.asientos.length):
                if self.asientos != None:
                    if self.asientos.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"