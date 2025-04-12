import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Seu token do BotFather
TOKEN = '8008443177:AAHxgKFtWKHeRuug6qk5vciKzITHuT94C80'

# Lista de frases quando há infectados
infectados_frases = [
    "— Um estalo ecoa pela floresta... algo está se movendo por perto.",
    "— O cheiro de sangue fresco no ar atraiu infectados. Você não está mais sozinho.",
    "— Galhos quebrados, passos arrastados... eles estão vindo.",
    "— De trás dos escombros, uma sombra grotesca se levanta.",
    "— O silêncio foi rasgado por um rugido gutural. Prepare-se!",
    "— Você escuta respirações aceleradas, seguidas por grunhidos cada vez mais próximos.",
    "— Algo corre pelas paredes, infectados estão no encalço!",
    "— A neblina se move estranhamente. Um infectado se esgueira no breu.",
    "— Barulhos de garras raspando em pedra. Eles estão próximos.",
    "— O som de carne se arrastando faz sua pele arrepiar. Há algo por perto."
]

# Palavras-chave que ativam o sistema
gatilhos = ["andar", "explorar", "procurar", "caminhar", "vasculhar", "investigar", "correr", "entrar", "sair"]

async def verifica_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if any(palavra in texto for palavra in gatilhos):
        chance = random.randint(1, 100)  # Gera número de 1 a 100

        if chance <= 40:
            frase = random.choice(infectados_frases)
            await update.message.reply_text(frase)
        else:
            # 60% de chance de silêncio
            pass

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Captura todas as mensagens no grupo
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), verifica_mensagem))

    print("Bot rodando... esperando jogadores!")
    app.run_polling()
