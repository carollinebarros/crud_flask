from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

usuariosDB=[
{
'nome':'User1',
'idade':'35',
'email':'user1@teste.com',
'senha':'12345'
},
{
'nome':'User2',
'idade':'27',
'email':'user2@teste.com',
'senha':'54321'
}
]

@app.route("/",methods=['GET'])
def welcome() :
    return "Welcome to Python Webservice"

@app.route("/usuarios/getUsuarios",methods=['GET'])
def getStudents():
    return jsonify({"usuarios":usuariosDB})

@app.route("/usuarios/getUsuario/<nome>",methods=['GET'])
def getUsuarioNome(nome):
    usuario = [user for user in usuariosDB if(user['nome']==nome)]
    print(usuario)
    return jsonify({"user":usuario})

@app.route("/usuarios/putUsuario/<nome>",methods=['PUT'])
def atualizarUsuario(nome):
    usuario = [user for user in usuariosDB if (user['nome'] == nome)]

    if('nome' in request.json):
        print("Usuario Disponivel")
    if('email' in request.json):
        usuario[0]['email'] = request.json['email']
    return jsonify({"user":usuario[0]})

@app.route("/usuarios/postUsuario/",methods=['POST'])
def inserirUsuario():
    usuario = {
           'nome': request.json['nome'],
           'idade': request.json['idade'],
           'email': request.json['email'],
           'senha': request.json['senha']
    }
    usuariosDB.append(usuario)
    return jsonify({"user":usuariosDB})

@app.route("/usuarios/deleteUsuario/<nome>",methods=['DELETE'])
def removeUsuario(nome):
    usuario = [user for user in usuariosDB if (user['nome'] == nome)]
    if(len(usuario) > 0):
        usuariosDB.remove(usuario[0])
    return jsonify({"user": usuariosDB})


if __name__=="__main__":
    app.run()