def consultar():
    arq = open('base_aluno.txt', 'r')
    print(arq.read())
    arq.close()
