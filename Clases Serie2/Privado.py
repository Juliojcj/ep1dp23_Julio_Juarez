from Centroeduc import Centroeduc

class Privado(Centroeduc):
    Cantidadh = 0
    Cantidadm = 0

    def DatosPrivado(self):
        super().DatosCentroeduc()
        print("cantidadh" , self.Cantidadh , "cantidadm" , self.Cantidadm)