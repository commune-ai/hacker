
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModel
import torch
import requests

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model and tokenizer
model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

class SearchQuery(BaseModel):
    query: str

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

@app.post("/search")
async def search(query: SearchQuery):
    # Get the embedding for the query
    query_embedding = get_embedding(query.query)

    # Search GitHub API
    github_api_url = "https://api.github.com/search/repositories"
    params = {
        "q": query.query,
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }
    response = requests.get(github_api_url, params=params)
    repos = response.json()["items"]

    # Calculate semantic similarity and sort results
    results = []
    for repo in repos:
        repo_embedding = get_embedding(repo["description"] or "")
        similarity = torch.nn.functional.cosine_similarity(
            torch.tensor(query_embedding),
            torch.tensor(repo_embedding),
            dim=0
        ).item()
        results.append({
            "name": repo["full_name"],
            "description": repo["description"],
            "url": repo["html_url"],
            "similarity": similarity
        })

    # Sort results by similarity
    results.sort(key=lambda x: x["similarity"], reverse=True)

    return results[:5]  # Return top 5 results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
