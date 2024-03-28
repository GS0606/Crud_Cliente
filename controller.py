
from storage import ClienteStorage

class ClienteController:
    def __init__(self):
        self.model = ClienteStorage()

    def buscar_clientes(self):
        return self.model.buscar_clientes()

    def buscar_cliente_por_id(self, id):
        cliente = self.model.buscar_cliente_por_id(id)
        if cliente:
            return cliente
        else:
            raise ValueError("Cliente não encontrado")

    def inserir_cliente(self, novo_cliente):
        self.model.inserir_cliente(novo_cliente)

    def editar_cliente(self, id, cliente_alterado):
        self.model.editar_cliente(id, cliente_alterado)

    def excluir_cliente(self, id):
        self.model.excluir_cliente(id)
