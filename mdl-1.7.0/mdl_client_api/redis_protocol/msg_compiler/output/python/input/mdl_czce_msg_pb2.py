# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: input/mdl_czce_msg.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='input/mdl_czce_msg.proto',
  package='datayes.mdl.mdl_czce_pbmsg',
  serialized_pb='\n\x18input/mdl_czce_msg.proto\x12\x1a\x64\x61tayes.mdl.mdl_czce_pbmsg\"5\n\x08\x64ouble_3\x12\r\n\x05Value\x18\x01 \x02(\x03\x12\x1a\n\x0c\x44\x65\x63imalShift\x18\x02 \x01(\r:\x04\x31\x30\x30\x30\"\xc5\x0e\n\tCTPFuture\x12\x10\n\x08InstruID\x18\x01 \x01(\t\x12\x37\n\tLastPrice\x18\x02 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x39\n\x0bPreSetPrice\x18\x03 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x37\n\tOpenPrice\x18\x04 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x37\n\tHighPrice\x18\x05 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x36\n\x08LowPrice\x18\x06 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x36\n\x08Turnover\x18\x07 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x35\n\x07OpenInt\x18\x08 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x36\n\x08SetPrice\x18\t \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x39\n\x0bULimitPrice\x18\n \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x39\n\x0bLLimitPrice\x18\x0b \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x0f\n\x07TradDay\x18\x0c \x01(\r\x12\x39\n\x0bPreCloPrice\x18\r \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x0e\n\x06Volume\x18\x0e \x01(\x05\x12\x38\n\nClosePrice\x18\x0f \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x36\n\x08PreDelta\x18\x10 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x37\n\tCurrDelta\x18\x11 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x12\n\nUpdateTime\x18\x12 \x01(\r\x12\x38\n\nPreOpenInt\x18\x13 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x37\n\tBidPrice1\x18\x14 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x12\n\nBidVolume1\x18\x15 \x01(\x05\x12\x37\n\tAskPrice1\x18\x16 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x12\n\nAskVolume1\x18\x17 \x01(\x05\x12\x37\n\tBidPrice2\x18\x18 \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x12\n\nBidVolume2\x18\x19 \x01(\x05\x12\x37\n\tAskPrice2\x18\x1a \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x12\n\nAskVolume2\x18\x1b \x01(\x05\x12\x37\n\tBidPrice3\x18\x1c \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x12\n\nBidVolume3\x18\x1d \x01(\x05\x12\x37\n\tAskPrice3\x18\x1e \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x12\n\nAskVolume3\x18\x1f \x01(\x05\x12\x37\n\tBidPrice4\x18  \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x12\n\nBidVolume4\x18! \x01(\x05\x12\x37\n\tAskPrice4\x18\" \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x12\n\nAskVolume4\x18# \x01(\x05\x12\x37\n\tBidPrice5\x18$ \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x12\n\nBidVolume5\x18% \x01(\x05\x12\x37\n\tAskPrice5\x18& \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x12\n\nAskVolume5\x18\' \x01(\x05\x12:\n\x0c\x41veragePrice\x18( \x01(\x0b\x32$.datayes.mdl.mdl_czce_pbmsg.double_3\x12\x11\n\tActionDay\x18) \x01(\r\"\x14\n\x03MID\x12\r\n\tMessageID\x10\x01\"\x14\n\x03SID\x12\r\n\tServiceID\x10\x08\"\x19\n\x03VID\x12\x12\n\x0eServiceVersion\x10\x65*,\n\x15MDLCZCEServiceVersion\x12\x13\n\x0fMDLVID_MDL_CZCE\x10\x65*1\n\x10MDLCZCEMessageID\x12\x1d\n\x19MDLMID_MDL_CZCE_CTPFuture\x10\x01\x42\x0c\x42\nMDLCZCEMsg')

_MDLCZCESERVICEVERSION = _descriptor.EnumDescriptor(
  name='MDLCZCEServiceVersion',
  full_name='datayes.mdl.mdl_czce_pbmsg.MDLCZCEServiceVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MDLVID_MDL_CZCE', index=0, number=101,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1975,
  serialized_end=2019,
)

MDLCZCEServiceVersion = enum_type_wrapper.EnumTypeWrapper(_MDLCZCESERVICEVERSION)
_MDLCZCEMESSAGEID = _descriptor.EnumDescriptor(
  name='MDLCZCEMessageID',
  full_name='datayes.mdl.mdl_czce_pbmsg.MDLCZCEMessageID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MDLMID_MDL_CZCE_CTPFuture', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2021,
  serialized_end=2070,
)

MDLCZCEMessageID = enum_type_wrapper.EnumTypeWrapper(_MDLCZCEMESSAGEID)
MDLVID_MDL_CZCE = 101
MDLMID_MDL_CZCE_CTPFuture = 1


