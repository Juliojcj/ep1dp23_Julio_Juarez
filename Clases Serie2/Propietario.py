from Privado import Privado

class Propietario(Privado):
    propietarioid = 0
    propietarionom = ""
    propietariotel = 0

    def Datospropietarios(self):
        super().DatosPropietarios()

        print("propietarioid" , self.propietarioid , "propietarionom" , self.propietarionom , "propietariotel" , self.propietariotel)
