from flask import Flask, jsonify, render_template, request
from flask_restful import Resource, Api
from models import Alunos, Cursos



app = Flask(__name__)
api = Api(app)


# Homepage for de API (there is no need for this btw)
@app.route('/')
def homepage():
    return render_template('homepage.html')


# Page for students (by ID)   URL/aluno/{student_id}
class Aluno(Resource):
    def get(self, id):
        try:
            aluno = Alunos.query.filter_by(id=id).first()
            response = {
                'nome': aluno.nome,
                'id': aluno.id
            }
        except AttributeError:
            response = {
                'status':'error',
                'message':'Aluno não encontrado'
            }
        except Exception:
            return {'status':'erro', 'message': 'Ocorreu algum erro.'}
        finally:
            return response


    def put(self, id):
        try:
            aluno = Alunos.query.filter_by(id=id)
            dados = request.json
            if 'nome' in dados:
                aluno.nome = dados['nome']
            response = {
                'nome':aluno.nome,
                'id':aluno.id
            }
        except AttributeError:
            return {'status':'erro', 'message': 'Aluno inexistente'}
        except Exception:
            return {'status':'erro', 'message': 'Ocorreu algum erro.'}
        return response

    
    def delete(self, id):
        try:
            aluno = Alunos.query.filter_by(id=id)
            aluno.delete()
        except AttributeError:
            return {'status':'erro', 'message': 'Aluno inexistente'}
        except Exception:
            return {'status':'erro', 'message': 'Ocorreu algum erro.'}
        finally:
            return {'status': 'sucesso', 'message': 'registro excluido'}



# Page to register students 
class Registrar_Aluno(Resource):
    def get(self):
        alunos = Alunos.query.all()
        alunos_lista = []
        for row in alunos:
            aluno = {"id": row.id,
                     "nome": row.nome}
            alunos_lista.append(aluno)
        response = alunos_lista
        return response
    
    def post(self):
        dados = request.json
        aluno = Alunos(nome=dados['nome'])
        aluno.save()
        return {"status": "sucesso", "message":"registro inserido, aluno inserido no ID {}".format(aluno.id)}



# RESTful architeture: adding an URN to each class
api.add_resource(Aluno, '/aluno/<int:id>')
api.add_resource(Registrar_Aluno, '/aluno')


if __name__ == '__main__':
    app.run(debug=True)