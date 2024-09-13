def ClassificaAluno(media, faltas):
    if media >= 9.5 and faltas <= 10:
        return "APROVADO COM LOUVOR"
    if media < 9.5 and media >= 7 and faltas <=10:
        return "APROVADO"
    if media < 7:
        return "REPROVADO"
    if faltas > 10:
        return "REPROVADO POR FALTAS"


media = float(input())
faltas = int(input())

print(ClassificaAluno(media, faltas))
