import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Enzoregigui12#",
    database = "bd_crud"
)

cursor = conexao.cursor(dictionary=True)

cursor.execute("SELECT * FROM usuario")
usuarios = cursor.fetchall()




def criar_usuario(new_user:str):
    global usuarios
    for usuario in usuarios:
        if new_user in usuario:
            print("Usuario já existe")
        return
    else:
        user = (new_user, )
        cursor.execute("INSERT INTO usuario (nome) VALUES (%s)", user)
        conexao.commit()
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()

def pegar_usuario_por_nome(user: str):
    for usuario in usuarios:
        if user in usuario["nome"]:
            print(f"Usuario encontrado \n{user}")
        else:
            print(f"Usuario inexistente!!")
        return None
    return None


def pegar_usuarios():
    for usuario in usuarios:
        print(f"Usuario {usuario['nome']}: id {usuario['id']}")
    return

def pegar_usuario_por_id(id_buscador:int):
    for usuario in usuarios:
        if id_buscador == usuario['id']:
            print(f"Usuário encontrado \nUsuário = {usuario['nome']} : ID = {usuario['id']}")
            return
    else:
        print(f"Usuário não encontrado!!")
        return

def deletar_usuario_por_nome(user:str):
    for usuario in usuarios:
        if user in usuario['nome']:
            escolha = input('Tem certeza que quer apagar o usuário?? s/n ').lower()
            if escolha == 's':
                del usuarios[user]
                print(f'Usuário {user} deletado!')
                return
            elif escolha == 'n':
                print(f'Operação cancelada!!')
                return
            else:
               print(f'Valor invalido!! \n Operação cancelada!!')
               return

def deletar_usuario_por_id(id_buscador: int):
    for user, id_user in usuarios.items():
        if id_buscador == id_user:
            deletar_usuario_por_nome(user)
    else:
        print(f"Usuário não encontrado!!")
        return

def atualizar_usuario(user: str):
    for usuario in usuarios:
        usuario_teste = usuario['nome']
        if user in usuario_teste:
            escolha = input('Deseja realmente mudar o nome de usuário? ')
            if escolha == 's' or escolha == 'S':
                novo_nome = input('Digite o novo nome: ')
                print(f'Usuário {user} mudado para {novo_nome}')
            elif escolha == 'N' or escolha == 'n':
                print('Operação cancelada!!')
            else:
                print(f'Valor invalido!! \n Operação cancelada!!')

def atualizar_usuario_por_id(id_buscador: int):
    for user, id_user in usuarios.items():
        if id_buscador == id_user:
            atualizar_usuario(user)
    else:
        print('Usuário não encontrado!!')


#criar_usuario('Pedro')
pegar_usuarios()
pegar_usuario_por_id(20)
pegar_usuario_por_nome('Pedro')
