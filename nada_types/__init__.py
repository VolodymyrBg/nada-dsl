from dataclasses import dataclass
from typing import Union, Type

AllTypes = Union[
    "PublicInteger8",
    "PublicInteger16",
    "PublicBigInteger",
    "SecretInteger8",
    "SecretInteger16",
    "SecretBigInteger",
    "SecretBoolean",
    "SecretFixedPointRational",
]
AllTypesType = Union[
    Type["PublicInteger8"],
    Type["PublicInteger16"],
    Type["PublicBigInteger"],
    Type["SecretInteger8"],
    Type["SecretInteger16"],
    Type["SecretBigInteger"],
    Type["SecretFixedPointRational"],
]
OperationType = Union[
    "Addition",
    "Multiplication",
    "Input",
    "Cast",
    "Map",
    "Zip",
    "Reduce",
    "Unzip",
    "CompareLessThan",
]


@dataclass
class NadaType:
    inner: OperationType
