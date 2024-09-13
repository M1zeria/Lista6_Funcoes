def multiplo (n):
    if n%3 == 0:
        return True
    else:
        return False

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat = fat*i
    return fat

def valorS(n):
    s = 0
    for i in range(n+1):
        s = s+n/fatorial(i)
    return s

soma = 0
contador = 0
while contador < 5:
    n = int(input())
    if multiplo(n)==True:
        soma = soma+fatorial(n)
    elif multiplo(n)==False:
        soma = soma+valorS(n)
    contador +=1

print(f"{soma:.2f}")
