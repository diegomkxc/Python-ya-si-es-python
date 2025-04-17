from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from sqlalchemy import create_engine

# Crear un chatbot con SQL
chatbot = ChatBot(
    "AsistenteVirtual",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3"
)

# Entrenar el chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish")
