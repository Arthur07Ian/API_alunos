from flask import Flask, jsonify, render_template, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


# Gonna change this to a database later -> using list for testing purposes
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

# Homepage for de API (there is no need for this btw)
@app.route('/')
def homepage():
    return render_template('homepage.html')


# Page for students (by ID)   URL/aluno/{student_id}
class Aluno(Resource):
    def get(self, id):
        try:
            response = alunos[id]
        except IndexError:
            message =  "Aluno de ID {} inexistente".format(id)
            response = {"status": "erro", "message": message}
        except Exception:
            message = "Erro desconhecido"
            response = {"status": "erro", "message": message}
        finally:
            return response

    def put(self, id):
        dados = json.loads(request.data)
        alunos[id] = dados
        return dados
    
    def delete(self, id):
        alunos.pop(id)
        return {'status': 'sucesso', 'message': 'registro excluido'}



# Page to register students 
class Registrar_Aluno(Resource):
    def get(self):
        return alunos
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(alunos)
        dados['id'] = posicao
        alunos.append(dados)
        return {"status": "sucesso", "message":"registro inserido, aluno inserido no ID {}".format(alunos[len(alunos)-1]['id'])}



# RESTful architeture: adding an URN to each class
api.add_resource(Aluno, '/aluno/<int:id>')
api.add_resource(Registrar_Aluno, '/aluno')


if __name__ == '__main__':
    app.run(debug=True)