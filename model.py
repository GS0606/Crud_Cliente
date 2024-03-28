class Cliente:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def __dict__(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "endereco": self.endereco
        }
