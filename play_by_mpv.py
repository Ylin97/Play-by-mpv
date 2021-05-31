#! /usr/bin/python
# coding=utf-8


import os
import sys
# import subprocess




def read_config():

    global CACHE_SIZE
    config_address = os.path.join('.', 'config.conf')
    with open(config_address, 'r', encoding='utf-8') as config:
        config_list = config.readlines()
        for x in config_list:
            tmp_list = x.split()
            if tmp_list[0] == 'cache_size' and len(tmp_list) == 3 and tmp_list[2].isdigit():
                CACHE_SIZE = int(tmp_list[2])
    # print(CACHE_SIZE)


def write_cache(raw_url, cmd):

    raw_url = raw_url.strip('/')
    cache_address = os.path.join('.', '.cache')
    
    with open(cache_address, 'r', encoding='utf-8') as cache:
        cache_url_list = cache.readlines()

    cache_size_current = len(cache_url_list)
    if cache_size_current == CACHE_SIZE:
        cache_url_list.pop()

    with open(cache_address, 'w', encoding='utf-8') as cache:
        new = 'url@@' + raw_url.strip('/') + '|cmd@@' + cmd.strip()
        cache.write("%s%s" % (new, os.linesep))
        for x in cache_url_list:
            cache.write("%s%s" % (x.strip(), os.linesep))

    
# get cookies includeing real URL
def get_cookies(raw_url):

    global is_existed

    raw_url = raw_url.strip('/')
    cache_address = os.path.join('.', '.cache')

    try:
        cache = open(cache_address, 'r', encoding='utf-8')
        cache_url_list = cache.readlines()
    except FileNotFoundError:
        cache = open(cache_address, 'w', encoding='utf-8')
        cache_url_list = []
    except Exception as ex:
        print('Unknown Error: {}'.format(ex))
        exit()
    finally:
        cache.close()
    
    for x in cache_url_list:
        pos1 = x.find('url@@')
        pos2 = x.find('|cmd@@')
        tmp_url = x[pos1 + 5:pos2]
        # tmp_cmd = x[pos2 + 6:]
        if raw_url == tmp_url:
            is_existed = True
            if is_play_ok:
                cmd = x[pos2 + 6:]
                return cmd
            else:
                cache_url_list.remove(x)
                with open(cache_address, 'w', encoding='utf-8') as cache:
                    for x in cache_url_list:
                        cache.write("%s%s" % (x.strip(), os.linesep))
                        
    cmd_you_get = 'you-get -u ' + raw_url + '>' + data_dir
    os.system(cmd_you_get)
    return None


# get command string for mpv
def cmd_str(url_list, site_address):
    cmd = 'mpv ' + '"'
    count = len(url_list)
    if 1 == count:
        cmd += url_list[0] + '"' + ' --referrer="{}"'.format(site_address) + " --no-ytdl"
    else:
        cmd += url_list[0] + '"'
        i = 1
        while i < count - 1:
            cmd += ',' + url_list[i]
            i += 1
        cmd +=' --audio-file=' + '"' + url_list[count - 1] + '"' + " --referrer='{}'".format(site_address) + " --no-ytdl"
        # cmd += ' --audio-file=' + url_list[count - 1] + " --no-ytdl"
    return cmd 


# TODO: download subtitle from video website
def get_subtile():
    pass


def main():

    global is_play_ok

    read_config()

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
    CACHE_SIZE = 30
    is_existed = False
    is_play_ok = True
    main()


# https://www.bilibili.com/bangumi/play/ss38233
