def cadastrar():
    print('*' * 20)
    print('** Tela de cadastro de alunos **')
    cad = True
    arq = open('base_aluno.txt', 'w')
    while cad:
        nome = input('Digite seu nome: ')
        mat = input('Digite sua matricula: ')
        arq.write(nome)
        arq.write(mat)
        break

    arq.close()