_CTPFUTURE_MID = _descriptor.EnumDescriptor(
  name='MID',
  full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.MID',
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
  serialized_start=1904,
  serialized_end=1924,
)

_CTPFUTURE_SID = _descriptor.EnumDescriptor(
  name='SID',
  full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.SID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ServiceID', index=0, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1926,
  serialized_end=1946,
)

_CTPFUTURE_VID = _descriptor.EnumDescriptor(
  name='VID',
  full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.VID',
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
  serialized_start=1948,
  serialized_end=1973,
)


_DOUBLE_3 = _descriptor.Descriptor(
  name='double_3',
  full_name='datayes.mdl.mdl_czce_pbmsg.double_3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Value', full_name='datayes.mdl.mdl_czce_pbmsg.double_3.Value', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DecimalShift', full_name='datayes.mdl.mdl_czce_pbmsg.double_3.DecimalShift', index=1,
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
  serialized_start=56,
  serialized_end=109,
)


_CTPFUTURE = _descriptor.Descriptor(
  name='CTPFuture',
  full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='InstruID', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.InstruID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LastPrice', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.LastPrice', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PreSetPrice', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.PreSetPrice', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OpenPrice', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.OpenPrice', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HighPrice', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.HighPrice', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LowPrice', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.LowPrice', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Turnover', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.Turnover', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OpenInt', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.OpenInt', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SetPrice', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.SetPrice', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ULimitPrice', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.ULimitPrice', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LLimitPrice', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.LLimitPrice', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TradDay', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.TradDay', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PreCloPrice', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.PreCloPrice', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Volume', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.Volume', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ClosePrice', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.ClosePrice', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PreDelta', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.PreDelta', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CurrDelta', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.CurrDelta', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UpdateTime', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.UpdateTime', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PreOpenInt', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.PreOpenInt', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidPrice1', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.BidPrice1', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidVolume1', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.BidVolume1', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskPrice1', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.AskPrice1', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskVolume1', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.AskVolume1', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidPrice2', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.BidPrice2', index=23,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidVolume2', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.BidVolume2', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskPrice2', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.AskPrice2', index=25,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskVolume2', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.AskVolume2', index=26,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidPrice3', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.BidPrice3', index=27,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidVolume3', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.BidVolume3', index=28,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskPrice3', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.AskPrice3', index=29,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskVolume3', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.AskVolume3', index=30,
      number=31, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidPrice4', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.BidPrice4', index=31,
      number=32, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidVolume4', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.BidVolume4', index=32,
      number=33, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskPrice4', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.AskPrice4', index=33,
      number=34, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskVolume4', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.AskVolume4', index=34,
      number=35, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidPrice5', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.BidPrice5', index=35,
      number=36, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BidVolume5', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.BidVolume5', index=36,
      number=37, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskPrice5', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.AskPrice5', index=37,
      number=38, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AskVolume5', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.AskVolume5', index=38,
      number=39, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AveragePrice', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.AveragePrice', index=39,
      number=40, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ActionDay', full_name='datayes.mdl.mdl_czce_pbmsg.CTPFuture.ActionDay', index=40,
      number=41, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CTPFUTURE_MID,
    _CTPFUTURE_SID,
    _CTPFUTURE_VID,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=112,
  serialized_end=1973,
)

_CTPFUTURE.fields_by_name['LastPrice'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['PreSetPrice'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['OpenPrice'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['HighPrice'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['LowPrice'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['Turnover'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['OpenInt'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['SetPrice'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['ULimitPrice'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['LLimitPrice'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['PreCloPrice'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['ClosePrice'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['PreDelta'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['CurrDelta'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['PreOpenInt'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['BidPrice1'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['AskPrice1'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['BidPrice2'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['AskPrice2'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['BidPrice3'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['AskPrice3'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['BidPrice4'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['AskPrice4'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['BidPrice5'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['AskPrice5'].message_type = _DOUBLE_3
_CTPFUTURE.fields_by_name['AveragePrice'].message_type = _DOUBLE_3
_CTPFUTURE_MID.containing_type = _CTPFUTURE;
_CTPFUTURE_SID.containing_type = _CTPFUTURE;
_CTPFUTURE_VID.containing_type = _CTPFUTURE;
DESCRIPTOR.message_types_by_name['double_3'] = _DOUBLE_3
DESCRIPTOR.message_types_by_name['CTPFuture'] = _CTPFUTURE

class double_3(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DOUBLE_3

  # @@protoc_insertion_point(class_scope:datayes.mdl.mdl_czce_pbmsg.double_3)

class CTPFuture(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CTPFUTURE

  # @@protoc_insertion_point(class_scope:datayes.mdl.mdl_czce_pbmsg.CTPFuture)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'B\nMDLCZCEMsg')
# @@protoc_insertion_point(module_scope)
