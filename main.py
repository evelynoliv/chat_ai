import openai
import dotenv

API_KEY = ;
openai.api_key = API_KEY
model = 'text-davinci-003'

question = str(input('ask and you shall receive: '))

response = openai.Completion.create(
prompt = question,
max_tokens = 800,
model = model,
temperature = 0.8,

)

print(response['choices'][0]['text'])   