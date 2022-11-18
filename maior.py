from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def maior_lista():
    with open('lista.txt', 'r') as arq:
        lista_bruta = arq.read()
        lista_tratada = lista_bruta.split()
        lista_convertida = []
        for i in range(0, len(lista_tratada)):
            lista_convertida.append(int(lista_tratada[i]))
    maior_elemento = max(lista_convertida)

    return render_template('pagina.html', conteudo=maior_elemento)


app.run()
