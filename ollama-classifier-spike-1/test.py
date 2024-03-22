import os
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from utils import read_messages, read_prompt

load_dotenv() 

prompt_text = read_prompt('prompt.txt')
messages = read_messages('messages.txt')

_prompt = ChatPromptTemplate.from_messages([
    ("system", prompt_text),
    ("human", "{text}"),
])

ollama_url = os.getenv('OLLAMA_URL', 'https://ollama.traefikturkey.icu')

_model = Ollama(base_url=ollama_url , model="dolphin-mistral", keep_alive=5)

chain = _prompt | _model

for message in messages:
  message['rating'] = float(chain.invoke({"text": message['content']}).strip())

messages = sorted(messages, key=lambda message: message['rating'])

for message in messages:
  print(f"Rating: {message['rating']: <4} Classified: {message['type']: <5} Message: {message['content'][:70]}... ")
