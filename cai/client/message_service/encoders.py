import random

from typing import Sequence, TYPE_CHECKING, Dict, Type
from cai.pb.im.msg.msg_body import MsgBody, PlainText, RichText, CustomFace, Elem
from cai.pb.msf.msg.svc.svc_pb2 import PbSendMsgReq, RoutingHead, Grp
from cai.pb.msf.msg.comm.comm_pb2 import ContentHead
from cai.client.packet import UniPacket

from . import models
from ...pb.msf.msg.svc import PbSendMsgReq

if TYPE_CHECKING:
    from cai.client.client import Client


# todo: https://github.com/mamoe/mirai/blob/7d3971259de59cede94b7a55650c8a6ad4346a59/mirai-core/src/commonMain/kotlin/network/protocol/packet/chat/receive/MessageSvc.PbSendMsg.kt#L103
# https://github.com/mamoe/mirai/blob/74fc5a50376ed0330b984af51e0fabc2147afdbb/mirai-core/src/commonMain/kotlin/contact/SendMessageHandler.kt

def build_msg(elements: Sequence[models.Element]) -> MsgBody:
    ret = []
    for e in elements:  # todo: support more element
        if isinstance(e, models.TextElement):
            ret.append(
                Elem(text=PlainText(str=e.content.encode()))
            )
        elif isinstance(e, models.ImageElement):
            ret.append(
                Elem(
                    custom_face=CustomFace(
                        file_type=66,
                        useful=1,
                        biz_type=0, #5
                        width=e.width,
                        height=e.height,
                        file_id=e.id,
                        file_path=e.filename,
                        image_type=e.filetype,
                        origin=1,
                        size=e.size,
                        md5=e.md5,
                        flag=b"\x00\x00\x00\x00"
                    )
                )
            )
        else:
            raise NotImplementedError(e)

    d = MsgBody(
        rich_text=RichText(
            #elems=[Elem(text=e) for e in ret],
            elems=ret,
            ptt=None
        )
    )
    print(d.SerializeToString().hex())
    return d


def encode_send_group_msg_req(
    seq: int, group: int, body: MsgBody, head: ContentHead
) -> PbSendMsgReq:
    return PbSendMsgReq(
        routing_head=RoutingHead(grp=Grp(group_code=group)),
        content_head=head,
        body=body,
        seq=seq,
        rand=random.randrange(3000, 30000),
        via=0
    )


def make_group_msg_pkg(seq: int, gid: int, body: MsgBody) -> PbSendMsgReq:
    return encode_send_group_msg_req(
        seq, gid, body, ContentHead(pkg_num=1, pkg_index=0, div_seq=0)
    )
