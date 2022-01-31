n = int(input())

if (n % 2 != 0):
    print("Estranho")
else:
    if(n<10):
        print("Não é estranho")
    elif(n >= 10 and n <= 20):
        print("Estranho")
    else:
        print("Não é estranho")