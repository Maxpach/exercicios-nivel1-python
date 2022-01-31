from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar != 0:
    try:
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite a sua idade: "))
        sobrenome = input("Digite seu sobrenome: ")
        usuario = Usuario(nome, idade, sobrenome)

        lista_usuarios.append(usuario)

        if usuario.idade == 99:
            break
        if usuario.idade == 98:
            continue

        print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}!")

        if usuario.idade <= 17:
            print(f"{usuario.nome} é adolecente!")

        elif usuario.idade >= 18 and usuario.idade <= 50:
            print(f"{usuario.nome} é adulto!")

        else:
            print(f"{usuario.nome} é idoso!")

        continuar = int(input("Deseja continuar? 1 - sim ou 0 - não -> "))

    except ValueError:
        print(f"Verifique se os dados estão corretos")
else:
    print("lista de usuarios cadastrados:")

    for x in lista_usuarios:
        print(f"Nome completo: {x.nome} {x.sobrenome} - Idade {x.idade}")

    print("O loop entrou no else")