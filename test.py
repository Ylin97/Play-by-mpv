#! /usr/bin/python
# coding=utf-8

import os 
import sys
from play_by_mpv import *


# test command
def test_cmd():
    cmd = 'mpv '
    cmd += """https://xy111x78x163x90xy.mcdn.bilivideo.cn:4483
    /upgcxcode/77/69/337086977/337086977-1-30077.m4s\?e\=ig8eu
    xZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_Y
    N0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02
    J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0
    eN0B599M\=\&uipk\=5\&nbs\=1\&deadline\=1622299972\&gen\=playu
    rlv2\&os\=mcdn\&oi\=2936350555\&trid\=0001217188d0854d49d38318d0
    a222f0857ap\&platform\=pc\&upsig\=23172bdc301ed1558c71d8b3
    28c5c79e\&uparams\=e,uipk,nbs,deadline,gen,os,oi,trid,plat
    form\&mcdnid\=2000558\&mid\=0\&bvc\=vod\&orderid\=0,3\&agr
    r\=0\&logo\=A0000002 audio-file=https://xy182x105x223x218x
    y.mcdn.bilivideo.cn:4483/upgcxcode/77/69/337086977/3370869
    77_nb2-1-30280.m4s\?e\=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBv
    EqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5t
    ZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7
    MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M\=\&uipk\=5\&nbs\=
    1\&deadline\=1622299972\&gen\=playurlv2\&os\=mcdn\&oi\=293
    6350555\&trid\=0001217188d0854d49d38318d0a222f0857ap\&plat
    form\=pc\&upsig\=bdf425d90bb49af0782c2ed28f4e0914\&uparam
    s\=e,uipk,nbs,deadline,gen,os,oi,trid,platform\&mcdnid\=20
    00691\&mid\=0\&bvc\=vod\&orderid\=0,3\&agrr\=0\&logo\=A000
    0002 --referrer=https://www.bilibili.com --no-ytdl'
    """
    os.system(cmd)


def test():
    
    global is_play_ok

    if len(sys.argv) < 2:
        print("[参数错误]\nUsage: ./play-to-mpv.py <url>")
        exit()
    # delete space characters for raw video url from head and end
    raw_url = sys.argv[1].strip()

    cmd = get_cookies(raw_url)
    if cmd:
        if os.system(cmd) != 0: # existent url is invalid
            is_play_ok = False
            get_cookies(raw_url)
        else:
            return 
    
    # get website's address
    tmp_list = raw_url.split('/')
    site_address = tmp_list[0] + '/' + tmp_list[1] + '/' + tmp_list[2] + '/'

    with open(data_dir, 'r', encoding='utf-8') as cookie:
        url_list = [] # video and audio url
        for x in cookie.readlines():
            x = x.strip("[]\'")
            if len(x) > 8 and x[:8] == 'https://' or x[:7] == 'http://':
                url_list.append(x.strip())
    
    cmd = cmd_str(url_list, site_address)
    # print('cmd2: ' + cmd)
    if os.system(cmd) == 0:
        write_cache(raw_url, cmd)


if __name__ == '__main__':
    # get directory of data.txt
    data_dir = os.path.join('.', 'data.txt')
    # print(data_dir)
    is_existed = False
    is_play_ok = True
    test()