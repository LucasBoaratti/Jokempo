import random 

# Função do jogo
def jokempo(): 
    print("Seja bem-vindo(a) ao jokempô! Aqui você terá que vencer o computador em uma batalha de pedra, papel e tesoura.\n") 
    print("Jogo criado por: Lucas Boaratti\n") 

    nome = input("Digite seu nome para começar a jogar: ")
    print(f"Seja bem vindo(a), {nome}! Suas opções de escolha são: 1 - pedra, 2 - papel e 3 - tesoura.") 

    # Opções de escolha clássicas do Jokempô
    opcoesEscolha = { 
        1: "Pedra",
        2: "Papel",
        3: "Tesoura",
    }

    pontosUsuario = 0 
    pontosComputador = 0 

    while True: 
        try: 
            escolhaUsuario = input("\nDigite a sua escolha (caso queira parar o jogo, digite 0): ") 
            escolhaUsuario = int(escolhaUsuario) 

            if escolhaUsuario == 0: 
                print("\nSaindo do jogo... Obrigado(a) por jogar!") 
                break 
            
            # Verifica se o usuário escolher uma opção inválida
            if escolhaUsuario not in opcoesEscolha: 
                print("\nSelecione uma opção válida!") 
                continue 

            escolhaComputador = random.randint(1, 3) 
            
            # Exibe as escolhas de cada um dos competidores
            print(f"Sua escolha: {opcoesEscolha[escolhaUsuario]}.") 
            print(f"Escolha do computador: {opcoesEscolha[escolhaComputador]}.") 

            # Verificações de pontuação
            if escolhaUsuario == escolhaComputador: 
                print("Jogo empatado!") 
            elif (escolhaUsuario == 1 and escolhaComputador == 3) or (escolhaUsuario == 2 and escolhaComputador == 1) or (escolhaUsuario == 3 and escolhaComputador == 2): 
                print(f"Ponto pro(a) {nome}!") 

                pontosUsuario += 1 
            else: 
                print("Ponto pro Computador!") 
 
                pontosComputador += 1 

            print(f"\nPlacar: Usuário {pontosUsuario} X {pontosComputador} Computador.") 

            # Verificações de placares para cada um dos competidores
            if pontosUsuario == 15: 
                print("\nParabéns! Você é o vencedor do jokempô!!! 🥳")
                print(f"\nPlacar final: {nome} {pontosUsuario} X {pontosComputador} Computador.")
                break
            elif pontosComputador == 15:
                print("\nQue pena, você perdeu! Tente novamente. ☹️")
                print(f"\nPlacar final: {nome} {pontosUsuario} X {pontosComputador} Computador.")
                break

        except ValueError: #Caso o usuário digite um valor errado...
            print("\nInsira apenas números inteiros!") 

jokempo() #Executando a função 