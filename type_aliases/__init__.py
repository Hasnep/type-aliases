import collections.abc as abstract_base_classes
import typing
from typing import TypeAlias

__all__ = [
    "Any",
    "Bool",
    "Bytes",
    "Callable",
    "Dict",
    "Float",
    "Int",
    "Iterable",
    "Iterator",
    "List",
    "Literal",
    "LiteralString",
    "NamedTuple",
    "Optional",
    "Set",
    "Str",
    "Tuple",
    "Type",
    "TypeVar",
    "Union",
]

Any: TypeAlias = typing.Any
Bool: TypeAlias = bool
Bytes: TypeAlias = bytes
Callable = abstract_base_classes.Callable
Dict = dict
Float: TypeAlias = float
Int: TypeAlias = int
Iterable = abstract_base_classes.Iterable
Iterator = abstract_base_classes.Iterator
List = list
Literal = typing.Literal
LiteralString: TypeAlias = typing.LiteralString
NamedTuple: TypeAlias = typing.NamedTuple
Optional = typing.Optional
Set = set
Str: TypeAlias = str
Tuple = tuple
Type: TypeAlias = type
TypeVar: TypeAlias = typing.TypeVar
Union = typing.Union
