from sqlalchemy.orm import Session
from models import Project

# Funzione per ottenere tutti i progetti
def get_projects(db: Session):
    return db.query(Project).all()

# Funzione per aggiungere un nuovo progetto
def create_project(db: Session, title: str, description: str, link: str = None):
    new_project = Project(title=title, description=description, link=link)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project
