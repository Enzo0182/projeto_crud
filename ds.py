import random as rd

usuarios = {}
def criar_usuario(new_user:str):


	if new_user in usuarios:
		print("Usuario já existe")
	else:
		while True:
			id_user = rd.randint(0, 10000)
			if id_user not in usuarios.values():
				usuarios[new_user] = id_user
				print(f"Usuario criado \nUsuário {new_user}: id {usuarios[new_user]} ")
				return
			else:
				continue


def pegar_usuario_por_nome(user: str):
	if user in usuarios.keys():
		print(f"Usuario encontrado \n{user}")
	else:
		print(f"Usuario inexistente!!")
	return None

def pegar_usuarios():
	for user, id_user in usuarios.items():
		print(f"\nUsuario {user}: id {id_user}")
	return

def pegar_usuario_por_id(id_buscador:int):
	for user, id_user1 in usuarios.items():
		if id_buscador == id_user1:
			print(f"Usuário encontrado \nUsuário = {user} : ID = {id_user1}")
			return
	else:
		print(f"Usuário não encontrado!!")
		return

def deletar_usuario_por_nome(user:str):
	if user in usuarios.keys():
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
	if user in usuarios:
		escolha = input('Deseja realmente mudar o nome de usuário? ')
		if escolha == 's' or escolha == 'S':
			novo_nome = input('Digite o novo nome de usuario: ')
			usuarios[novo_nome] = usuarios.pop(user)
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


criar_usuario('Enzo')
pegar_usuarios()
pegar_usuario_por_nome('Enzo')
pegar_usuario_por_id(int(input('')))
#deletar_usuario_por_nome('Enzo')
#deletar_usuario_por_id(int(input()))
