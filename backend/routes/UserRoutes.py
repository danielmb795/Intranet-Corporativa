from repository.UserRepository import UserRepository
from models.enums.UserEnums import TypeUser


UserRepository.creteUser(name="teste", email="teste@teste", password="teste", userEnum=TypeUser.STANDARD)   