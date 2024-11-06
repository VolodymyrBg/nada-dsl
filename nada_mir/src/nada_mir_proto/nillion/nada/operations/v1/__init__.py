# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: nillion/nada/v1/operations.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import List

import betterproto

from ...types import v1 as __types_v1__


class OperationVariant(betterproto.Enum):
    """
    The variant of the operation.
     This enumeration effectively lists all the different operations supported
    """

    REDUCE = 0
    """Reduce operation variant"""

    MAP = 1
    """Map operation variant"""

    UNZIP = 2
    """Unzip operation variant"""

    ZIP = 3
    """Zip operation variant"""

    ADDITION = 4
    """Addition operation variant"""

    SUBTRACTION = 5
    """Addition operation variant"""

    MULTIPLICATION = 6
    """Multiplication operation variant"""

    LESS_THAN = 7
    """Less-than comparison operation variant"""

    LESS_EQ = 8
    """Less-or-equal-than comparison operation variant"""

    GREATER_THAN = 9
    """Greater-than comparison operation variant"""

    GREATER_EQ = 10
    """Greater-or-equal-than comparison operation variant"""

    EQUALS_PUBLIC_OUTPUT = 11
    """Equals public output comparison operation variant"""

    EQUALS = 12
    """
    Equals comparison operation variant also public-public
     comparisons
    """

    CAST = 13
    """Cast operation variant"""

    INPUT_REF = 14
    """InputReference operation variant"""

    LITERAL_REF = 15
    """LiteralReference operation variant"""

    NADA_FN_ARG_REF = 16
    """Nada function argument variant"""

    MODULO = 17
    """Modulo operation variant"""

    POWER = 18
    """Power operation variant"""

    DIVISION = 19
    """Division operation variant"""

    NADA_FN_CALL = 20
    """Nada function call variant"""

    ARRAY_ACC = 21
    """Array accessor variant"""

    TUPLE_ACC = 22
    """Tuple accessor variant"""

    NEW = 23
    """New operation variant"""

    RANDOM = 24
    """Random operation variant"""

    IF_ELSE = 25
    """IfElse operation variant"""

    REVEAL = 26
    """Reveal operation variant"""

    NOT = 27
    """Not operation variant"""

    LEFT_SHIFT = 28
    """Left Shift operation variant"""

    RIGHT_SHIFT = 29
    """Right Shift operation variant"""

    TRUNC_PR = 30
    """Probabilistic truncation operation variant"""

    INNER_PROD = 31
    """Inner product operation"""

    NOT_EQUALS = 32
    """Not equals operation"""

    BOOL_AND = 33
    """Boolean AND operation variant"""

    BOOL_OR = 34
    """Boolean OR operation variant"""

    BOOL_XOR = 35
    """Boolean XOR operation variant"""


class TupleIndex(betterproto.Enum):
    LEFT = 0
    """The left element of the tuple"""

    RIGHT = 1
    """The right element of the tuple"""


@dataclass(eq=False, repr=False)
class OperationDescriptor(betterproto.Message):
    """
    The operation descriptor abstracts the base elements that identify any
     operation:
     - The operation identifier
     - The output type of the operation
     - The index of the source reference
    """

    id: int = betterproto.uint64_field(1)
    """Operation identifier"""

    type: "__types_v1__.NadaType" = betterproto.message_field(2)
    """The output type of the operation"""

    source_ref_index: int = betterproto.uint64_field(3)
    """Source file info related with this operation."""


@dataclass(eq=False, repr=False)
class BinaryOperation(betterproto.Message):
    """
    MIR Binary operation.
     Basically most arithmetic operations: Addition, Subtraction
     Division, Modulo, Power, etc.
    """

    op: "OperationDescriptor" = betterproto.message_field(1)
    """Operation descriptor"""

    left: int = betterproto.uint64_field(2)
    """Left operand of the operation"""

    right: int = betterproto.uint64_field(3)
    """Right operand of the operation"""


@dataclass(eq=False, repr=False)
class UnaryOperation(betterproto.Message):
    """
    Represents a MIR Unary operation:
     - Cast
     - Not
     - Reveal
     - Unzip
    """

    op: "OperationDescriptor" = betterproto.message_field(1)
    """Operation descriptor"""

    this: int = betterproto.uint64_field(2)
    """The operand of the operation"""


