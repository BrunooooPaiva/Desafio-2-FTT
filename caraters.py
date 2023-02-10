while True:
    nome_personagem = input('Nome do personagem: ')
    descricao_personagem = input('Descrição do personagem: ')
    link_imagem_personagem = input('Link da imagem do personagem: ')
    programa_personagem = input('Programa do personagem: ')
    animador_personagem = input('Animador do personagem: ')

    with open('save_caraters.txt', 'a', encoding='UTF-8') as arquivo:
        lista = [nome_personagem,'|' , descricao_personagem,'|', link_imagem_personagem,'|', programa_personagem,'|', animador_personagem]
        for valor in lista:
            arquivo.write(str(valor))
        arquivo.write('\n')


    mostrar = input(str('Deseja ver informações de algum dos personagens [sim/s ou não/n]?  ')).lower()

    if mostrar == 'sim' or mostrar == 's':
        r_sim = input(str('Qual personagem você quer buscar as informações? '))
        with open('save_caraters.txt', 'r', encoding='UTF-8') as arquivo:
            mensagem = arquivo.readlines()

        for linha in mensagem:
            if r_sim in linha:
                print(linha)
        continuar = input(str('Deseja continuar [sim/s ou não/n]?  ')).lower()
        if continuar == 'sim' or continuar == 's':
            continue
        else:
            break
    else:
        break