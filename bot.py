import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

# Carrega variáveis do .env (funciona no Render se as variáveis forem definidas no painel)
load_dotenv()

TOKEN = os.getenv("TOKEN")
print("TOKEN carregado:", TOKEN)

# Lista de frases quando há infectado
frases_infectadas = [
    "Um estalo ecoa pela floresta... algo está se movendo por perto.",
    "O cheiro de sangue fresco é atrativo para os infectados. Você não está mais sozinho.",
    "Galhos quebrados, passos arrastados... eles estão vindo...Mas quantos?",
    "Se arrastando pelo local, um infectado aparece no seu campo de visão, por sorte, ele esta sozinho",
    "Um silêncio foi rasgado por um rugido gutural. Prepare-se!",
    "Respirações aceleradas, seguidas por grunhidos, estão cada vez mais próximas.",
    "Algo corre pelas paredes, infectados estão no encalço!",
    "A neblina se move estranhamente. Um infectado se esgueira no breu.",
    "Barulhos de garras raspando... Eles estão vindo."
    "Shhh... Você ouviu isso? Tem um Estalador por perto."
    "Não faça barulho. Qualquer som e eles vêm correndo."
    "Tem fungo fresco no ar... eles passaram por aqui há pouco."
    "Esse barulho... não é vento. É coisa pior."
    "Olha ali... contorce igual um Estalador. Não se mexe!"
    "Baiacu detectado! Se ele estourar, já era!"
    "Tem alguma coisa se arrastando ali... o barulho é irregular, como se os pés mal tocassem o chão. Se for um Estalador, a gente vai saber pelo som."
    "O ar ficou pesado... aquele cheiro podre, úmido. Isso sempre vem antes de um Corredor aparecer. Eles sentem a gente mesmo sem ver."
    "Algo grande acabou de passar entre as sombras. Os fungos cobriam quase tudo no corpo dele. Aquilo não se move como um humano faz."
    "Silêncio total... por alguns segundos, até começar aquele clique repetitivo. Baixo, insistente. Se tem um Estalador por perto, os outros não estão longe."
    "Um grunhido baixo, abafado... depois o estalo. Não precisa ver pra saber que tem Estalador se aproximando, e ele não tá sozinho."
    "A névoa dos esporos tá densa. Tá difícil respirar. Isso só acontece quando aqueles desgraçados grandes aparecem... os que demoram anos pra virar o que são."
    O silêncio é estranho demais. Infectados comuns não sabem se esconder assim. Ou tem algo diferente por perto... ou alguém."
    "Olhos brilham no escuro por um segundo. Rápidos. Focados. Não era só fome... era estratégia. Talvez um híbrido."
    "Tem pegadas recentes, mas espaçadas, leves... como se estivesse te seguindo sem querer ser notado. Isso é típico de híbrido."    
]

# Gatilhos que ativam a resposta
gatilhos = [
    "infectado", "caçar", "algo", "grunhido", "sangue", "neblina", "grito", "passos", "escuridão",
    "correr", "esconderijo", "zumbi", "rugido", "pavor", "sombra", "barulho", "rastejar", "eco", 
    "arranhar", "batida", "pânico", "fedor", "desespero", "sussurro", "movimento", "estripar", "vítima",
    "respirar", "algo estranho", "arranhão", "estalou", "gritou", "pulou", "correu", "explosão", "manada",
    "bomba", "terror", "tiros", "gritando", "atirando"
]

# Função que verifica se a mensagem deve gerar uma resposta
async def verifica_mensagem(update: Update, context):
    mensagem = update.message.text.lower()

    # 50% chance de resposta (bot ativo) e 50% chance de ficar em silêncio
    if random.random() < 0.5:  # 50% de chance para ser ativo
        if any(gatilho in mensagem for gatilho in gatilhos):
            frase = random.choice(frases_infectadas)
            await update.message.reply_text(frase)

# Iniciar o bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, verifica_mensagem))

    print("Bot rodando... esperando jogadores!")
    app.run_polling()
