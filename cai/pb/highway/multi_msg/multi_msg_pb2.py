# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cai/pb/highway/multi_msg/multi_msg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(cai/pb/highway/multi_msg/multi_msg.proto\" \n\tExternMsg\x12\x13\n\x0b\x63hannelType\x18\x01 \x01(\x05\"I\n\x14MultiMsgApplyDownReq\x12\x10\n\x08msgResid\x18\x01 \x01(\x0c\x12\x0f\n\x07msgType\x18\x02 \x01(\x05\x12\x0e\n\x06srcUin\x18\x03 \x01(\x03\"\xe1\x01\n\x14MultiMsgApplyDownRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x15\n\rthumbDownPara\x18\x02 \x01(\x0c\x12\x0e\n\x06msgKey\x18\x03 \x01(\x0c\x12\x14\n\x0cuint32DownIp\x18\x04 \x03(\x05\x12\x16\n\x0euint32DownPort\x18\x05 \x03(\x05\x12\x10\n\x08msgResid\x18\x06 \x01(\x0c\x12!\n\rmsgExternInfo\x18\x07 \x01(\x0b\x32\n.ExternMsg\x12\x15\n\rbytesDownIpV6\x18\x08 \x03(\x0c\x12\x18\n\x10uint32DownV6Port\x18\t \x03(\x05\"g\n\x12MultiMsgApplyUpReq\x12\x0e\n\x06\x64stUin\x18\x01 \x01(\x03\x12\x0f\n\x07msgSize\x18\x02 \x01(\x03\x12\x0e\n\x06msgMd5\x18\x03 \x01(\x0c\x12\x0f\n\x07msgType\x18\x04 \x01(\x05\x12\x0f\n\x07\x61pplyId\x18\x05 \x01(\x05\"\x97\x02\n\x12MultiMsgApplyUpRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x10\n\x08msgResid\x18\x02 \x01(\t\x12\x0f\n\x07msgUkey\x18\x03 \x01(\x0c\x12\x12\n\nuint32UpIp\x18\x04 \x03(\x05\x12\x14\n\x0cuint32UpPort\x18\x05 \x03(\x05\x12\x11\n\tblockSize\x18\x06 \x01(\x03\x12\x10\n\x08upOffset\x18\x07 \x01(\x03\x12\x0f\n\x07\x61pplyId\x18\x08 \x01(\x05\x12\x0e\n\x06msgKey\x18\t \x01(\x0c\x12\x0e\n\x06msgSig\x18\n \x01(\x0c\x12!\n\rmsgExternInfo\x18\x0b \x01(\x0b\x32\n.ExternMsg\x12\x13\n\x0b\x62ytesUpIpV6\x18\x0c \x03(\x0c\x12\x16\n\x0euint32UpV6Port\x18\r \x03(\x05\"\xf7\x01\n\x0cMultiReqBody\x12\x0e\n\x06subcmd\x18\x01 \x01(\x05\x12\x10\n\x08termType\x18\x02 \x01(\x05\x12\x14\n\x0cplatformType\x18\x03 \x01(\x05\x12\x0f\n\x07netType\x18\x04 \x01(\x05\x12\x10\n\x08\x62uildVer\x18\x05 \x01(\t\x12/\n\x12multimsgApplyupReq\x18\x06 \x03(\x0b\x32\x13.MultiMsgApplyUpReq\x12\x33\n\x14multimsgApplydownReq\x18\x07 \x03(\x0b\x32\x15.MultiMsgApplyDownReq\x12\x0e\n\x06\x62uType\x18\x08 \x01(\x05\x12\x16\n\x0ereqChannelType\x18\t \x01(\x05\"\x84\x01\n\x0cMultiRspBody\x12\x0e\n\x06subcmd\x18\x01 \x01(\x05\x12/\n\x12multimsgApplyupRsp\x18\x02 \x03(\x0b\x32\x13.MultiMsgApplyUpRsp\x12\x33\n\x14multimsgApplydownRsp\x18\x03 \x03(\x0b\x32\x15.MultiMsgApplyDownRspB.Z,github.com/Mrs4s/MiraiGo/client/pb/multi_msgb\x06proto3')



