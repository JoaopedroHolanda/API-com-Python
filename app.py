from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [{
     'id': 1,
    'titulo': "O senhor dos Anéis - A Sociedade do Anel",
    'autor' : "J.R.R Tolkien"
},
{
    'id': 2,
    'titulo': "Harry Potter e a Pedra Filosofal",
    'autor': "J.K. Rowling"
},
{
    'id': 3,
    'titulo': "A Guerra dos Tronos",
    'autor': "George R.R. Martin"
},
{
    'id': 4,
    'titulo': "1984",
    'autor': "George Orwell"
}]

@app.route('/livros', methods=['GET'])
def obterLivros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def consultarLivroPorId(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>', methods=['PUT'])
def editarLivroPorid(id):
    livroAlterado = request.get_json()
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[i].update(livroAlterado)
            return jsonify(livros[i])

@app.route('/livros', methods=['POST'])
def incluirNovoLivro():
    novoLivro = request.get_json()
    livros.append(novoLivro)
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluirLivro(id):
    for i,livro in enumerate(livros):
         if livro.get('id') == id:
            del livros[i]
    return jsonify(livros)
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
