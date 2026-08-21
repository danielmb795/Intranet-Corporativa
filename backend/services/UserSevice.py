from repository.UserRepository import UserRepository
from models.enums.UserEnums import TypeUser

UserRepository.creteUser(
    name="daniel",
    email="teste@atitus.edu.br",
    password="teste",
    type=TypeUser.STANDARD   
)