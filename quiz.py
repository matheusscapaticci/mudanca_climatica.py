import time

def quiz():
    print("Bem-vindo ao quiz!")

    pontos = 0

    quiz_start = input("Digite Sim para começar o quiz ou Não para sair: ")

    if quiz_start == "Sim":
        print("Vamos começar o quiz antes algumas instruções:")
        print("Será feito 5 perguntas sobre mudanças climáticas, cada pergunta vale 1 ponto.")
        print("Escrever a primeira palvra em maiusculo e colocar acentuação se precisar.")
        time.sleep(6)
        print("1. São alterações nos padrões do clima da Terra ao longo do tempo. O que é?")
        resposta = input("Digite sua resposta: ")

        if resposta == "Mudança climática" or resposta == "Mudanças climáticas":
            print("Parabéns, você acertou!")
            pontos += 1
        else:
            print("Você errou! A resposta era Mudança climática ou Mudanças climáticas.")

        time.sleep(2)
        print("2. Qual é o principal responsável pelo aquecimento global atualmente?")
        resposta = input("Digite sua resposta: ")

        if resposta == "Ser humano":
            print("Muito bem! Você acertou!")
            pontos += 1
        else:
            print("Você errou! A resposta era Ser humano.")

        time.sleep(2)
        print("3. Qual gás contribui para o efeito estufa?")
        resposta = input("Digite sua resposta: ")

        if resposta == "Gás carbônico":
            print("Parabéns, você acertou!")
            pontos += 1
        else:
            print("Você errou! A resposta era Gás carbônico.")

        time.sleep(2)
        print("4. O desmatamento contribui para as mudanças climáticas?")
        resposta = input("Digite sua resposta: ")

        if resposta == "Sim":
            print("Isso mesmo!")
            pontos += 1
        else:
            print("Você errou! A resposta era Sim.")

        time.sleep(2)
        print("5. Qual fenômeno causa o aumento da temperatura média da Terra?")
        resposta = input("Digite sua resposta: ")

        if resposta == "Aquecimento global":
            print("Parabéns, você acertou!")
            pontos += 1
        else:
            print("Você errou! A resposta era Aquecimento global.")

        print("Fim do quiz!")
        print("Sua pontuação foi:", pontos, "de 5")

        if pontos == 5:
            print("Parabéns! Você acertou todas!")
        elif pontos >= 3:
            print("Muito bem! Você foi muito bem!")
        else:
            print("Continue estudando! Você consegue!")

    elif quiz_start == "Não":
        print("Saindo do quiz")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Carregando menu...")
        time.sleep(2)

    else:
        print("Essa opção não existe!")
