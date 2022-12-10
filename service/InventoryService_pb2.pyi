import Book_pb2 as _Book_pb2
import InventoryItem_pb2 as _InventoryItem_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBookRequest(_message.Message):
    __slots__ = ["newBook"]
    NEWBOOK_FIELD_NUMBER: _ClassVar[int]
    newBook: _Book_pb2.Book
    def __init__(self, newBook: _Optional[_Union[_Book_pb2.Book, _Mapping]] = ...) -> None: ...

class CreateBookResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["author", "genre", "publishYear", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: _Book_pb2.Genre
    publishYear: int
    title: str
    def __init__(self, title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[_Book_pb2.Genre, str]] = ..., publishYear: _Optional[int] = ...) -> None: ...
