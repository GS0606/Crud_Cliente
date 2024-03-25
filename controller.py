from flask import jsonify, request
from model import ClienteModel

class ClienteController:
    def __init__(self):
        self.model = ClienteModel()

    def buscar_clientes(self):
        clientes = self.model.buscar_clientes()
        return jsonify(clientes)

    def buscar_cliente_por_id(self, id):
        cliente = self.model.buscar_cliente_por_id(id)
        if cliente:
            return jsonify(cliente)
        else:
            return jsonify({"mensagem": "Cliente não encontrado"}), 404

    def inserir_cliente(self):
        novo_cliente = request.get_json()
        self.model.inserir_cliente(novo_cliente)
        return jsonify({"mensagem": "Cliente inserido com sucesso"})

    def editar_cliente(self, id):
        cliente_alterado = request.get_json()
        self.model.editar_cliente(id, cliente_alterado)
        return jsonify({"mensagem": "Cliente atualizado com sucesso"})

    def excluir_cliente(self, id):
        self.model.excluir_cliente(id)
        return jsonify({"mensagem": "Cliente excluído com sucesso"})
