# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Book.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nBook.proto\x12\x04\x62ook\"b\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x1a\n\x05genre\x18\x04 \x01(\x0e\x32\x0b.book.Genre\x12\x13\n\x0bpublishYear\x18\x05 \x01(\x05*[\n\x05Genre\x12\x15\n\x11GENRE_UNSPECIFIED\x10\x00\x12\x11\n\rGENRE_FANTASY\x10\x01\x12\x13\n\x0fGENRE_DYSTOPIAN\x10\x02\x12\x13\n\x0fGENRE_ADVENTURE\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Book_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENRE._serialized_start=120
  _GENRE._serialized_end=211
  _BOOK._serialized_start=20
  _BOOK._serialized_end=118
# @@protoc_insertion_point(module_scope)
