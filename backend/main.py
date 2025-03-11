from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, crud

app = FastAPI()

# 🔹 Abilitare CORS per permettere le richieste dal frontend
origins = [
    "http://localhost:5173",  # Frontend locale    
    "http://127.0.0.1:5173",  # Variante possibile dell'URL locale
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permetti SOLO richieste dal frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permetti tutti i metodi HTTP (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Permetti tutti gli headers
)

# Crea le tabelle nel database se non esistono
models.Base.metadata.create_all(bind=engine)

# Dependency per ottenere la sessione DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/projects/")
def read_projects(db: Session = Depends(get_db)):
    return crud.get_projects(db)

@app.post("/projects/")
def create_project(title: str, description: str, link: str = None, db: Session = Depends(get_db)):
    return crud.create_project(db, title, description, link)
