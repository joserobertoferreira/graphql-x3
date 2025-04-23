from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.type_api import TypeEngine  # For proper type hint of column_type

# Genérico para o tipo Python, ajuda nos type hints
T = TypeVar('T')


class ArrayColumnMixin:
    """
    Mixin to create a hybrid_property that acts like a list
    mapped to multiple columns in the database (ex: COL_0, COL_1, ...).
    This is useful for cases where you want to store a list of values
    in separate columns but access them as a single list in Python.
    """

    @classmethod
    def create_array_property(
        cls,
        db_column_name: str,
        property_name: str,
        count: int,
        column_type: Type[TypeEngine],  # Ex: Date, Unicode, Integer (tipo SQLAlchemy)
        python_type: Type[T] = Any,  # Ex: date, str, int (tipo Python para hints)
        **kwargs,  # Argumentos extras para mapped_column (nullable, server_default, etc.)
    ) -> Tuple[hybrid_property, Dict[str, Mapped[Optional[T]]]]:
        """
        Create and return a hybrid_property and a dictionary of the underlying Mapped columns.

        Args:
            db_column_name: Prefix of the column names in the database (e.g., 'DATINV').
            property_name: Desired name for the hybrid property in the Python model (e.g., 'datinv').
            count: Number of columns in the database (e.g., 3 for DATINV_0, DATINV_1, DATINV_2).
            column_type: The SQLAlchemy type for the columns (e.g., Date, Unicode(10), Integer).
            python_type: The corresponding Python type for type hints (e.g., date, str, int).
            **kwargs: Additional arguments passed to each `mapped_column` (e.g., nullable=True).

        Returns:
            A tuple containing:
            1. The configured hybrid_property object.
            2. A dictionary where the keys are the names of the internal attributes
               (e.g., '_datinv_0') and the values are the corresponding Mapped objects.
        """
        mapped_columns: Dict[str, Mapped[Optional[T]]] = {}
        internal_attr_names: List[str] = []

        # 1. Generate names and create Mapped objects for individual columns
        for i in range(count):
            db_column_name = f'{db_column_name}_{i}'
            # use property_name to ensure uniqueness if using the mixin multiple times
            internal_attr_name = f'_{property_name}_{i}'
            internal_attr_names.append(internal_attr_name)

            # create the mapped_column for this index
            mapped_columns[internal_attr_name] = mapped_column(db_column_name, column_type, **kwargs)

        # 2. Defines a getter function that retrieves the values of the internal attributes
        def getter(self) -> List[Optional[python_type]]:  # type: ignore
            """Read the internal attributes and return as a list."""
            return [getattr(self, name, None) for name in internal_attr_names]

        # 3. Defines a setter function that takes a list and assigns it to the internal attributes
        def setter(self, values: List[Optional[python_type]]) -> None:  # type: ignore
            """Receive a list and distribute it to the internal attributes."""
            if not isinstance(values, list):
                raise TypeError(f"Valor atribuído a '{property_name}' deve ser uma lista.")

            # Opcional: Validar tamanho máximo
            if len(values) > count:
                raise ValueError(f"Lista para '{property_name}' não pode ter mais que {count} elementos.")

            # Set the values to the internal attributes, padding with None if necessary or
            # the list is shorter than 'count'
            padded_values = values + [None] * (count - len(values))
            for i in range(count):
                setattr(self, internal_attr_names[i], padded_values[i])

        # 4. Create the hybrid_property using the getter and setter functions
        array_prop = hybrid_property(fget=getter, fset=setter)

        # 5. Return the hybrid_property and the dictionary of mapped columns
        return array_prop, mapped_columns


# class GenericsMixin:
#     """
#     Mixin class for generic fields and methods.
#     This class provides a set of common fields and methods that can be used across
#     different models.
#     It includes fields for tracking creation and modification timestamps,
#     as well as a UUID field for unique identification.
#     """

#     @declared_attr
#     def percentageOrAmount0(cls) -> Mapped[decimal.Decimal]:
#         return mapped_column('INVDTAAMT_0', Numeric(20, 5), server_default=text('((0))'))

#     INVDTAAMT_1: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_2: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_3: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_4: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_5: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_6: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_7: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_8: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_9: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_10: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_11: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_12: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_13: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_14: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_15: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_16: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_17: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_18: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_19: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_20: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_21: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_22: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_23: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_24: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_25: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_26: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_27: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_28: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTAAMT_29: Mapped[decimal.Decimal] = mapped_column(Numeric(20, 5))
#     INVDTA_0: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_1: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_2: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_3: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_4: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_5: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_6: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_7: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_8: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_9: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_10: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_11: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_12: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_13: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_14: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_15: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_16: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_17: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_18: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_19: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_20: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_21: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_22: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_23: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_24: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_25: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_26: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_27: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_28: Mapped[int] = mapped_column(SmallInteger)
#     INVDTA_29: Mapped[int] = mapped_column(SmallInteger)
