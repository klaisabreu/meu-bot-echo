import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

print("Diretório atual:", os.getcwd())
print(".env existe?", os.path.isfile(".env"))

# Corrigido: caminho completo pro .env
load_dotenv(dotenv_path="/storage/emulated/0/Android/data/ru.iiec.pydroid3/files/.env")

TOKEN = os.getenv("TOKEN")
print("TOKEN carregado:", TOKEN)

# Lista de frases quando há infectados
infectados_frases = [
    "- Um estalo ecoa pela floresta... algo está se movendo por perto.",
    "- O cheiro de sangue fresco no ar atraiu infectados. Você não está mais sozinho.",
    "- Galhos quebrados, passos arrastados... eles estão vindo.",
    "- De trás dos escombros, uma sombra grotesca se levanta.",
    "- O silêncio foi rasgado por um rugido gutural. Prepare-se!",
    "- Você escuta respirações aceleradas, seguidas por grunhidos cada vez mais próximos.",
    "- Algo corre pelas paredes, infectados estão no encalço!",
    "- A neblina se move estranhamente. Um infectado se esgueira no breu.",
    "- Barulhos de garras raspando... Eles estão próximos."
]

# Gatilhos que ativam a chance de frase
gatilhos = [
    "infectado", "caçar", "som", "grunhido", "sangue", "neblina", "grito", "passos",
    "escuridão", "floresta", "correndo", "esconderijo", "zumbi", "rugido", "pavor", "sombra",
    "barulho", "rastejar", "eco", "arranhar", "batida", "pânico", "fedor", "desespero",
    "medo", "cheiro", "latido", "vulto", "espreita", "som estranho", "arranhão"
]

# Função principal que verifica a mensagem
async def verifica_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    if any(palavra in texto for palavra in gatilhos):
        chance = random.randint(1, 100)
        if chance <= 40:
            frase = random.choice(infectados_frases)
            await update.message.reply_text(frase)

# Inicia o bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), verifica_mensagem))
    print("Bot rodando... esperando jogadores!")
    app.run_polling()
