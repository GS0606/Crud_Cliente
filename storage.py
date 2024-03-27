import sqlite3
from model import Cliente

class ClienteStorage:
    def __init__(self, db_name='loja_virtual10.db'):
        self.db_name = db_name

    def conectar_bd(self):
        return sqlite3.connect(self.db_name)

    def criar_tabela_cliente(self):
        with self.conectar_bd() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    endereco TEXT
                )
            """)
            conexao.commit()

    def buscar_clientes(self):
        with self.conectar_bd() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM cliente")
            clientes = cursor.fetchall()
        return [Cliente(id=row[0], nome=row[1], endereco=row[2]) for row in clientes]


    def buscar_cliente_por_id(self, id):
        with self.conectar_bd() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM cliente WHERE id=?", (id,))
            cliente = cursor.fetchone()
        return [Cliente(id=row[0], nome=row[1], endereco=row[2]) for row in cliente]


    def inserir_cliente(self, novo_cliente):
        with self.conectar_bd() as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO cliente (nome, email, endereco) VALUES (?, ?, ?)",
                           (novo_cliente['nome'], novo_cliente['email'], novo_cliente['endereco']))
            conexao.commit()

    def editar_cliente(self, id, cliente_alterado):
        with self.conectar_bd() as conexao:
            cursor = conexao.cursor()
            cursor.execute("UPDATE cliente SET nome=?, email=?, endereco=? WHERE id=?",
                           (cliente_alterado['nome'], cliente_alterado['email'], cliente_alterado['endereco'], id))
            conexao.commit()

    def excluir_cliente(self, id):
        with self.conectar_bd() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM cliente WHERE id=?", (id,))
            conexao.commit()
