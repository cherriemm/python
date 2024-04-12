#!/usr/bin/python
# -*- coding:UTF-8 -*-
import struct


# 题目十七：二进制数据报文构建与解析
def pack_message(data_dict):
    type = data_dict['type']
    csum = data_dict['csum']
    id = data_dict['id'].encode("utf-8")
    dis1 = data_dict['dis1']
    dis2 = data_dict['dis2']
    count = data_dict['count']
    if (data_dict and type and csum and id and dis1 and dis2 and count) == 0:
        return "Parameter Error."
    msg = struct.pack(
        ">BB16sIIB" , type, csum, id, dis1, dis2, count
    )
    return msg


def unpack_message(message):
    msg = struct.unpack(
        ">BB16sIIB", message
    )
    dic = {}
    key = ['type', 'csum', 'id', 'dis1', 'dis2', 'count']
    for i in range(len(msg)):
        if key[i] == 'id' :
            dic['id'] = msg[i].decode("utf-8")
        else:
            dic[key[i]] = msg[i]


    return dic


if __name__ == "__main__":
    data_dict = {'type': 50, 'csum': 1, 'id': 'abcdefghigklmnop', 'dis1': 300, 'dis2': 100, 'count': 20}
    data = pack_message(data_dict)