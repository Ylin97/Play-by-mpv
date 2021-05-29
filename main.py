#! /usr/bin/python
# coding=utf-8


import os


def get_cookies(raw_url):
    # with open('./data.txt', 'w') as cookie:
    cmd = 'you-get c '



def string_format(raw_str):
    i = 0
    str_len = len(raw_str)
    result_string = ''
    while i < str_len:
        if raw_str[i] == '=' or raw_str[i] == '?' or raw_str[i] == '&':
            result_string += '\\' + raw_str[i]
        else:
            result_string += raw_str[i]
        
        i += 1

    return repr(raw_str)


def cmd_str(url_list):
    cmd = 'mpv '
    count = len(url_list)
    # cmd += repr(url_list[0])
    cmd += url_list[0]
    i = 1
    while i < count - 1:
        # cmd += ',' + repr(url_list[i])
        cmd += ',' + url_list[i]
        i += 1
    # cmd += ' --audio-file=' + repr(url_list[count - 1]) + " --referrer='https://www.bilibili.com' --no-ytdl"
    cmd += ' --audio-file=' + url_list[count - 1] + " --referrer='https://www.bilibili.com' --no-ytdl"
    return cmd 


def main():

    with open('./data.txt', 'r') as cookie:
        url_list = [] # video and audio url
        for x in cookie.readlines():
            if len(x) > 8 and x[:8] == 'https://':
                # x = string_format(x)
                url_list.append(repr(x.strip()))
    
    cmd = cmd_str(url_list)
    # print(cmd)
    os.system(cmd)


def test():
    with open('./data.txt', 'r') as cookie:
        url_list = [] # video and audio url
        for x in cookie.readlines():
            if len(x) > 8 and x[:8] == 'https://':
                url_list.append(x)
    for x in url_list:
        print(x)

if __name__ == '__main__':
    main()
    # test()

    
