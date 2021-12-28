from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()


def create_user(db: Session, user: schemas.User):
    db_user = models.User(id=user.id,
                          login=user.login,
                          password=user.password,
                          balance=user.balance)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_item(db: Session, item: schemas.Item):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
