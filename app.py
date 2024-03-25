from flask import Flask
from controller import ClienteController

app = Flask(__name__)
controller = ClienteController()

@app.route('/clientes', methods=['GET'])
def buscar_clientes():
    return controller.buscar_clientes()

@app.route('/clientes/<int:id>', methods=['GET'])
def buscar_cliente_por_id(id):
    return controller.buscar_cliente_por_id(id)

@app.route('/clientes', methods=['POST'])
def inserir_cliente():
    return controller.inserir_cliente()

@app.route('/clientes/<int:id>', methods=['PUT'])
def editar_cliente(id):
    return controller.editar_cliente(id)

@app.route('/clientes/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    return controller.excluir_cliente(id)

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
