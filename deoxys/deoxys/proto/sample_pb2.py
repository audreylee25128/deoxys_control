# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sample.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0csample.proto\"\x1e\n\x11RobotStateMessage\x12\t\n\x01x\x18\x01 \x01(\x05\x62\x06proto3')
)




_ROBOTSTATEMESSAGE = _descriptor.Descriptor(
  name='RobotStateMessage',
  full_name='RobotStateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='RobotStateMessage.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=46,
)

DESCRIPTOR.message_types_by_name['RobotStateMessage'] = _ROBOTSTATEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RobotStateMessage = _reflection.GeneratedProtocolMessageType('RobotStateMessage', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTSTATEMESSAGE,
  '__module__' : 'sample_pb2'
  # @@protoc_insertion_point(class_scope:RobotStateMessage)
  })
_sym_db.RegisterMessage(RobotStateMessage)


# @@protoc_insertion_point(module_scope)
