## ARCHIVO PRINCIPAL ##
print 'bienvenido al examen final de IPC 2014'
print 'el programa se trata del famoso juego, ahorcado'


class Carro: 
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print "tenemos ",gasolina," litros"
        
    def arrancar(self):
        if self.gasolina >0 :
            print "Arrancando"
        else:
            print "No arranca"
            
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print "quedan ",self.gasolina," litros"
        else:
            print "no se mueve"