@dataclass(eq=False, repr=False)
class IfElseOperation(betterproto.Message):
    op: "OperationDescriptor" = betterproto.message_field(1)
    """Operation descriptor"""

    cond: int = betterproto.uint64_field(2)
    """operand of the conditional operation"""

    first: int = betterproto.uint64_field(3)
    """operand of the first operation"""

    second: int = betterproto.uint64_field(4)
    """operand of the second operation"""


@dataclass(eq=False, repr=False)
class RandomOperation(betterproto.Message):
    op: "OperationDescriptor" = betterproto.message_field(1)
    """Operation descriptor"""


@dataclass(eq=False, repr=False)
class InputReference(betterproto.Message):
    """
    Input reference structure, can be used for:
     - Input
     - Literal
     Also, it is used to describe the nada function arguments.
    """

    op: "OperationDescriptor" = betterproto.message_field(1)
    """Operation descriptor"""

    refers_to: int = betterproto.uint64_field(2)
    """Index of the input/literal operation referred by this operation"""


@dataclass(eq=False, repr=False)
class MapOperation(betterproto.Message):
    op: "OperationDescriptor" = betterproto.message_field(1)
    """Operation descriptor"""

    fn: int = betterproto.uint64_field(2)
    """Function to execute"""

    inner: int = betterproto.uint64_field(3)
    """Map operation input"""


@dataclass(eq=False, repr=False)
class ReduceOperation(betterproto.Message):
    op: "OperationDescriptor" = betterproto.message_field(1)
    """Operation descriptor"""

    fn: int = betterproto.uint64_field(2)
    """Function to execute"""

    inner: int = betterproto.uint64_field(3)
    """Map operation input"""

    initial: int = betterproto.uint64_field(4)
    """Initial accumulator value"""


@dataclass(eq=False, repr=False)
class NewOperation(betterproto.Message):
    op: "OperationDescriptor" = betterproto.message_field(1)
    """Operation descriptor"""

    elements: List[int] = betterproto.uint64_field(2)
    """The elements of this compound type"""


@dataclass(eq=False, repr=False)
class ArrayAccessor(betterproto.Message):
    op: "OperationDescriptor" = betterproto.message_field(1)
    """Operation descriptor"""

    index: int = betterproto.uint32_field(2)
    """
    array index - for now an integer but eventually it could be the result of
     an operation
    """

    source: int = betterproto.uint64_field(3)
    """source - The Operation that represents the array we are accessing"""


@dataclass(eq=False, repr=False)
class TupleAccessor(betterproto.Message):
    op: "OperationDescriptor" = betterproto.message_field(1)
    """Operation descriptor"""

    index: "TupleIndex" = betterproto.enum_field(2)
    """tuple index (left or right)"""

    source: int = betterproto.uint64_field(3)
    """source - The Operation that represents the tuple we are accessing"""


@dataclass(eq=False, repr=False)
class NadaFunctionArgRef(betterproto.Message):
    arg: "InputReference" = betterproto.message_field(1)
    """The input reference for this argument"""

    function_id: int = betterproto.uint64_field(2)
    """Function owner of this argument"""


@dataclass(eq=False, repr=False)
class NadaFunctionCall(betterproto.Message):
    op: "OperationDescriptor" = betterproto.message_field(1)
    """Operation descriptor"""

    function_id: int = betterproto.uint64_field(2)
    """Function owner of this call"""

    args: List[int] = betterproto.uint64_field(3)
    """Arguments of the call"""


@dataclass(eq=False, repr=False)
class Operation(betterproto.Message):
    """
    The Operation.
     An operation is identified by:
     - The operation variant
    """

    id: "OperationVariant" = betterproto.enum_field(1)
    binary: "BinaryOperation" = betterproto.message_field(2, group="operation")
    unary: "UnaryOperation" = betterproto.message_field(3, group="operation")
    ifelse: "IfElseOperation" = betterproto.message_field(4, group="operation")
    random: "RandomOperation" = betterproto.message_field(5, group="operation")
    input: "InputReference" = betterproto.message_field(6, group="operation")
    map: "MapOperation" = betterproto.message_field(7, group="operation")
    reduce: "ReduceOperation" = betterproto.message_field(8, group="operation")
    new: "NewOperation" = betterproto.message_field(9, group="operation")
    array_accessor: "ArrayAccessor" = betterproto.message_field(10, group="operation")
    tuple_accessor: "TupleAccessor" = betterproto.message_field(11, group="operation")
    arg: "NadaFunctionArgRef" = betterproto.message_field(12, group="operation")
    call: "NadaFunctionCall" = betterproto.message_field(13, group="operation")