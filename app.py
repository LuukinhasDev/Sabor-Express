import os

restaurantes = [{'nome': 'Outback', 'categoria': 'Australiana', 'ativo': True}, 
                {'nome': 'Sushi Bar', 'categoria': 'Japonesa', 'ativo': True},
                {'nome': 'Mamamia', 'categoria': 'italiana', 'ativo': False}]

def exibir_nome_do_jogo ():
    ''' Essa função é responsável por exibir o nome do jogo '''
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n''')
       
def exibir_opcoes():
    ''' Essa função é responsável por exibir as opções '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Aternar Estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Essa função é responsável por finalizar o app '''
    exibir_subtitulo('App finalizado com sucesso!')

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal '''
    input(f'\n Digite uma tecla qualquer para voltar ao menu ')
    main() 

def opcao_invalida():
    ''' Essa função é responsável por exibir opção inválida '''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Essa função é responsável por exibir os subtitulos '''
    os.system('cls')
    linha = '*' * (len(texto))
    print (linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''

    exibir_subtitulo('Cᴀᴅᴀsᴛʀᴏ ᴅᴇ ɴᴏᴠᴏs ʀᴇsᴛᴀᴜʀᴀɴᴛᴇs')
    nome_do_restaurante = input('Digite o nome do restaurante para cadastrá-lo: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista restaurantes presentes na lista de restaurantes '''

    exibir_subtitulo('Rᴇsᴛᴀᴜʀᴀɴᴛᴇs Lɪsᴛᴀᴅᴏs')
    print(f"{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}")
    print('-' * 59)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    ''' Essa função aterna o estado ativo/desativado de um restaurante '''

    exibir_subtitulo('Aʟᴛᴇʀɴᴀɴᴅᴏ Esᴛᴀᴅᴏ ᴅᴏ Rᴇsᴛᴀᴜʀᴀɴᴛᴇ')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restautante in restaurantes:
        if nome_restaurante == restautante['nome']:
            restaurante_encontrado = True
            restautante['ativo'] = not restautante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restautante['ativo'] else f'O restaurante {nome_restaurante}foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'\nRestaurante {nome_restaurante} não encontrado!')

    voltar_ao_menu_principal()
    
def escolher_opcao(): 
    ''' Essa função é responsável por solicitar e executar a opção escolhida pelo usuário '''
    try:
        opcao_escolhida = int(input('Escolha uma das opções: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2: 
                listar_restaurantes()
            case 3:
                alternar_estado_do_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
   
def main(): # função principal que vai ser executada ao rodar o programa, e a ordem em que cada função vai ocorrer
    ''' Essa é a função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_jogo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': # define esse arquivo como principal e executa a função principal
    main()