
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from .auth import create_access_token, get_current_user
from .repo_manager import RepoManager

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/repos/", response_model=schemas.Repo)
def create_repo(repo: schemas.RepoCreate, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return crud.create_repo(db=db, repo=repo, user_id=current_user.id)

@app.get("/repos/{repo_id}", response_model=schemas.Repo)
def read_repo(repo_id: int, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_repo = crud.get_repo(db, repo_id=repo_id)
    if db_repo is None:
        raise HTTPException(status_code=404, detail="Repo not found")
    return db_repo

@app.put("/repos/{repo_id}/files/{file_path:path}")
def update_file(repo_id: int, file_path: str, file_content: str, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    repo = crud.get_repo(db, repo_id=repo_id)
    if repo is None:
        raise HTTPException(status_code=404, detail="Repo not found")
    if repo.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to edit this repo")
    
    repo_manager = RepoManager(repo.name)
    result = repo_manager.update_file(file_path, file_content, f"Update {file_path}", current_user.email)
    return {"message": "File updated successfully", "commit_id": result['commit_id']}

@app.post("/repos/{repo_id}/pull-requests")
def create_pull_request(repo_id: int, pr: schemas.PullRequestCreate, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    repo = crud.get_repo(db, repo_id=repo_id)
    if repo is None:
        raise HTTPException(status_code=404, detail="Repo not found")
    return crud.create_pull_request(db=db, pr=pr, user_id=current_user.id, repo_id=repo_id)

# Add more endpoints for managing repos, files, and pull requests

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
