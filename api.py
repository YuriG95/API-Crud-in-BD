from flask import Flask, jsonify, request
from bd import db, Usuario, init_db

app = Flask(__name__)

init_db(app)

@app.route('/add_usuario' , methods = ['POST'])
def add_usuario():
    data = request.get_json()
    
    # Verifica se os dados estão completos
    if not data or not 'nome' in data or not 'email' in data:
        return jsonify({"message": "Dados incompletos"}), 400

    nome = data['nome']
    email = data['email']
    
    # Cria novo usuário
    novo_usuario = Usuario(nome=nome, email=email)
    
    try:
        # Adiciona e salva o novo usuário 
        db.session.add(novo_usuario)
        db.session.commit()
        return jsonify({"message": "Usuário adicionado com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

# Rota para listar todos os usuar
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    usuarios_data = [{"id": u.id, "nome": u.nome, "email": u.email} for u in usuarios]
    return jsonify(usuarios_data)

# Rota para deletar os usuarios

@app.route('/rmv_usuario/<int:id>' , methods=['DELETE'])
def remove_usario(id):
     item = Usuario.query.get(id)
     if item is None:
         return jsonify({'error' : 'Item não encontrado'}), 404
     
    #Deletar o item no Bd
     db.session.delete(item) 
     db.session.commit()
     return jsonify({'message' : f'Sucesso item {id} deletado'}), 200


if __name__ == '__main__':
    app.run(debug=True)

