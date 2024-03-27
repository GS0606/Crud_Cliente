from flask import jsonify, request
from storage import ClienteStorage

class ClienteController:
    def __init__(self):
        self.model = ClienteStorage()

    def buscar_clientes(self):
        try:
            clientes = self.model.buscar_clientes()
            return jsonify(clientes)
        except Exception as e:
            return jsonify({"mensagem": "Erro ao buscar clientes: " + str(e)}), 500

    def buscar_cliente_por_id(self, id):
        try:
            cliente = self.model.buscar_cliente_por_id(id)
            if cliente:
                return jsonify(cliente)
            else:
                return jsonify({"mensagem": "Cliente não encontrado"}), 404
        except Exception as e:
            return jsonify({"mensagem": "Erro ao buscar cliente por ID: " + str(e)}), 500

    def inserir_cliente(self):
        try:
            novo_cliente = request.get_json()
            self.model.inserir_cliente(novo_cliente)
            return jsonify({"mensagem": "Cliente inserido com sucesso"})
        except Exception as e:
            return jsonify({"mensagem": "Erro ao inserir cliente: " + str(e)}), 500

    def editar_cliente(self, id):
        try:
            cliente_alterado = request.get_json()
            self.model.editar_cliente(id, cliente_alterado)
            return jsonify({"mensagem": "Cliente atualizado com sucesso"})
        except Exception as e:
            return jsonify({"mensagem": "Erro ao editar cliente: " + str(e)}), 500

    def excluir_cliente(self, id):
        try:
            self.model.excluir_cliente(id)
            return jsonify({"mensagem": "Cliente excluído com sucesso"})
        except Exception as e:
            return jsonify({"mensagem": "Erro ao excluir cliente: " + str(e)}), 500
