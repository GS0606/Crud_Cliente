
from flask import Flask, jsonify, request
from service import ClienteService

app = Flask(__name__)
controller = ClienteService()

@app.route('/clientes', methods=['GET'])
def buscar_clientes():
    clientes = controller.buscar_clientes()
    clientes_serializaveis = [cliente.__dict__() for cliente in clientes]
    return jsonify(clientes_serializaveis)

@app.route('/clientes/<int:id>', methods=['GET'])
def buscar_cliente_por_id(id):
    try:
        cliente = controller.buscar_cliente_por_id(id)
        cliente_serializavel = cliente.__dict__()
        return jsonify(cliente_serializavel)
    except ValueError as e:
        return jsonify({"mensagem": str(e)}), 404

@app.route('/clientes', methods=['POST'])
def inserir_cliente():
    novo_cliente = request.get_json()
    controller.inserir_cliente(novo_cliente)
    return jsonify({"mensagem": "Cliente inserido com sucesso"})

@app.route('/clientes/<int:id>', methods=['PUT'])
def editar_cliente(id):
    cliente_alterado = request.get_json()
    controller.editar_cliente(id, cliente_alterado)
    return jsonify({"mensagem": "Cliente atualizado com sucesso"})

@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    controller.excluir_cliente(id)
    return jsonify({"mensagem": "Cliente excluído com sucesso"})

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)