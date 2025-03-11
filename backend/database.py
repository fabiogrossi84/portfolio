from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Recupera i dati dal file .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Crea il motore di connessione al database
engine = create_engine(DATABASE_URL, echo=True)

# Crea la sessione per interagire con il database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
