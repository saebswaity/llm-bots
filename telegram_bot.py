
import telebot
from session import Session

class TelegramBot:
    def __init__(self, token, llm):
        self.bot = telebot.TeleBot(token)
        self.llm = llm
        self.sessions = {}
        self._register_handlers()

    def _register_handlers(self):
        self.bot.message_handler(commands=['start'])(self.start)
        self.bot.message_handler(func=lambda message: True)(self.handle_message)

    def start(self, message):
        user_id = message.from_user.id
        if user_id not in self.sessions:
            self.sessions[user_id] = Session(self.llm)
        self.bot.reply_to(message, "Hello! I'm ready to chat. Send me a message!")

    def handle_message(self, message):
        user_id = message.from_user.id
        if user_id not in self.sessions:
            self.sessions[user_id] = Session(self.llm)
        
        session = self.sessions[user_id]
        user_message = message.text
        response = session.get_response(user_message)
        self.bot.reply_to(message, response)

    def run(self):
        self.bot.polling()
