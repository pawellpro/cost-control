from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, login=user.login)
    if db_user:
        raise HTTPException(status_code=400, detail="Login already exist")
    return crud.create_user(db=db, user=user)


@app.post("/users/{login}/items/", response_model=schemas.Item)
def create_item_for_user(item: schemas.Item, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item)


@app.get("/users/{login}", response_model=schemas.User)
def get_user_by_login(login: str, db: Session = Depends(get_db)):
    return crud.get_user(db, login)

# todo: make method to read items by time
# @app.get("/items/{user}/", response_model=list[schemas.Item])
# def read_items(user: schemas.User, db: Session = Depends(get_db)):
#     items = crud.get_items(db, login=user.login)
#     return items
