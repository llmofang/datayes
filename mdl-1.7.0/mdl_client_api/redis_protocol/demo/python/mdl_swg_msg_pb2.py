# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: input/mdl_swg_msg.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='input/mdl_swg_msg.proto',
  package='datayes.mdl.mdl_swg_pbmsg',
  serialized_pb='\n\x17input/mdl_swg_msg.proto\x12\x19\x64\x61tayes.mdl.mdl_swg_pbmsg\"4\n\x07\x66loat_3\x12\r\n\x05Value\x18\x01 \x02(\x05\x12\x1a\n\x0c\x44\x65\x63imalShift\x18\x02 \x01(\r:\x04\x31\x30\x30\x30\"\xcd\x06\n\x05Index\x12\x12\n\nSecurityID\x18\x01 \x01(\t\x12\x14\n\x0cSecurityName\x18\x02 \x01(\t\x12\x37\n\x0bPreCloPrice\x18\x03 \x01(\x0b\x32\".datayes.mdl.mdl_swg_pbmsg.float_3\x12\x35\n\tOpenPrice\x18\x04 \x01(\x0b\x32\".datayes.mdl.mdl_swg_pbmsg.float_3\x12\x10\n\x08Turnover\x18\x05 \x01(\x04\x12\x35\n\tHighPrice\x18\x06 \x01(\x0b\x32\".datayes.mdl.mdl_swg_pbmsg.float_3\x12\x34\n\x08LowPrice\x18\x07 \x01(\x0b\x32\".datayes.mdl.mdl_swg_pbmsg.float_3\x12\x35\n\tLastPrice\x18\x08 \x01(\x0b\x32\".datayes.mdl.mdl_swg_pbmsg.float_3\x12\x31\n\x05Ratio\x18\t \x01(\x0b\x32\".datayes.mdl.mdl_swg_pbmsg.float_3\x12\x0e\n\x06Volume\x18\n \x01(\x04\x12\x14\n\x0c\x42idVolume123\x18\x0b \x01(\x04\x12\x35\n\tBidPrice2\x18\x0c \x01(\x0b\x32\".datayes.mdl.mdl_swg_pbmsg.float_3\x12\x12\n\nBidVolume2\x18\r \x01(\x04\x12\x35\n\tBidPrice3\x18\x0e \x01(\x0b\x32\".datayes.mdl.mdl_swg_pbmsg.float_3\x12\x12\n\nBidVolume3\x18\x0f \x01(\x04\x12\x14\n\x0c\x41skVolume123\x18\x10 \x01(\x04\x12\x35\n\tAskPrice2\x18\x11 \x01(\x0b\x32\".datayes.mdl.mdl_swg_pbmsg.float_3\x12\x12\n\nAskVolume2\x18\x12 \x01(\x04\x12\x35\n\tAskPrice3\x18\x13 \x01(\x0b\x32\".datayes.mdl.mdl_swg_pbmsg.float_3\x12\x12\n\nAskVolume3\x18\x14 \x01(\x04\x12\x12\n\nUpdateTime\x18\x15 \x01(\r\"\x14\n\x03MID\x12\r\n\tMessageID\x10\x01\"\x14\n\x03SID\x12\r\n\tServiceID\x10\x0c\"\x19\n\x03VID\x12\x12\n\x0eServiceVersion\x10\x65**\n\x14MDLSWGServiceVersion\x12\x12\n\x0eMDLVID_MDL_SWG\x10\x65*+\n\x0fMDLSWGMessageID\x12\x18\n\x14MDLMID_MDL_SWG_Index\x10\x01\x42\x0b\x42\tMDLSWGMsg')

_MDLSWGSERVICEVERSION = _descriptor.EnumDescriptor(
  name='MDLSWGServiceVersion',
  full_name='datayes.mdl.mdl_swg_pbmsg.MDLSWGServiceVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MDLVID_MDL_SWG', index=0, number=101,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=956,
  serialized_end=998,
)

MDLSWGServiceVersion = enum_type_wrapper.EnumTypeWrapper(_MDLSWGSERVICEVERSION)
_MDLSWGMESSAGEID = _descriptor.EnumDescriptor(
  name='MDLSWGMessageID',
  full_name='datayes.mdl.mdl_swg_pbmsg.MDLSWGMessageID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MDLMID_MDL_SWG_Index', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1000,
  serialized_end=1043,
)

MDLSWGMessageID = enum_type_wrapper.EnumTypeWrapper(_MDLSWGMESSAGEID)
MDLVID_MDL_SWG = 101
MDLMID_MDL_SWG_Index = 1


_INDEX_MID = _descriptor.EnumDescriptor(
  name='MID',
  full_name='datayes.mdl.mdl_swg_pbmsg.Index.MID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MessageID', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=885,
  serialized_end=905,
)

