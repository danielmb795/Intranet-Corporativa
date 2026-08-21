from database.engine import SessionLocal
from models.UserModel import UserModel
from models.enums import UserEnums
import bcrypt

class UserRepository():
    @staticmethod
    def _hash_password(password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    @staticmethod
    def _verify(password: str, hashed: str) ->  bool:
        return bcrypt.checkpw(
            password.encode('utf-8'),
            hashed.encode('utf-8')
        )


    @staticmethod
    def creteUser(name: str, email: str, password: str, type: UserEnums) -> UserModel | None:
        with SessionLocal() as session:
            hashed_password = UserRepository._hash_password(password)
            new_user = UserModel(name=name, email=email, password=hashed_password,type=type)
            session.add(new_user)
            session.commit()
        return new_user
            

    @staticmethod
    def listAllUsers():
        with SessionLocal() as session:
            user = session.query(UserModel).all()
            return user
            

    @staticmethod
    def filterUserById(id: int):
        with SessionLocal() as session:
            user = session.query(UserModel).filter_by(id=id).first()
            if user is None:
                return "User not found"
            return user
            
    @staticmethod
    def updateUser(id: int ,name, email, password : str ,type: UserEnums):
        with SessionLocal() as session:
            user = session.query(UserModel).filter_by(id=id).first()
            if user is None:
                return "User not found" 

            user.name = name
            user.email = email
            user.password = password
            user.type = type
            session.commit()
            session.refresh(user)

            return user
        
    @staticmethod
    def deleteUser(id: int):
        with SessionLocal() as session:
            user = session.query(UserModel).filter_by(id=id).first()
            if user is None:
                "Usuário não encontrado"

            session.delete(user)
            session.commit()
            return "Usuário deletado com sucesso"