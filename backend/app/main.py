from fastapi import FastAPI
from sqlmodel import select
from app.helpers.db import engine, SQLModel, session
from app.helpers.models import Hero

app = FastAPI(title="Nova Backend")
SQLModel.metadata.create_all(engine)

@app.get("/")
async def root():
    return {"message": "Hello darthman"}

@app.post("/add-hero")
async def add_hero():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)

    session.commit()
    session.close()
    return {"message":"Success"}

@app.get("/get-heros")
async def get_heros():
    statement = select(Hero)
    results = session.exec(statement)
    heros = results.all()
    return {"data":heros}