_EXTERNMSG = DESCRIPTOR.message_types_by_name['ExternMsg']
_MULTIMSGAPPLYDOWNREQ = DESCRIPTOR.message_types_by_name['MultiMsgApplyDownReq']
_MULTIMSGAPPLYDOWNRSP = DESCRIPTOR.message_types_by_name['MultiMsgApplyDownRsp']
_MULTIMSGAPPLYUPREQ = DESCRIPTOR.message_types_by_name['MultiMsgApplyUpReq']
_MULTIMSGAPPLYUPRSP = DESCRIPTOR.message_types_by_name['MultiMsgApplyUpRsp']
_MULTIREQBODY = DESCRIPTOR.message_types_by_name['MultiReqBody']
_MULTIRSPBODY = DESCRIPTOR.message_types_by_name['MultiRspBody']
ExternMsg = _reflection.GeneratedProtocolMessageType('ExternMsg', (_message.Message,), {
  'DESCRIPTOR' : _EXTERNMSG,
  '__module__' : 'cai.pb.highway.multi_msg.multi_msg_pb2'
  # @@protoc_insertion_point(class_scope:ExternMsg)
  })
_sym_db.RegisterMessage(ExternMsg)

MultiMsgApplyDownReq = _reflection.GeneratedProtocolMessageType('MultiMsgApplyDownReq', (_message.Message,), {
  'DESCRIPTOR' : _MULTIMSGAPPLYDOWNREQ,
  '__module__' : 'cai.pb.highway.multi_msg.multi_msg_pb2'
  # @@protoc_insertion_point(class_scope:MultiMsgApplyDownReq)
  })
_sym_db.RegisterMessage(MultiMsgApplyDownReq)

MultiMsgApplyDownRsp = _reflection.GeneratedProtocolMessageType('MultiMsgApplyDownRsp', (_message.Message,), {
  'DESCRIPTOR' : _MULTIMSGAPPLYDOWNRSP,
  '__module__' : 'cai.pb.highway.multi_msg.multi_msg_pb2'
  # @@protoc_insertion_point(class_scope:MultiMsgApplyDownRsp)
  })
_sym_db.RegisterMessage(MultiMsgApplyDownRsp)

MultiMsgApplyUpReq = _reflection.GeneratedProtocolMessageType('MultiMsgApplyUpReq', (_message.Message,), {
  'DESCRIPTOR' : _MULTIMSGAPPLYUPREQ,
  '__module__' : 'cai.pb.highway.multi_msg.multi_msg_pb2'
  # @@protoc_insertion_point(class_scope:MultiMsgApplyUpReq)
  })
_sym_db.RegisterMessage(MultiMsgApplyUpReq)

MultiMsgApplyUpRsp = _reflection.GeneratedProtocolMessageType('MultiMsgApplyUpRsp', (_message.Message,), {
  'DESCRIPTOR' : _MULTIMSGAPPLYUPRSP,
  '__module__' : 'cai.pb.highway.multi_msg.multi_msg_pb2'
  # @@protoc_insertion_point(class_scope:MultiMsgApplyUpRsp)
  })
_sym_db.RegisterMessage(MultiMsgApplyUpRsp)

MultiReqBody = _reflection.GeneratedProtocolMessageType('MultiReqBody', (_message.Message,), {
  'DESCRIPTOR' : _MULTIREQBODY,
  '__module__' : 'cai.pb.highway.multi_msg.multi_msg_pb2'
  # @@protoc_insertion_point(class_scope:MultiReqBody)
  })
_sym_db.RegisterMessage(MultiReqBody)

MultiRspBody = _reflection.GeneratedProtocolMessageType('MultiRspBody', (_message.Message,), {
  'DESCRIPTOR' : _MULTIRSPBODY,
  '__module__' : 'cai.pb.highway.multi_msg.multi_msg_pb2'
  # @@protoc_insertion_point(class_scope:MultiRspBody)
  })
_sym_db.RegisterMessage(MultiRspBody)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/Mrs4s/MiraiGo/client/pb/multi_msg'
  _EXTERNMSG._serialized_start=44
  _EXTERNMSG._serialized_end=76
  _MULTIMSGAPPLYDOWNREQ._serialized_start=78
  _MULTIMSGAPPLYDOWNREQ._serialized_end=151
  _MULTIMSGAPPLYDOWNRSP._serialized_start=154
  _MULTIMSGAPPLYDOWNRSP._serialized_end=379
  _MULTIMSGAPPLYUPREQ._serialized_start=381
  _MULTIMSGAPPLYUPREQ._serialized_end=484
  _MULTIMSGAPPLYUPRSP._serialized_start=487
  _MULTIMSGAPPLYUPRSP._serialized_end=766
  _MULTIREQBODY._serialized_start=769
  _MULTIREQBODY._serialized_end=1016
  _MULTIRSPBODY._serialized_start=1019
  _MULTIRSPBODY._serialized_end=1151
# @@protoc_insertion_point(module_scope)
