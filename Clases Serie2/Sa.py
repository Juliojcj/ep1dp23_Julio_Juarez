from Propietario import Propietario

class Sa(Propietario):

    nombresa = ""
    representante = ""
    represencorreo = ""

    def DatosSa(self):
        super().DatosSa()
        print("nombresa;" , self.nombresa , "representante" , self.representante , "represencorreo: " , self.represencorreo)
        