_INDEX_SID = _descriptor.EnumDescriptor(
  name='SID',
  full_name='datayes.mdl.mdl_swg_pbmsg.Index.SID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ServiceID', index=0, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=907,
  serialized_end=927,
)

_INDEX_VID = _descriptor.EnumDescriptor(
  name='VID',
  full_name='datayes.mdl.mdl_swg_pbmsg.Index.VID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ServiceVersion', index=0, number=101,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=929,
  serialized_end=954,
)


_FLOAT_3 = _descriptor.Descriptor(
  name='float_3',
  full_name='datayes.mdl.mdl_swg_pbmsg.float_3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Value', full_name='datayes.mdl.mdl_swg_pbmsg.float_3.Value', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DecimalShift', full_name='datayes.mdl.mdl_swg_pbmsg.float_3.DecimalShift', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=54,
  serialized_end=106,
)


_INDEX = _descriptor.Descriptor(
  name='Index',
  full_name='datayes.mdl.mdl_swg_pbmsg.Index',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SecurityID', full_name='datayes.mdl.mdl_swg_pbmsg.Index.SecurityID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SecurityName', full_name='datayes.mdl.mdl_swg_pbmsg.Index.SecurityName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PreCloPrice', full_name='datayes.mdl.mdl_swg_pbmsg.Index.PreCloPrice', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OpenPrice', full_name='datayes.mdl.mdl_swg_pbmsg.Index.OpenPrice', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Turnover', full_name='datayes.mdl.mdl_swg_pbmsg.Index.Turnover', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HighPrice', full_name='datayes.mdl.mdl_swg_pbmsg.Index.HighPrice', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LowPrice', full_name='datayes.mdl.mdl_swg_pbmsg.Index.LowPrice', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastPrice', full_name='datayes.mdl.mdl_swg_pbmsg.Index.LastPrice', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Ratio', full_name='datayes.mdl.mdl_swg_pbmsg.Index.Ratio', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Volume', full_name='datayes.mdl.mdl_swg_pbmsg.Index.Volume', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidVolume123', full_name='datayes.mdl.mdl_swg_pbmsg.Index.BidVolume123', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidPrice2', full_name='datayes.mdl.mdl_swg_pbmsg.Index.BidPrice2', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidVolume2', full_name='datayes.mdl.mdl_swg_pbmsg.Index.BidVolume2', index=12,
      number=13, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidPrice3', full_name='datayes.mdl.mdl_swg_pbmsg.Index.BidPrice3', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidVolume3', full_name='datayes.mdl.mdl_swg_pbmsg.Index.BidVolume3', index=14,
      number=15, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskVolume123', full_name='datayes.mdl.mdl_swg_pbmsg.Index.AskVolume123', index=15,
      number=16, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskPrice2', full_name='datayes.mdl.mdl_swg_pbmsg.Index.AskPrice2', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskVolume2', full_name='datayes.mdl.mdl_swg_pbmsg.Index.AskVolume2', index=17,
      number=18, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskPrice3', full_name='datayes.mdl.mdl_swg_pbmsg.Index.AskPrice3', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskVolume3', full_name='datayes.mdl.mdl_swg_pbmsg.Index.AskVolume3', index=19,
      number=20, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UpdateTime', full_name='datayes.mdl.mdl_swg_pbmsg.Index.UpdateTime', index=20,
      number=21, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INDEX_MID,
    _INDEX_SID,
    _INDEX_VID,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=109,
  serialized_end=954,
)

_INDEX.fields_by_name['PreCloPrice'].message_type = _FLOAT_3
_INDEX.fields_by_name['OpenPrice'].message_type = _FLOAT_3
_INDEX.fields_by_name['HighPrice'].message_type = _FLOAT_3
_INDEX.fields_by_name['LowPrice'].message_type = _FLOAT_3
_INDEX.fields_by_name['LastPrice'].message_type = _FLOAT_3
_INDEX.fields_by_name['Ratio'].message_type = _FLOAT_3
_INDEX.fields_by_name['BidPrice2'].message_type = _FLOAT_3
_INDEX.fields_by_name['BidPrice3'].message_type = _FLOAT_3
_INDEX.fields_by_name['AskPrice2'].message_type = _FLOAT_3
_INDEX.fields_by_name['AskPrice3'].message_type = _FLOAT_3
_INDEX_MID.containing_type = _INDEX;
_INDEX_SID.containing_type = _INDEX;
_INDEX_VID.containing_type = _INDEX;
DESCRIPTOR.message_types_by_name['float_3'] = _FLOAT_3
DESCRIPTOR.message_types_by_name['Index'] = _INDEX

class float_3(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FLOAT_3

  # @@protoc_insertion_point(class_scope:datayes.mdl.mdl_swg_pbmsg.float_3)

class Index(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INDEX

  # @@protoc_insertion_point(class_scope:datayes.mdl.mdl_swg_pbmsg.Index)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'B\tMDLSWGMsg')
# @@protoc_insertion_point(module_scope)
