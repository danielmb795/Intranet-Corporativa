from database.engine import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey, String ,Enum
from models.enums.TicketEnums import TypeTicket, UrgencyTicket
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.UserModel import UserModel

class TicketModel(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    title: Mapped[str] = mapped_column(String(90))
    body: Mapped[str] = mapped_column(String(90))

    type: Mapped[TypeTicket] = mapped_column(
        Enum(TypeTicket),
        default=TypeTicket.REQUEST,
        nullable=False
    )

    urgency: Mapped[UrgencyTicket] = mapped_column(
        Enum(UrgencyTicket),
        default=UrgencyTicket.MEDIUM,
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    users: Mapped["UserModel"] = relationship(
        back_populates="tickets"
    )

    