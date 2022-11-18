import Cadastro
import Consulta

print('*' * 20)
print('** Sistema de controle academico **')
print('*' * 20)
print('Digite a operação que deseja executar: ')
operacao = int(input("[1] Para Cadastrar [2] Para Consultar [3] Sair \n"))

if operacao == 1:
    Cadastro.cadastrar()
elif operacao == 2:
    Consulta.consultar()
