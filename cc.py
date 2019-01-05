import pymysql.cursors  # import lib pyMySQL to access MariaDB Database


class Conexao:  # Connect to Database
    def __init__(self, servidor, usuario, senha, banco):
        self.db = pymysql.connect(servidor, usuario, senha, banco)
        self.cursor = self.db.cursor()
        print('\033[32mConexão ao Banco de Dados bem sucedida!\033[m')

    def terminar_conexao(self):  # Stop Connection
        con.terminar_conexao()
        self.cursor.close()

    def listar_clientes(self):
        self.cursor.execute('SELECT * FROM clientes')
        resposta = self.cursor.fetchall()
        print('\n\nClientes:')
        for item in resposta:
            print(item)

    def listar_fornecedor(self):
        self.cursor.execute('SELECT * FROM fornecedor')
        resposta = self.cursor.fetchall()
        print('\n\nFornecedores:')
        for item in resposta:
            print(item)

    def listar_produtos(self):
        self.cursor.execute('SELECT * FROM produtos')
        resposta = self.cursor.fetchall()
        print('\n\nProdutos:')
        for item in resposta:
            print(item)

    def comitar(self):
        self.db.commit()


class Cadastro:  # SuperClass to reuse code
    def __init__(self, nome, cidade, qtd):
        self.nome = nome
        self.cidade = cidade
        self.qtd = qtd


con = Conexao  # Connection to Database instance

try:
    con = Conexao('localhost', 'root', '', 'pycadastros')
    cursor = con.cursor
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()
    print('Versão do MariaDB:', version)
except Exception as e003:
    print('Ocorreu um erro:', e003)


def escolher():  # Initial guide
    try:
        iescolha = int(input('Digite sua escolha:\n1 = Cadastrar produto\n2 = Cadastrar fornecedor'
                             '\n3 = Cadastrar cliente\n4 = Listar tabelas\n5 = Sair\n\n\t>'))
        if iescolha == 1:
            cadastrar_produto()
        elif iescolha == 2:
            cadastrar_fornecedor()
        elif iescolha == 3:
            cadastrar_cliente()
        elif iescolha == 4:
            con.listar_clientes()
            con.listar_fornecedor()
            con.listar_produtos()
        elif iescolha == 5:
            print('Até logo!')
            exit()
        else:
            print('Valor inválido, tente novamente')
            return escolher()

    except ValueError:
        print('Valor inválido, tente novamente')
        return escolher()


def cadastrar_cliente():  # Register clients
    Cadastro.nome = input('Digite o nome do Cliente: ')
    Cadastro.cidade = input('Digite a cidade do Cliente: ')
    try:
        sql = "INSERT INTO clientes(cli_nome, cli_cidade) VALUES('{}', '{}')".format(Cadastro.nome, Cadastro.cidade)
        cursor.execute(sql)
        con.comitar()
        resultado = cursor.fetchone()
        print(resultado)
        print('\033[32mOperação realizada!\033[m')
    except Exception as e002:
        print('\033[31mOperação não efetuada, erro:', e002, '\033[m')
    finally:
        con.cursor.close()
        de_novo()


def cadastrar_fornecedor():  # Register providers
    Cadastro.nome = input('Digite o nome do Fornecedor: ')
    Cadastro.cidade = input('Digite a cidade do Fornecedor: ')
    try:
        sql = "INSERT INTO fornecedor(for_nome, for_cidade) VALUES('{}', '{}')".format(Cadastro.nome,
                                                                                       Cadastro.cidade)
        cursor.execute(sql)
        con.comitar()
        print('\033[32mOperação realizada!\033[m')
    except Exception as e002:
        print('\033[31mOperação não efetuada, erro:', e002, '\033[m')
    finally:
        con.cursor.close()
        de_novo()


def cadastrar_produto():  # Register products
    try:
        Cadastro.qtd = int(input('Digite a quantidade do Produto: '))
    except ValueError:
        print('Valor inválido, tente novamente')
        return cadastrar_produto()
    Cadastro.nome = input('Digite o nome do produto: ')
    try:
        sql = "INSERT INTO produtos(pro_nome, pro_qtd) VALUES('{}', '{}')".format(Cadastro.nome, Cadastro.qtd)
        cursor.execute(sql)
        con.comitar()
        print('\033[32mOperação realizada!\033[m')
    except Exception as e002:
        print('\033[31mOperação não efetuada, erro:', e002, '\033[m')

    finally:
        con.cursor.close()
        de_novo()


def de_novo():  # Ask if the user wants to run again
        a = input('Quer executar novamente? [s/n]')
        if a in 'sS':
            escolher()
        elif a in 'nN':
            con.cursor.close()
            print('Servidor fechado')
            exit()
        else:
            print('Valor errado, tente novamente')


escolher()  # Start process
