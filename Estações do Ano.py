def EstacaoAno(dia, mes):
    if mes == 9 and dia >=21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20:
        return "PRIMAVERA"
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <=20:
        return "VERAO"
    if mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        return "OUTONO"
    if mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <=20:
        return "INVERNO"

dia = int(input())
mes = int(input())

print(EstacaoAno(dia, mes))
