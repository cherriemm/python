# -*- coding: UTF-8 -*-

import base64

#题目十五：Base64编解码
def b64en(path_in, path_out):
    with open(path_in, 'rb')  as file_object:
        binary = file_object.read()
        indexOfBase64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        base64String = ''
        IndexOfLastTriple = len(binary) // 3 * 3
        for i in range(0, IndexOfLastTriple,3):
            idx1 = binary[i] >> 2
            idx2 = ((binary[i] & 0x3) << 4) | ((binary[i+1] & 0xF0) >> 4)
            idx3 = ((binary[i+1] & 0x0F) << 2) | ((binary[i+2] & 0xC0) >> 6)
            idx4 = binary[i+2] & 0x3F
            base64String += indexOfBase64[idx1]
            base64String += indexOfBase64[idx2]
            base64String += indexOfBase64[idx3]
            base64String += indexOfBase64[idx4]

        i += 3
        if i == len(binary) - 1:
            # one character left
            idx1 = binary[i] >> 2
            idx2 = (binary[i] & 0x3) << 4
            base64String += indexOfBase64[idx1]
            base64String += indexOfBase64[idx2]
            base64String += "=="

        elif i == len(binary) -2:
            idx1 = binary[i] >> 2
            idx2 = ((binary[i] & 0x3) << 4) | ((binary[i+1] & 0xF0) >>4)
            idx3 = (binary[i+1]& 0x0F )<< 2
            base64String += indexOfBase64[idx1]
            base64String += indexOfBase64[idx2]
            base64String += indexOfBase64[idx3]
            base64String += "="

        with open(path_out, 'w') as fb:
            fb.write(base64String)



def b64de(path_in, path_out):
    with open(path_in) as file_object:
        Todecode = file_object.read()
        num = (len(Todecode) // 4 - 1) * 4
        decodestr=bytes()
        l = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80,
    80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80,
    80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 62, 80, 80, 80, 63,
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 80, 80, 80, 64, 80, 80,
    80,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 80, 80, 80, 80, 80,
    80, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 80, 80, 80, 80, 80]

        for i in range(0, num, 4):
            c1 = l[ord(Todecode[i])]
            c2 = l[ord(Todecode[i+1])]
            c3 = l[ord(Todecode[i+2])]
            c4 = l[ord(Todecode[i+3])]

            a1 = ((c1 << 2) | ((c2 & 0xF0) >> 4)).to_bytes()
            a2 = (((c2 & 0x0F) << 4) | ((c3 & 0x3c) >> 2)).to_bytes()
            a3 = (((c3 & 0x3) << 6 | c4 )).to_bytes()
            decodestr += a1
            decodestr += a2
            decodestr += a3

        i += 4
        c1 = l[ord(Todecode[i])]
        c2 = l[ord(Todecode[i + 1])]
        a1 = ((c1 << 2) | ((c2 & 0xF0) >> 4)).to_bytes()
        decodestr += a1
        if Todecode[i+3] == '=':
            if Todecode[i+2] != '=':
                c3 = l[ord(Todecode[i + 2])]
                a2 = (((c2 & 0x0F) << 4) | ((c3 & 0x3c) >> 2)).to_bytes()
                decodestr += a2
        else :
            c3 = l[ord(Todecode[i + 2])]
            c4 = l[ord(Todecode[i + 3])]
            a2 = (((c2 & 0x0F) << 4) | ((c3 & 0x3c) >> 2)).to_bytes()
            a3 = (((c3 & 0x3) << 6 | c4)).to_bytes()
            decodestr += a2
            decodestr += a3


        with open(path_out, 'wb') as fo:
            fo.write(decodestr)




if __name__ == '__main__':
    b64en("./pic.jpg", "./pic_en.txt")
    b64de("./pic_en.txt", "./pic_de.jpg")
