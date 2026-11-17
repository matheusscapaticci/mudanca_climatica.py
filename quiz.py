import time

def quiz():
    print("Bem-vindo ao quiz!")

    quiz_start = input("Digite Sim para começar o quiz ou Não para sair:")

    if quiz_start == "Sim":
        print("Vamos começar o quiz")
    elif quiz_start == "Não":
        print("saindo do quiz")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Carregando menu...")
        time.sleep(2)
    else:
        print("Essa opção não existe")
