from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# Configure the chatbot to use MySQL on PythonAnywhere
english_bot = ChatBot(
    'Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='mysql+pymysql://Mathew002:Sqlrithik@002@Mathew002.mysql.pythonanywhere-services.com/Mathew002$2chatbotdb'
)

# Use ListTrainer
trainer = ListTrainer(english_bot)

# Train using your data files
for file in os.listdir('data'):
    print('Training using ' + file)
    convData = open('data/' + file, encoding="utf-8").readlines()
    trainer.train(convData)
    print("Training completed for " + file)
