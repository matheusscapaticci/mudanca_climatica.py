
import unicodedata


perguntas = [
    {
        "pergunta": "São alterações nos padrões do clima da Terra ao longo do tempo. O que é?",
        "respostas": ["Mudança climática", "Mudanças climáticas"]
    },
    {
        "pergunta": "Qual é o principal responsável pelo aquecimento global atualmente?",
        "respostas": ["Ser humano", "Atividades humanas"]
    },
    {
        "pergunta": "Qual gás contribui para o efeito estufa?",
        "respostas": ["Gás carbônico", "Dióxido de carbono", "CO2"]
    },
    {
        "pergunta": "O desmatamento contribui para as mudanças climáticas?",
        "respostas": ["Sim"]
    },
    {
        "pergunta": "Qual fenômeno causa o aumento da temperatura média da Terra?",
        "respostas": ["Aquecimento global"]
    }
]


def normalizar(texto):
    texto = texto.strip().lower()

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        letra for letra in texto
        if unicodedata.category(letra) != "Mn"
    )

    return texto


def verificar_resposta(resposta, respostas_corretas):
    resposta = normalizar(resposta)

    return any(
        resposta == normalizar(correta)
        for correta in respostas_corretas
    )
