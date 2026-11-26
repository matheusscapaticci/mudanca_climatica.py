from flask import Flask, render_template, jsonify, request, session
from curiosidades import curiosidades
from dicas import dicas
from quiz import perguntas, verificar_resposta

app = Flask(__name__)

app.secret_key = "chave-do-projeto-clima"


# PÁGINA INICIAL
@app.route("/")
def inicio():
    return render_template("index.html")


# CURIOSIDADES
@app.route("/api/curiosidades")
def mostrar_curiosidades():
    resultado = curiosidades()

    return jsonify({
        "resultado": resultado
    })


# DICAS AMBIENTAIS
@app.route("/api/dicas")
def mostrar_dicas():
    resultado = dicas()

    return jsonify({
        "resultado": resultado
    })


# INICIAR QUIZ
@app.route("/api/quiz/iniciar", methods=["POST"])
def iniciar_quiz():
    session["pergunta_atual"] = 0
    session["pontos"] = 0

    return jsonify({
        "pergunta": perguntas[0]["pergunta"],
        "numero": 1,
        "total": len(perguntas)
    })


# PRÓXIMA PERGUNTA
@app.route("/api/quiz/proxima")
def proxima_pergunta():
    if "pergunta_atual" not in session:
        return jsonify({
            "erro": "Quiz não iniciado."
        }), 400

    indice = session["pergunta_atual"]

    return jsonify({
        "pergunta": perguntas[indice]["pergunta"],
        "numero": indice + 1,
        "total": len(perguntas)
    })


# RESPONDER QUIZ
@app.route("/api/quiz/responder", methods=["POST"])
def responder_quiz():

    if "pergunta_atual" not in session:
        return jsonify({
            "erro": "Inicie o quiz primeiro."
        }), 400

    dados = request.get_json(silent=True) or {}
    resposta = dados.get("resposta", "")

    if not isinstance(resposta, str) or not resposta.strip():
        return jsonify({
            "erro": "Digite uma resposta."
        }), 400

    indice = session["pergunta_atual"]

    if indice >= len(perguntas):
        return jsonify({
            "erro": "O quiz já foi finalizado."
        }), 400

    pergunta = perguntas[indice]

    acertou = verificar_resposta(
        resposta,
        pergunta["respostas"]
    )

    if acertou:
        session["pontos"] += 1

    resultado = {
        "acertou": acertou,
        "resposta_correta": pergunta["respostas"][0]
    }

    indice += 1
    session["pergunta_atual"] = indice

    if indice >= len(perguntas):

        pontos = session["pontos"]

        resultado["finalizado"] = True
        resultado["pontos"] = pontos
        resultado["total"] = len(perguntas)

        if pontos == 5:
            resultado["mensagem"] = "Parabéns, Você acertou todas as perguntas."

        elif pontos >= 3:
            resultado["mensagem"] = "Muito bem, Você teve um bom resultado."

        else:
            resultado["mensagem"] = "Continue estudando, Você consegue."

        session.pop("pergunta_atual", None)
        session.pop("pontos", None)

    else:

        resultado["finalizado"] = False
        resultado["proxima_pergunta"] = perguntas[indice]["pergunta"]
        resultado["numero"] = indice + 1

    return jsonify(resultado)


# INICIAR SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)

    time.sleep(2)
    print("Até mais tarde!")
else:
    print("Opção não existe")
