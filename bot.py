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
    "Um estalo ecológico pela floresta... algo está se movendo por perto.",
    "O cheiro de sangue fresco não é atrativo para infectados. Você não está mais sozinho.",
    "Galhos quebrados, passos arrastados... eles estão vindo.",
    "De trás dos escombros, uma sombra grotesca se levanta.",
    "Um silêncio foi rasgado por um rugido gutural. Prepare-se!",
    "Com suas respirações aceleradas, seguidas por grunhidos cada vez mais próximos.",
    "Algo corre pelas paredes, infectados estão no encalço!",
    "A neblina se move estranhamente. Um infectado se esgueira no breu.",
    "Barulhos de garras raspando... Eles estão vindo."
]

# Gatilhos que ativam a resposta
gatilhos = [
    "infectado", "caçar", "algo", "grunhido", "sangue", "neblina", "grito", "passos", "escuridão",
    "correr", "esconderijo", "zumbi", "rugido", "pavor", "sombra", "barulho", "rastejar", "eco", 
    "arranhar", "batida", "pânico", "fedor", "desespero", "sussurro", "movimento", "estripar", "vítima",
    "respirar", "algo estranho", "arranhão"
]

# Função que verifica se a mensagem deve gerar uma resposta
async def verifica_mensagem(update: Update, context):
    mensagem = update.message.text.lower()
    
    # 40% chance de resposta (bot ativo) e 60% chance de ficar em silêncio
    if random.random() < 0.4:  # 40% de chance para ser ativo
        if any(gatilgo in mensagem for gatilho in gatilhos):
            frase = random.choice(frases_infectadas)
            await update.message.reply_text(frase)

# Iniciar o bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, verifica_mensagem))

    print("Bot rodando... esperando jogadores!")
    app.run_polling()
