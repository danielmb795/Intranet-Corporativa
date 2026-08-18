from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Enum
from models.enums.UserEnums import TypeUser
from typing import TYPE_CHECKING
from database.engine import Base
# from models.TicketModel import TicketModel

if TYPE_CHECKING:
    from models.TicketModel import TicketModel


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(90))
    email: Mapped[str] = mapped_column(String(90))
    password: Mapped[str] = mapped_column(String(100))
    
    type: Mapped[TypeUser] = mapped_column(
        Enum(TypeUser),
        default=TypeUser.STANDARD,
        nullable=False  
        )

    tickets: Mapped[list["TicketModel"]] = relationship(
        back_populates="users"
    )
