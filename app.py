from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)

alunos = [
    {'id': 0,
     'nome': 'Jhonatan',
     'cursos': ['matemática', 'física', 'química']
     },

    {'id': 1,
     'nome': 'Arthur',
     'cursos': ['computação', 'física', 'matemática', 'química']
     },

    {'id':2,
     'nome':'Beatriz',
     'cursos': ['história', 'redação', 'biologia']
     }
]

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/aluno/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def aluno(id):
    if request.method == 'GET':
        try:
            response = alunos[id]
        except IndexError:
            message =  "Aluno de ID {} inexistente".format(id)
            response = {"status": "erro", "message": message}
        except Exception:
            message = "Erro desconhecido"
            response = {"status": "erro", "message": message}
        finally:
            return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        alunos[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        alunos.pop(id)
        return jsonify({'status': 'sucesso', 'message': 'registro excluido'})




@app.route('/aluno', methods=['POST', 'GET'])
def registrar_aluno():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(alunos)
        dados['id'] = posicao
        alunos.append(dados)
        return jsonify({"status": "sucesso", "message":"registro inserido, aluno inserido no ID {}".format(alunos[len(alunos)-1]['id'])})
    elif request.method == 'GET':
        return jsonify(alunos)



if __name__ == '__main__':
    app.run(debug=True)