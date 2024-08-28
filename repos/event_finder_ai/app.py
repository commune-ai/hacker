
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import requests
from bs4 import BeautifulSoup

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

def search_web(query):
    # This is a simplified web search function. In a real-world scenario, you'd use a proper search API.
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='g')
    return [result.get_text() for result in results[:5]]

@app.route('/find_events', methods=['POST'])
def find_events():
    data = request.json
    location = data.get('location')
    preferences = data.get('preferences')

    if not location or not preferences:
        return jsonify({"error": "Missing location or preferences"}), 400

    search_query = f"events in {location} {preferences}"
    search_results = search_web(search_query)

    prompt = f"Based on the following search results about events in {location} related to {preferences}, provide a list of 5 relevant events with their names, dates, and brief descriptions:\n\n"
    prompt += "\n".join(search_results)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    events = response.choices[0].text.strip()
    return jsonify({"events": events})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
