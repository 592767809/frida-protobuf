# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/OperationType.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/OperationType.proto',
  package='com.tencent.qqlive.protocol.pb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bpyproto/OperationType.proto\x12\x1e\x63om.tencent.qqlive.protocol.pb*\xa0\x08\n\rOperationType\x12\x19\n\x15OPERATION_TYPE_ACTION\x10\x00\x12\x19\n\x15OPERATION_TYPE_ATTENT\x10\x01\x12\x18\n\x14OPERATION_TYPE_SHARE\x10\x02\x12\x19\n\x15OPERATION_TYPE_PRAISE\x10\x03\x12\x1b\n\x17OPERATION_TYPE_DOWNLOAD\x10\x04\x12\x1b\n\x17OPERATION_TYPE_FEEDBACK\x10\x05\x12\x1d\n\x19OPERATION_TYPE_PLAY_VIDEO\x10\x06\x12\x1e\n\x1aOPERATION_TYPE_SCROLL_LIST\x10\x08\x12!\n\x1dOPERATION_TYPE_CHANGE_SECTION\x10\t\x12#\n\x1fOPERATION_TYPE_EXTRA_BLOCK_LIST\x10\n\x12\x19\n\x15OPERATION_TYPE_REPORT\x10\x0b\x12\x19\n\x15OPERATION_TYPE_FOLLOW\x10\x0c\x12 \n\x1cOPERATION_TYPE_SCHEME_ACTION\x10\r\x12+\n\'OPERATION_TYPE_TRANSITION_IMAGE_PREVIEW\x10\x0e\x12\x18\n\x14OPERATION_TYPE_EMPTY\x10\x0f\x12\x1a\n\x16OPERATION_TYPE_COMMENT\x10\x10\x12\"\n\x1eOPERATION_TYPE_REFRESH_SECTION\x10\x11\x12\x19\n\x15OPERATION_TYPE_SEARCH\x10\x12\x12#\n\x1fOPERATION_TYPE_INTERACT_TRIGGER\x10\x13\x12\x1f\n\x1bOPERATION_TYPE_FLIP_SECTION\x10\x14\x12\x1f\n\x1bOPERATION_TYPE_INTERFERENCE\x10\x15\x12)\n%OPERATION_TYPE_INSERT_NEW_LINE_CONFIG\x10\x16\x12\x1c\n\x18OPERATION_TYPE_CARD_FLOP\x10\x17\x12\x1e\n\x1aOPERATION_TYPE_TITLE_TOPIC\x10\x18\x12$\n OPERATION_TYPE_FLOP_CARD_OPERATE\x10\x19\x12!\n\x1dOPERATION_TYPE_FLOP_CARD_INFO\x10\x1a\x12 \n\x1cOPERATION_TYPE_POPUP_CONTENT\x10\x1b\x12$\n OPERATION_TYPE_USER_INFO_RED_DOT\x10\x1c\x12$\n OPERATION_TYPE_CREATOR_JUMP_PAGE\x10\x1d\x12\x1c\n\x18OPERATION_TYPE_SUBSCRIBE\x10\x1e\x12#\n\x1fOPERATION_TYPE_SHOW_OPER_DIALOG\x10\x1f\x12\x1f\n\x1bOPERATION_TYPE_COMMON_FLOAT\x10 b\x06proto3'
)

_OPERATIONTYPE = _descriptor.EnumDescriptor(
  name='OperationType',
  full_name='com.tencent.qqlive.protocol.pb.OperationType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_ACTION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_ATTENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_SHARE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_PRAISE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_DOWNLOAD', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_FEEDBACK', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_PLAY_VIDEO', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_SCROLL_LIST', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_CHANGE_SECTION', index=8, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_EXTRA_BLOCK_LIST', index=9, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_REPORT', index=10, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_FOLLOW', index=11, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_SCHEME_ACTION', index=12, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_TRANSITION_IMAGE_PREVIEW', index=13, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_EMPTY', index=14, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_COMMENT', index=15, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_REFRESH_SECTION', index=16, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_SEARCH', index=17, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_INTERACT_TRIGGER', index=18, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_FLIP_SECTION', index=19, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_INTERFERENCE', index=20, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_INSERT_NEW_LINE_CONFIG', index=21, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_CARD_FLOP', index=22, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_TITLE_TOPIC', index=23, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_FLOP_CARD_OPERATE', index=24, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_FLOP_CARD_INFO', index=25, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_POPUP_CONTENT', index=26, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_USER_INFO_RED_DOT', index=27, number=28,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_CREATOR_JUMP_PAGE', index=28, number=29,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_SUBSCRIBE', index=29, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_SHOW_OPER_DIALOG', index=30, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_TYPE_COMMON_FLOAT', index=31, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=64,
  serialized_end=1120,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONTYPE)

OperationType = enum_type_wrapper.EnumTypeWrapper(_OPERATIONTYPE)
OPERATION_TYPE_ACTION = 0
OPERATION_TYPE_ATTENT = 1
OPERATION_TYPE_SHARE = 2
OPERATION_TYPE_PRAISE = 3
OPERATION_TYPE_DOWNLOAD = 4
OPERATION_TYPE_FEEDBACK = 5
OPERATION_TYPE_PLAY_VIDEO = 6
OPERATION_TYPE_SCROLL_LIST = 8
OPERATION_TYPE_CHANGE_SECTION = 9
OPERATION_TYPE_EXTRA_BLOCK_LIST = 10
OPERATION_TYPE_REPORT = 11
OPERATION_TYPE_FOLLOW = 12
OPERATION_TYPE_SCHEME_ACTION = 13
OPERATION_TYPE_TRANSITION_IMAGE_PREVIEW = 14
OPERATION_TYPE_EMPTY = 15
OPERATION_TYPE_COMMENT = 16
OPERATION_TYPE_REFRESH_SECTION = 17
OPERATION_TYPE_SEARCH = 18
OPERATION_TYPE_INTERACT_TRIGGER = 19
OPERATION_TYPE_FLIP_SECTION = 20
OPERATION_TYPE_INTERFERENCE = 21
OPERATION_TYPE_INSERT_NEW_LINE_CONFIG = 22
OPERATION_TYPE_CARD_FLOP = 23
OPERATION_TYPE_TITLE_TOPIC = 24
OPERATION_TYPE_FLOP_CARD_OPERATE = 25
OPERATION_TYPE_FLOP_CARD_INFO = 26
OPERATION_TYPE_POPUP_CONTENT = 27
OPERATION_TYPE_USER_INFO_RED_DOT = 28
OPERATION_TYPE_CREATOR_JUMP_PAGE = 29
OPERATION_TYPE_SUBSCRIBE = 30
OPERATION_TYPE_SHOW_OPER_DIALOG = 31
OPERATION_TYPE_COMMON_FLOAT = 32


DESCRIPTOR.enum_types_by_name['OperationType'] = _OPERATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)