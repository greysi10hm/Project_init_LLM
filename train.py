import os
import openai
import tiktoken

#Dati 
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

#Creazione e addestramento
openai.api_key  = os.environ['OPENAI_API_KEY']

#test del modello addestrato