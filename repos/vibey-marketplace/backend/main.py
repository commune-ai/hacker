
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sentence_transformers import SentenceTransformer
import os

app = FastAPI()

# Database setup
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Website(Base):
    __tablename__ = "websites"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    title = Column(String)
    description = Column(Text)
    vector = Column(Text)

Base.metadata.create_all(bind=engine)

# Load sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

class WebsiteInput(BaseModel):
    url: str
    title: str
    description: str

@app.post("/websites")
def add_website(website: WebsiteInput):
    db = SessionLocal()
    
    # Check if website already exists
    existing_website = db.query(Website).filter(Website.url == website.url).first()
    if existing_website:
        raise HTTPException(status_code=400, detail="Website already exists")
    
    # Generate vector embedding
    text_to_embed = f"{website.title} {website.description}"
    vector = model.encode(text_to_embed).tolist()
    
    # Create new website entry
    new_website = Website(
        url=website.url,
        title=website.title,
        description=website.description,
        vector=str(vector)
    )
    
    db.add(new_website)
    db.commit()
    db.refresh(new_website)
    db.close()
    
    return {"message": "Website added successfully"}

@app.get("/search")
def search_websites(query: str):
    db = SessionLocal()
    
    # Generate vector embedding for the query
    query_vector = model.encode(query).tolist()
    
    # Perform vector search (simplified version, not efficient for large datasets)
    websites = db.query(Website).all()
    results = []
    
    for website in websites:
        website_vector = eval(website.vector)
        similarity = sum(a*b for a, b in zip(query_vector, website_vector))
        results.append((website, similarity))
    
    # Sort results by similarity (descending order)
    results.sort(key=lambda x: x[1], reverse=True)
    
    # Return top 10 results
    top_results = [
        {
            "url": website.url,
            "title": website.title,
            "description": website.description
        }
        for website, _ in results[:10]
    ]
    
    db.close()
    
    return top_results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
