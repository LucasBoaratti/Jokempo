import random #Importando a biblioteca random

def jokempo(): #Criando a função para o jogo
    print("Seja bem-vindo(a) ao jokempô! Aqui você terá que vencer o computador em uma batalha de pedra, papel e tesoura.\n") #Exibindo a mensagem de boas vindas na tela/terminal
    
    print("Jogo criado por: Lucas Henrique Boaratti Silva.\n") #Exibindo a mensagem do criador do jogo na tela/terminal

    print("Lembrete: as opções de escolha são: 1 - pedra, 2 - papel e 3 - tesoura.") #Exibindo as opções de escolha na tela

    opcoesEscolha = { #Criando um dicionário para as opções de escolha
        1: "Pedra",
        2: "Papel",
        3: "Tesoura",
    }

    pontosUsuario = 0 #Armazenando o valor 0 para a variável pontosUsuario
    
    pontosComputador = 0 #Armazenando o valor 0 para a variável pontosComputador

    while True: #Laço de repetição para jogar o jogo até o usuário parar
        try: #Tentativa de executar o código do jogo
            escolhaUsuario = input("\nDigite a sua escolha (caso queira parar o jogo, digite 0): ") #O usuário vai fazer a escolha dele
            escolhaUsuario = int(escolhaUsuario) #Transformando a variável escolhaUsuario em inteiro

            if escolhaUsuario == 0: #Verificando se o usuário escolheu o número 0
                print("\nSaindo do jogo... Obrigado(a) por jogar!") #Exibindo a mensagem de agradecimento na tela/terminal   
                break #Parando o programa
            
            if escolhaUsuario not in opcoesEscolha: #Verificando se o usuário escolheu uma opção inválida
                print("Selecione uma opção válida!") #Exibindo a mensagem de aviso na tela/terminal
                continue #Continuando o programa

            escolhaComputador = random.randint(1, 3) #O computador vai escolher um número aleatório para a sua jogada 

            print(f"\nSua escolha: {opcoesEscolha[escolhaUsuario]}.\n") #Exibindo a escolha do usuário na tela/terminal

            print(f"Escolha do computador: {opcoesEscolha[escolhaComputador]}.\n") #Exibindo a escolha do computador na tela/terminal

            if escolhaUsuario == escolhaComputador: #Verificando se a escolha do usuário foi igual a escolha do computador
                print("Jogo empatado!\n") #Exibindo a mensagem de empate na tela/terminal
            elif (escolhaUsuario == 1 and escolhaComputador == 3) or (escolhaUsuario == 2 and escolhaComputador == 1) or (escolhaUsuario == 3 and escolhaComputador == 2): #Verificando se o usuário escolheu todas as possibilidades de vencer o computador
                print("Parabéns, você venceu!\n") #Exibindo a mensagem de parabenização na tela/terminal
                
                pontosUsuario += 1 #Aumentando o placar do usuário
            else: #Caso as opções acima sejam favoráveis para o computador...
                print("Ops, você perdeu.\n") #Exibindo a mensagem de derrota na tela/terminal
 
                pontosComputador += 1 #Aumentando o placar do computador

            print(f"Placar: Usuário {pontosUsuario} X {pontosComputador} Computador.") #Exibindo o placar na tela/terminal

            if pontosUsuario == 15:
                print("\nParabéns. Você é o vencedor do jokempô!!! 🥳")
                print(f"\nPlacar final: Usuário {pontosUsuario} X {pontosComputador} Computador.")
            elif pontosComputador == 15:
                print("\nQue pena, você perdeu! ☹️")
                print(f"\nPlacar final: Usuário {pontosUsuario} X {pontosComputador} Computador.")

        except ValueError: #Caso o usuário digite um valor errado...
            print("\nInsira apenas números inteiros!") #Exibindo a mensagem de aviso na tela/terminal

jokempo() #Executando a função 