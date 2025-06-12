from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os
from flask import Flask
from flask_cors import CORS


load_dotenv()

# Inicializa o cliente OpenAI com base na API da Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)



app = Flask(__name__)
CORS(app, resources={r"/summarize": {"origins": "*"}})



def summarize(text):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "Resuma o texto abaixo de forma objetiva:"},
            {"role": "user", "content": text}
        ],
        temperature=0.5,
        max_tokens=200
    )
    return response.choices[0].message.content

# Define a rota da API
@app.route('/summarize', methods=['POST'])
def summarize_route():
    data = request.get_json() 
    text = data.get('text')    
    
    if not text:
        return jsonify({'error': 'Campo "text" é obrigatório'}), 400

    resumo = summarize(text)
    return jsonify({'resumo': resumo})

# Roda o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
