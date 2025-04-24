from enum import Enum


class Chapter1(Enum):
    """Chapter 1: Menu type"""

    NO = 1
    YES = 2


class Chapter45(Enum):
    """Chapter 45: Definition level"""

    FOLDER = 1
    COMPANY = 2
    SITE = 3


class Chapter46(Enum):
    """Chapter 46: Sequence number type"""

    ALPHANUMERIC = 1
    NUMERIC = 2


class Chapter47(Enum):
    """Chapter 47: Sequence number fields"""

    CONSTANT = 1
    YEAR = 2
    MONTH = 3
    WEEK = 4
    DAY = 5
    COMPANY = 6
    SITE = 7
    SEQUENCE_NUMBER = 8
    COMPLEMENT = 9
    FISCAL_YEAR = 10
    PERIOD = 11
    FORMULA = 12


class Chapter48(Enum):
    """Chapter 48: Reset sequence number to zero"""

    NO_RTZ = 1
    ANNUAL = 2
    MONTHLY = 3
    FISCAL_YEAR = 4
    PERIOD = 5
