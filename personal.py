"LOAIZA NAVARRO GEOVANNI DANIEL 18TE0661"
"UNIDAD 4"
"EVALUACIÓN GITHUB"


"En este código se definen las clases de la empresa y usuarios"


print("Archivo modificado en Software Pycharm")
class Gerente:
    def __init__(self, Nombre, Altura, Vestimenta):
        self.__Vestimenta=Vestimenta
        self.__Altura=Altura
        self.__Nombre=Nombre

    def status(self):
        print("El gerente de la empresa es un empleado que mide ", self.__Altura, "metros")
        print("Se llama ", self.__Nombre, "y tiene", self.__Vestimenta)

    def getInfo(self):
        print("Nombre: ", self.__Nombre)
        print("Altura: ", self.__Altura)
        print("Vestimenta: ", self.__Vestimenta)

    def Entrevistando(self):
        return ("En este momento el Gerente esta entrevistando a una persona para su contratacion")
    def Supervisando(self):
        return ("En este momento el Gerente esta supervisando las áreas de trabajo")
    def Noasiste(self):
        return ("El gerente no asistio")


class Empleado(Gerente):
    def __init__(self, Nombre, Altura, Vestimenta):
        super().__init__(Nombre, Altura, Vestimenta)
        self.__Vestimenta = Vestimenta
        self.__Altura = Altura
        self.__Nombre = Nombre

    def status(self):
        print("El empleado de la empresa es un empleado que mide ", self.__Altura, "metros")
        print("Se llama ", self.__Nombre, "y tiene", self.__Vestimenta)

    def Trabajanto(self):
        print("En este momento el empleado esta trabajando.")

    def Descansando(self):
        print("En este momento el empleado esta descansando.")

    def Cobrar(self):
        print("En este momento el trabajador esta cobrando.")


class Persona(Gerente):
    def __init__(self, Nombre, Altura, Vestimenta):
        super().__init__(Nombre, Altura, Vestimenta)
        self.__Vestimenta = Vestimenta
        self.__Altura = Altura
        self.__Nombre = Nombre

    def getInfo(self):
        super().getInfo()

    def status(self):
        print("La persona va a solicitar empleo en la empresa, es una persona que mide ", self.__Altura, "metros")
        print("Se llama ", self.__Nombre, "y tiene", self.__Vestimenta)

    def Solicitando(self):
        print("En este momento la persona esta solicitando empleo")

    def Buscando(self):
        print("En este momento la persona esta buscando empleo")

    def Aceptado(self):
        print("La persona ha sido aceptada")