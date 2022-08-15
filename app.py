from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)

alunos = [
    {'nome': 'Jhonatan',
     'cursos': ['matemática', 'física', 'química']
     },

    {'nome': 'Arthur',
     'cursos': ['computação', 'física', 'matemática', 'química']
     },

    {'nome':'Beatriz',
     'cursos': ['história', 'redação', 'biologia']
     }
]

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/aluno/<int:id>', methods=['GET', 'PUT'])
def aluno(id):
    if request.method == 'GET':
        aluno = alunos[id]
        return jsonify({'aluno':aluno})
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        alunos[id] = dados
        return jsonify(dados)





if __name__ == '__main__':
    app.run(debug=True)