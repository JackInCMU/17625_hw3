import Book_pb2 as _Book_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
STATUS_AVAILABLE: Status
STATUS_TAKEN: Status
STATUS_UNSPECIFIED: Status

class InventoryItem(_message.Message):
    __slots__ = ["aBook", "inventoryNum", "status"]
    ABOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORYNUM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    aBook: _Book_pb2.Book
    inventoryNum: int
    status: Status
    def __init__(self, inventoryNum: _Optional[int] = ..., status: _Optional[_Union[Status, str]] = ..., aBook: _Optional[_Union[_Book_pb2.Book, _Mapping]] = ...) -> None: ...

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
