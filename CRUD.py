import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "blablabla",
    database = "bd_crud"
)

cursor=conexao.cursor(dictionary=True)

cursor.execute("SELECT * FROM usuario")
usuarios = cursor.fetchall()




def criar_usuario(new_user:str):
    global cursor, usuarios, conexao
    for usuario in usuarios:
        if new_user in usuario['nome']:
            print("Usuario já existe")
            return False
    else:
        user = (new_user, )
        cursor.execute("INSERT INTO usuario (nome) VALUES (%s)", user)
        conexao.commit()
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()
        return "Usuario criado com sucesso!"


def pegar_usuario_por_nome(user: str):
    global usuarios
    for usuario in usuarios:
        if user in usuario["nome"]:
            print(f"Usuario encontrado \n{user}")
            return True
        else:
            print(f"Usuario inexistente!!")
        return False


def pegar_usuarios():
    global usuarios
    for usuario in usuarios:
        print(f"Usuario {usuario['nome']}: id {usuario['id']}")
    return

def pegar_usuario_por_id(id_buscador:int):
    global usuarios
    for usuario in usuarios:
        if id_buscador == usuario['id']:
            print(f"Usuário encontrado \nUsuário = {usuario['nome']} : ID = {usuario['id']}")
            return True
    else:
        print(f"Usuário não encontrado!!")
        return False

def deletar_usuario_por_nome(user:str):
    global usuarios
    for usuario in usuarios:
        usuario_nome = user.rstrip().lstrip().split(" ")
        usuario_capitalizado = []
        for x in usuario_nome:
            usuario_capitalizado.append(x.capitalize())
        usuario_nome = ' '.join(usuario_capitalizado)
        if usuario["nome"] == usuario_nome:
            deletar_usuario_por_id(usuario['id'])
            return True
    else:
        print('Usuario não encontrado!!')
        return False

def deletar_usuario_por_id(id_buscador: int):
    global cursor, usuarios, conexao
    for usuario in usuarios:
        if id_buscador == usuario['id']:
            escolha = input('Tem certeza que quer apagar o usuário?? s/n ').lower().rstrip().lstrip()
            if escolha == 's':
                cursor.execute("DELETE FROM usuario WHERE id = %s", (usuario['id'],))
                conexao.commit()
                cursor.execute("SELECT * FROM usuario")
                usuarios = cursor.fetchall()
                print(f"Usuário {usuario['nome']} deletado!")
                return
            elif escolha == 'n':
                print(f'Operação cancelada!!')
                return
            else:
                print(f'Valor invalido!! \n Operação cancelada!!')
                return

    else:
        print(f"Usuário não encontrado!!")
        return

def atualizar_usuario(user: str):
    global usuarios
    for usuario in usuarios:
        if user in usuario['nome']:
            escolha = input('Deseja realmente mudar o nome de usuário? s/n\n').lower().rstrip().lstrip()
            if escolha == 's':
                novo_nome = input('Digite o novo nome: ').split(' ')
                novo_nome_capitalizado = []
                if novo_nome != " ":
                    for x in novo_nome:
                        novo_nome_capitalizado.append(x.capitalize())
                    novo_nome = ' '.join(novo_nome_capitalizado)
                    cursor.execute("UPDATE usuario SET nome = %s WHERE id = %s", (novo_nome, usuario['id']))
                    conexao.commit()
                    cursor.execute("SELECT * FROM usuario")
                    usuarios = cursor.fetchall()
                    print(f'Usuário {user} mudado para {novo_nome}')
                    return True
                else:
                    print('Não aceitamos nomes nulos')
                    return atualizar_usuario(user)
            elif escolha == "n":
                print("Operação cancelada!!")
                return False
            else:
                print(f'Valor invalido!! \nOperação cancelada!!')
                return False

def atualizar_usuario_por_id(id_buscador: int):
    global usuarios
    for usuario in usuarios:
        if id_buscador == usuario["id"]:
            atualizar_usuario(usuario['nome'])
            return "Nome atualizado com sucesso!"
    else:
        return 'Usuário não encontrado!!'



pegar_usuario_por_nome(input("Entre com o nome"))