def eh_primo(numero):

    if numero <= 1:
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
            
    return True

print("Números primos entre 1 e 100:")
for n in range(1, 101):
    if eh_primo(n):
        print(n, end=" ")