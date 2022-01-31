# Considerando uma lista (lista = []), você pode executar as ações:
# insert i e: Inserir o inteiro e na posição i;
# print: Exibe a lista;
# remove e: Exclui a primeira ocorrência do inteiro e;
# append e: Adiciona o inteiro e no final da lista;
# sort: Ordena a lista;
# pop: Remove o último elemento da lista;
# reverse: Inverte a lista.
# Onde serão informadas N sequências de ações da listagem acima, que devem ser aplicadas em uma lista.

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# saida esperada
#
#[6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]



#n = int(input())
#lista = []
#for i in range(0,n):
    #print(lista)
#    lista.insert(0, 5)
#    lista.insert(1, 10)
#    lista.insert(0, 6)
#    print(lista)
#    lista.remove(6)
#    lista.append(9)
#    lista.append(1)
#    lista.sort()
#    print(lista)
#    lista.pop()
#    lista.reverse()
#    print(lista)
#    if lista == [9, 5, 1]:
#        break

n = int(input())

lista = []
for i in range(0, n):
    values = input().split()

    if len(values) == 3:
        acao, i, e = values
    elif len(values) == 2:
        acao, e = values
    else:
        acao = values.pop()

    if acao == "insert":
        lista.insert(int(i), int(e))
    elif acao == "print":
        print(lista)
    elif acao == "remove":
        lista.remove(int(e))
    elif acao == "append":
        lista.append(int(e))
    elif acao == "sort":
        lista.sort()
    elif acao == "pop":
        lista.pop()
    elif acao == "reverse":
        lista.reverse()