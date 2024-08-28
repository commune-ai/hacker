
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class SearchRequest(BaseModel):
    location: str
    preferences: str

@app.post("/search")
async def search_rentals(request: SearchRequest):
    try:
        # Use OpenAI to generate search queries
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Generate a web search query for rental listings in {request.location} with these preferences: {request.preferences}",
            max_tokens=50
        )
        search_query = response.choices[0].text.strip()

        # Perform web scraping (simplified example)
        url = f"https://www.example-rental-site.com/search?q={search_query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract rental listings (this is a placeholder, you'd need to implement actual scraping logic)
        listings = [{"title": item.text, "link": item['href']} for item in soup.select('.rental-listing a')]

        # Use OpenAI to filter and summarize results
        summary = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Summarize these rental listings based on the preferences: {request.preferences}\n\n{listings}",
            max_tokens=200
        )

        return {"listings": listings, "summary": summary.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
