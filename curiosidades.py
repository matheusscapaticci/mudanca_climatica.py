import random
import time

def curiosidades():
    print("Bem vindo a seção de curiosidades sobre a mudança climática")
    time.sleep(2)

    print("Para você ter mais curiosidades atualize a página do site")
    time.sleep(2)

    lista = [
        "O planeta está ficando cada vez mais quente.",
        "As geleiras estão derretendo por causa do calor.",
        "O calor pode prejudicar a saúde das pessoas.",
        "Muitos animais estão perdendo suas casas por causa das mudanças no clima.",
        "O desmatamento aumenta o aquecimento global.",
        "O aumento do calor pode causar secas.",
        "Os oceanos estão ficando mais quentes.",
        "As tartarugas marinhas podem ser afetadas pelo calor dos oceanos.",
        "Plantar árvores ajuda a cuidar do planeta.",
        "O desperdício de água pode piorar em tempos de seca.",
        "O calor pode prejudicar as plantações.",
        "O aumento do nível do mar pode ameaçar cidades perto das praias.",
        "As florestas ajudam a retirar gás carbônico do ar.",
        "As ondas de calor podem durar vários dias.",
        "A queima de combustíveis libera gases que aquecem o planeta."
    ]

    curiosidade = random.choice(lista)

    print("Curiosidade: " + curiosidade)

    time.sleep(5)
