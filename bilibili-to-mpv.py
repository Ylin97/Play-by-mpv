#! /usr/bin/python
# coding=utf-8


import os
import sys
# import subprocess

# get cookies includeing real URL
def get_cookies(raw_url):
    cmd = 'you-get -u ' + raw_url + '>' + data_dir
    os.system(cmd)


# get command string for mpv
def cmd_str(url_list, site_address):
    cmd = 'mpv '
    count = len(url_list)
    if 1 == count:
        cmd += url_list[0] + " --referrer='{}'".format(site_address) + " --no-ytdl"
    else:
        cmd += url_list[0]
        i = 1
        while i < count - 1:
            cmd += ',' + url_list[i]
            i += 1
        cmd += ' --audio-file=' + url_list[count - 1] + " --referrer='{}'".format(site_address) + " --no-ytdl"
        # cmd += ' --audio-file=' + url_list[count - 1] + " --no-ytdl"
    return cmd 


# TODO: download subtitle from video website
def get_subtile():
    pass


def main():
    if len(sys.argv) < 2:
        print("[参数错误]\nUsage: ./play-to-mpv.py <url>")
        exit()
    get_cookies(sys.argv[1])
    # get website's address
    tmp_list = sys.argv[1].split('/')
    site_address = tmp_list[0] + '/' + tmp_list[1] + '/' + tmp_list[2]


    # with open('./data.txt', 'r') as cookie:
    with open(data_dir, 'r') as cookie:
        url_list = [] # video and audio url
        for x in cookie.readlines():
            x = x.strip("[]\'")
            if len(x) > 8 and x[:8] == 'https://' or x[:7] == 'http://':
                url_list.append(repr(x))
    
    cmd = cmd_str(url_list, site_address)
    os.system(cmd)


if __name__ == '__main__':
    # get directory of data.txt
    data_dir = os.path.join('.', 'data.txt')
    # print(data_dir)
    main()

# https://www.bilibili.com/bangumi/play/ss38233
