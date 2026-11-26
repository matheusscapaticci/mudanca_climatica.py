import random
import time

def dicas():
    print("Dicas para ajudar a conter a mudança climática:")
    time.sleep(2)

    lista = [
        "Economize energia elétrica.",
        "Evite o desperdício de água.",
        "Proteja os animais e seus habitats.",
        "Não jogue lixo nas ruas e praias.",
        "Plante árvores.",
        "Evite queimadas e desmatamento.",
        "Separe o lixo para reciclagem.",
        "Reduza o uso de plástico.",
        "Evite desperdiçar alimentos.",
        "Preserve as florestas.",
        "Use bicicleta quando possível.",
        "Prefira transporte público.",
        "Cuide das praias e dos oceanos.",
        "Economize água durante o banho.",
        "Apague as luzes ao sair do cômodo."
    ]
        
    dicas = random.choice(lista)
    print("Dica: " + dicas)    
    
    time.sleep(5)
