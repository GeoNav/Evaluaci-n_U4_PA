"LOAIZA NAVARRO GEOVANNI DANIEL 18TE0661"
"UNIDAD 4"
"EVALUACIÓN GITHUB"


"El código a continuación es usado para dar infromación de la empresa dada por el problema"

"Se va a usar en dadpo caso de colocar en la ejecución del código el método de la clase"

"Se coloca como un archivo adicional para evitar fallas en la ejecucuión"

class Company:
    def __init__(self, Nombre, Direccion, Vacante):
        self.__Nombre=Nombre
        self.__Direccion=Direccion
        self.__Vacante=Vacante

    def GetInfoEmpresa(self):
        print("El nombre de la empresa es:", self.__Nombre)
        print("La direccion es:", self.__Direccion)
        print("Tipo de vacante:", self.__Vacante)