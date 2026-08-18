from database.engine import SessionLocal
from models.UserModel import UserModel

class UserRepository():
    @staticmethod
    def createUser(user: UserModel) -> UserModel:
        user = UserModel(
            
        )