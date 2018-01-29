# Programa que transforma a notação de 24 horas para a notação de 12 horas.

def calculaHorario(hora):
    return hora - 12

def converteHora(hora, minuto):
    if(hora < 12 and hora > 0):
        print("%i:%i A.M"%(hora, minuto))
    elif(hora == 0):
        print("12:%i A.M." % (minuto))
    else:
        if(hora == 12):
            print("12:%i P.M."%(minuto))
        else:
            hora = calculaHorario(hora)
            print("%i:%i P.M." % (hora, minuto))




ciclo = True
while ciclo:
    hora = int(input("Digite a Hora: "))
    minuto = int(input("Digite os Minutos: "))
    converteHora(hora, minuto)
    ciclo = bool(int(input("Deseja continuar convertendo horários? (1 = Sim / 0 = Não): ")))


