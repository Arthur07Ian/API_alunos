from flask import Flask, jsonify, render_template, request
from flask_restful import Resource, Api
from models import Alunos, Cursos, USUARIOS
from flask_httpauth import HTTPBasicAuth



app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()



@auth.verify_password
def verify_password(username, password):
    if not (username, password):
        return False
    return USUARIOS.query.filter_by(username=username, password=password).first()        # return true or false if the user types the wrong password


# Homepage for de API (there is no need for this btw)
@app.route('/')
def homepage():
    return render_template('homepage.html')


# Page for students (by ID)   URL/aluno/{student_id}
class Aluno(Resource):
    @auth.login_required  # To acess this method is required the user to be loged in
    def get(self):
        try:
            usuario = auth.current_user()
            aluno = Alunos.query.filter_by(id=usuario.aluno.id).first()
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


    @auth.login_required
    def put(self):
        try:
            usuario = auth.current_user()
            aluno = Alunos.query.filter_by(id=usuario.aluno.id).first()
            dados = request.json
            if 'nome' in dados:
                aluno.nome = dados['nome']
                aluno.save()
            response = {
                'nome':aluno.nome,
                'id':aluno.id
            }
        except AttributeError:
            return {'status':'erro', 'message': 'Aluno inexistente'}
        except Exception:
            return {'status':'erro', 'message': 'Ocorreu algum erro.'}
        return response


    @auth.login_required
    def delete(self):
        try:
            usuario = auth.current_user()
            aluno = Alunos.query.filter_by(id=usuario.aluno.id).first()
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



class Registrar_Cursos(Resource):
    def get(self):
        cursos = Cursos.query.all()
        response = [{"nome":curso.nome, "id":curso.id, "aluno":curso.aluno.nome} for curso in cursos]
        return response

    
    def post(self):
        dados = request.json
        aluno = Alunos.query.filter_by(nome=dados['aluno']).first()
        curso = Cursos(nome=dados['nome'], aluno=aluno)
        curso.save()
        response = {
            'aluno':curso.aluno.nome,
            'curso':curso.nome,
            'id':curso.id
        }
        return response


# RESTful architeture: adding an URN to each class
api.add_resource(Aluno, '/aluno')
api.add_resource(Registrar_Aluno, '/alunos')
api.add_resource(Registrar_Cursos, '/cursos')


if __name__ == '__main__':
    app.run(debug=True)