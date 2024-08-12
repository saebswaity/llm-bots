from llm import TitanLLM,CohereCommandLLM
from telegram_bot import TelegramBot

def main():
    #llm = TitanLLM()
    llm = CohereCommandLLM()
    bot = TelegramBot("YOURTOKEN", llm)
    bot.run()

if __name__ == "__main__":
    main()