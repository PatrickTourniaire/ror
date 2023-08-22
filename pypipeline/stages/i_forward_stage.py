# External imports
from typing import Generic, Tuple, TypeVar, get_args

# Local imports
from .common import IBaseStage

# Generics
I = TypeVar("I")  # Input data type
O = TypeVar("O")  # Output data type
N = TypeVar("N", bound=IBaseStage)  # Next stage reference


class IForwardStage(IBaseStage[I, O], Generic[I, O, N]):
    def __init_subclass__(cls) -> None:
        cls._types = get_args(cls.__orig_bases__[0])

    def discover(self) -> N:
        return self._types[-1]

    def get_output(self) -> Tuple[N, O]:
        pass

    def input_schema(self) -> I:
        return self._types[0]

    def output_schema(self) -> O:
        return self._types[-1]