import os

import requests
import re
import m3u8
from Crypto.Cipher import AES


# EXTM3U
# EXT-X-VERSION:3
# EXT-X-TARGETDURATION:2
# EXT-X-PLAYLIST-TYPE:VOD
# EXT-X-MEDIA-SEQUENCE:0
# EXT-X-KEY:METHOD=AES-128,URI="https://9dzh34ee91.motorjn.com/20221217/YHDG4OBP/4000kb/hls/key.key"
# EXTINF:1,
# https://9dzh34ee91.motorjn.com/20221217/YHDG4OBP/4000kb/hls/B7GmKpMa.ts
# EXTINF:1,
# https://9dzh34ee91.motorjn.com/20221217/YHDG4OBP/4000kb/hls/QHl2YRNw.ts
# EXTINF:1,
# https://9dzh34ee91.motorjn.com/20221217/YHDG4OBP/4000kb/hls/dfI7vqSL.ts
# EXTINF:1,
# https://9dzh34ee91.motorjn.com/20221217/YHDG4OBP/4000kb/hls/H1bqPNdf.ts
# EXT-X-ENDLIST

def network():
    url = 'https://0yefiks35y.motorjn.com/20221109/aSgcm11j/index.m3u8'
    content = requests.get(url).text
    print(content)
    if '#EXTM3U' not in content:
        print('这不是m3u8视频链接')
        return False
    # list_content  = ts_rs.split('\n')
    # 使用re正则得到key和视频地址
    jiami = re.findall('#EXT-X-KEY:(.*)\n', content)
    key = re.findall('URI="(.*)"', jiami[0])

    # 得到每一个ts视频链接
    tslist = re.findall('EXTINF:(.*)\n(.*)\n#', content)
    newlist = []
    for i in tslist:
        newlist.append(i[1])

    keycontent = requests.get(key[0]).text
    print(keycontent)

    cryptor = AES.new(keycontent.encode(), AES.MODE_CBC)
    if os.path.exists('xx.mp4'):
        print('删除旧的mp4文件')
        os.remove('xx.mp4')

    index = 0
    print('一共%d个ts文件' % len(newlist))
    for i in newlist:
        res = requests.get(i).content
        cont = cryptor.decrypt(res)
        index = index + 1
        with open('xx.mp4', 'ab+') as f:
            f.write(cont)
            print('写入%d/%d' % (index, len(newlist)))


if __name__ == '__main__':
    network()
