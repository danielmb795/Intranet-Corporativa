from database.engine import SessionLocal, engine
from models.UserModel import UserModel
from models.enums.UserEnums import TypeUser 

class UserRepository():
    @staticmethod
    def creteUser(name: str, email: str, password: str, typeuser : type[TypeUser]) -> UserModel | None:
        with SessionLocal(engine) as session:
            new_user = UserModel(name=name, email=email, password=password)
            session.add(new_user)
            session.commit()
        return new_user
            

    @staticmethod
    def listAllUsers():
        pass
                

    @staticmethod
    def filterUser():
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass

UserRepository.creteUser(name="teste", email="teste@teste", password="teste", userEnum=type.STANDARD)