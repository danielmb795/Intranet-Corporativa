import enum
from sqlalchemy import Enum

class TypeTicket(enum.Enum):
    INCIDENT = "INCIDENT"
    REQUEST = "REQUEST"

class UrgencyTicket(enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

