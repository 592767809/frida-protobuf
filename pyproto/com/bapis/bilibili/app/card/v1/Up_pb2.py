# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/com.bapis.bilibili.app.card.v1.Up.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyproto.com.bapis.bilibili.app.card.v1 import Button_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Button__pb2
from pyproto.com.bapis.bilibili.app.card.v1 import Avatar_pb2 as pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Avatar__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/com.bapis.bilibili.app.card.v1.Up.proto',
  package='com.bapis.bilibili.app.card.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/pyproto/com.bapis.bilibili.app.card.v1.Up.proto\x12\x1e\x63om.bapis.bilibili.app.card.v1\x1a\x33pyproto/com.bapis.bilibili.app.card.v1.Button.proto\x1a\x33pyproto/com.bapis.bilibili.app.card.v1.Avatar.proto\"\xc6\x02\n\x02Up\x12\x0f\n\x02id\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04\x64\x65sc\x18\x03 \x01(\tH\x02\x88\x01\x01\x12;\n\x06\x61vatar\x18\x04 \x01(\x0b\x32&.com.bapis.bilibili.app.card.v1.AvatarH\x03\x88\x01\x01\x12\x1a\n\rofficial_icon\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12@\n\x0b\x64\x65sc_button\x18\x06 \x01(\x0b\x32&.com.bapis.bilibili.app.card.v1.ButtonH\x05\x88\x01\x01\x12\x18\n\x0b\x63ooperation\x18\x07 \x01(\tH\x06\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_nameB\x07\n\x05_descB\t\n\x07_avatarB\x10\n\x0e_official_iconB\x0e\n\x0c_desc_buttonB\x0e\n\x0c_cooperationb\x06proto3'
  ,
  dependencies=[pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Button__pb2.DESCRIPTOR,pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Avatar__pb2.DESCRIPTOR,])




_UP = _descriptor.Descriptor(
  name='Up',
  full_name='com.bapis.bilibili.app.card.v1.Up',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.bapis.bilibili.app.card.v1.Up.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.bapis.bilibili.app.card.v1.Up.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desc', full_name='com.bapis.bilibili.app.card.v1.Up.desc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='com.bapis.bilibili.app.card.v1.Up.avatar', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='official_icon', full_name='com.bapis.bilibili.app.card.v1.Up.official_icon', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desc_button', full_name='com.bapis.bilibili.app.card.v1.Up.desc_button', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cooperation', full_name='com.bapis.bilibili.app.card.v1.Up.cooperation', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_id', full_name='com.bapis.bilibili.app.card.v1.Up._id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_name', full_name='com.bapis.bilibili.app.card.v1.Up._name',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_desc', full_name='com.bapis.bilibili.app.card.v1.Up._desc',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_avatar', full_name='com.bapis.bilibili.app.card.v1.Up._avatar',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_official_icon', full_name='com.bapis.bilibili.app.card.v1.Up._official_icon',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_desc_button', full_name='com.bapis.bilibili.app.card.v1.Up._desc_button',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_cooperation', full_name='com.bapis.bilibili.app.card.v1.Up._cooperation',
      index=6, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=190,
  serialized_end=516,
)

_UP.fields_by_name['avatar'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Avatar__pb2._AVATAR
_UP.fields_by_name['desc_button'].message_type = pyproto_dot_com_dot_bapis_dot_bilibili_dot_app_dot_card_dot_v1_dot_Button__pb2._BUTTON
_UP.oneofs_by_name['_id'].fields.append(
  _UP.fields_by_name['id'])
_UP.fields_by_name['id'].containing_oneof = _UP.oneofs_by_name['_id']
_UP.oneofs_by_name['_name'].fields.append(
  _UP.fields_by_name['name'])
_UP.fields_by_name['name'].containing_oneof = _UP.oneofs_by_name['_name']
_UP.oneofs_by_name['_desc'].fields.append(
  _UP.fields_by_name['desc'])
_UP.fields_by_name['desc'].containing_oneof = _UP.oneofs_by_name['_desc']
_UP.oneofs_by_name['_avatar'].fields.append(
  _UP.fields_by_name['avatar'])
_UP.fields_by_name['avatar'].containing_oneof = _UP.oneofs_by_name['_avatar']
_UP.oneofs_by_name['_official_icon'].fields.append(
  _UP.fields_by_name['official_icon'])
_UP.fields_by_name['official_icon'].containing_oneof = _UP.oneofs_by_name['_official_icon']
_UP.oneofs_by_name['_desc_button'].fields.append(
  _UP.fields_by_name['desc_button'])
_UP.fields_by_name['desc_button'].containing_oneof = _UP.oneofs_by_name['_desc_button']
_UP.oneofs_by_name['_cooperation'].fields.append(
  _UP.fields_by_name['cooperation'])
_UP.fields_by_name['cooperation'].containing_oneof = _UP.oneofs_by_name['_cooperation']
DESCRIPTOR.message_types_by_name['Up'] = _UP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Up = _reflection.GeneratedProtocolMessageType('Up', (_message.Message,), {
  'DESCRIPTOR' : _UP,
  '__module__' : 'pyproto.com.bapis.bilibili.app.card.v1.Up_pb2'
  # @@protoc_insertion_point(class_scope:com.bapis.bilibili.app.card.v1.Up)
  })
_sym_db.RegisterMessage(Up)


# @@protoc_insertion_point(module_scope)