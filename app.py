from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import DictCursor
import json

app = Flask("Livretos")

def get_db_connection():
    conn = psycopg2.connect(
        dbname="rklrejgj", 
        user="rklrejgj", 
        password="vSDcFc14nusYYaRPMQVY6qvhy0_A8vbv",
        host="silly.db.elephantsql.com"  
    )
    return conn

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/livro', methods=['POST'])
def post_livros():
    data = request.json
    titulo = data['Titulo']
    autor = data['Autor']
    ano_publicacao = data['AnoPublicacao']
    genero = data['Genero']

    info_livros = (titulo, autor, ano_publicacao, genero)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Livros (Titulo, Autor, AnoPublicacao, Genero) VALUES (%s, %s, %s, %s)
    """, info_livros)

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Livro adicionado com sucesso!"})

# Exemplo de como ajustar a função get_livros
@app.route('/livro', methods=['GET'])
def get_livros():
    conn = get_db_connection()
    cursor = conn.cursor()

    filtro_genero = request.args.get("genero")

    if filtro_genero:
        cursor.execute("""
        SELECT * FROM Livros WHERE Genero = %s
        """, (filtro_genero,))
    else:
        cursor.execute("SELECT * FROM Livros")
        
    livros = cursor.fetchall()
    conn.close()

    livros_list = []
    for livro in livros:
        livro_dict = {
            "id": livro[0],
            "Titulo": livro[1],
            "Autor": livro[2],
            "AnoPublicacao": livro[3],
            "Genero": livro[4]
        }
        livros_list.append(livro_dict)

    return jsonify(livros_list)

@app.route("/livro/<int:id>", methods=['GET'])
def escolhe_livro(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM Livros WHERE ID = %s
    """, (id,))
    livro = cursor.fetchone()
    conn.close()

    if livro:
        livro_dict = {
            "id": livro[0],
            "Titulo": livro[1],
            "Autor": livro[2],
            "AnoPublicacao": livro[3],
            "Genero": livro[4]
        }
        return jsonify(livro_dict)
    else:
        return jsonify({"mensagem": "Livro não encontrado"}), 404

@app.route("/livro/<int:id>", methods=['DELETE'])
def deleta_livro(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Livros WHERE ID = %s", (id,))
    livro = cursor.fetchone()

    if livro is None:
        conn.close()
        return jsonify({"erro": "Livro não encontrado"}), 404

    cursor.execute("DELETE FROM Livros WHERE ID = %s", (id,))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "O livro foi deletado"})

@app.route('/usuario', methods=['POST'])
def post_usuario():
    data = request.json
    nome = data['Nome']
    email = data['Email']
    data_cadastro = data['DataCadastro']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Usuarios (Nome, Email, DataCadastro) VALUES (%s, %s, %s)
    """, (nome, email, data_cadastro))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"})

@app.route('/usuario', methods=['GET'])
def get_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    usuarios = cursor.fetchall()
    conn.close()

    usuarios_list = []
    for usuario in usuarios:
        usuario_dict = {
            "id": usuario[0],
            "Nome": usuario[1],
            "Email": usuario[2],
            "DataCadastro": usuario[3]
        }
        usuarios_list.append(usuario_dict)

    return jsonify(usuarios_list)

@app.route("/usuario/<int:id>", methods=['GET'])
def escolhe_usuario(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE ID = %s", (id,))
    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        usuario_dict = {
            "id": usuario[0],
            "Nome": usuario[1],
            "Email": usuario[2],
            "DataCadastro": usuario[3]
        }
        return jsonify(usuario_dict)
    else:
        return jsonify({"mensagem": "Usuário não encontrado"}), 404

@app.route("/usuario/<int:id>", methods=['DELETE'])
def deleta_usuario(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE ID = %s", (id,))
    usuario = cursor.fetchone()

    if usuario is None:
        conn.close()
        return jsonify({"erro": "Usuário não encontrado"}), 404

    cursor.execute("DELETE FROM Usuarios WHERE ID = %s", (id,))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "O usuário foi excluído"})

if __name__ == '__main__':
    app.run(debug=True)
