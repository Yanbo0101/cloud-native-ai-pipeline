# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/protobuf/frame.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63ore/protobuf/frame.proto\"\xa7\x01\n\x0c\x46rameMessage\x12\x13\n\x0bpipeline_id\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x03\x12\x0b\n\x03raw\x18\x03 \x01(\x0c\x12\x0e\n\x06ts_new\x18\x04 \x01(\x01\x12\x12\n\nraw_height\x18\x05 \x01(\x05\x12\x11\n\traw_width\x18\x06 \x01(\x05\x12\x14\n\x0craw_channels\x18\x07 \x01(\x05\x12\x16\n\x0ets_infer_start\x18\x08 \x01(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.protobuf.frame_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_FRAMEMESSAGE']._serialized_start=30
  _globals['_FRAMEMESSAGE']._serialized_end=197
# @@protoc_insertion_point(module_scope)