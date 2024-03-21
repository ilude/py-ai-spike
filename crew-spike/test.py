from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from utils import read_messages, read_prompt

prompt_text = read_prompt('prompt.txt')
messages = read_messages('messages.txt')

_prompt = ChatPromptTemplate.from_messages([
    ("system", prompt_text),
    ("human", "{text}"),
])

_model = Ollama(base_url='https://ollama.traefikturkey.icu', model="dolphin-mistral", keep_alive=5) # dolphin-mistral

chain = _prompt | _model

for message in messages:
  message['rating'] = float(chain.invoke({"text": message['content']}).strip())

messages = sorted(messages, key=lambda message: message['rating'])

for message in messages:
  print(f"Rating: {message['rating']: <4} Classified: {message['type']: <5} Message: {message['content'][:70]}... ")
