import sys
import requests
import os
import json
import re
from bs4 import BeautifulSoup
from moviepy.editor import VideoFileClip
from lxml import *
import urllib.request
import urllib.request
import urllib.parse
import random
import base64
import time
import multiprocessing
import threading
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import *
import ffmpeg
import youtube_dl
import webbrowser
import winreg
import tkinter as tk
from tkinter import filedialog

class Douyin_Crawler(object):
    def __init__(self):
        self.url = share_url_list
        self.m3u8_real_url
        self.m3u8_real_url_list = []
        self.path = path

    def download_audio(self)->list:
        for each_url in self.url:
            response = requests.get(each_url)
            # 获取headers
            headers = response.headers
            session = requests.session()
            # 获取cookie
            session.get(each_url, headers=headers)
            # 携带cookie连接地址
            response = session.get(each_url, headers=headers)
            response.encoding = 'utf-8'
            data = response.text
            # 匹配获取么m3u8地址
            m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')
            # 获取m3u8文件
            response = session.get(m3u8_url, headers=headers)
            response.encoding = 'utf-8'
            data = response.text
            # 获取m3u8文件的真实地址
            self.m3u8_resl_url = data.split('/', 3)[-1].strip()
            self.m3u8_resl_url = urljoin(m3u8_url, self.m3u8_resl_url)
            self.m3u8_real_url_list.append(self.m3u8_real_url)
        # 创建文件保存路径
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        pool = ThreadPoolExecutor(max_workers = 50)
        tasks = []
        for j in range(len(self.m3u8_real_url_list)):
            tasks.append(pool.submit(download_audio_fen, self.m3u8_real_url_list[j], self.path))
        wait(tasks)

    def download_video(self)->list:
        for each_url in self.url:
            response = requests.get(each_url)
            # 获取headers
            headers = response.headers
            session = requests.session()
            # 获取cookie
            session.get(each_url, headers=headers)
            # 携带cookie连接地址
            response = session.get(each_url, headers=headers)
            response.encoding = 'utf-8'
            data = response.text
            # 匹配获取么m3u8地址
            m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')
            # 获取m3u8文件
            response = session.get(m3u8_url, headers=headers)
            response.encoding = 'utf-8'
            data = response.text
            # 获取m3u8文件的真实地址
            self.m3u8_resl_url = data.split('/', 3)[-1].strip()
            self.m3u8_resl_url = urljoin(m3u8_url, self.m3u8_resl_url)
            self.m3u8_real_url_list.append(self.m3u8_real_url)
        # 创建文件保存路径
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        pool = ThreadPoolExecutor(max_workers=50)
        tasks = []
        for j in range(len(self.m3u8_real_url_list)):
            tasks.append(pool.submit(download_vidio_fen, self.m3u8_real_url_list[j], self.path))
        wait(tasks)

    def download_avdio(self)->list:
        for each_url in self.url:
            response = requests.get(each_url)
            # 获取headers
            headers = response.headers
            session = requests.session()
            # 获取cookie
            session.get(each_url, headers=headers)
            # 携带cookie连接地址
            response = session.get(each_url, headers=headers)
            response.encoding = 'utf-8'
            data = response.text
            # 匹配获取么m3u8地址
            m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')
            # 获取m3u8文件
            response = session.get(m3u8_url, headers = headers)
            response.encoding = 'utf-8'
            data = response.text
            # 获取m3u8文件的真实地址
            self.m3u8_resl_url = data.split('/', 3)[-1].strip()
            self.m3u8_resl_url = urljoin(m3u8_url, self.m3u8_resl_url)
            self.m3u8_real_url_list.append(self.m3u8_real_url)
        # 创建文件保存路径
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        # 多线程下载m3u8和ts文件
        pool = ThreadPoolExecutor(max_workers=50)
        tasks = []
        i = 0
        with open('index.m3u8', mode = 'r', encoding = 'utf-8') as f:
            for line in f:
                # 不是链接就走下一趟循环
                if line.startswith('#'):
                    continue
                print(line, i)
                print("开始下载ts文件!")
                tasks.append(pool.submit(download_ts, line.strip(), i, headers))
                i += 1
        print(i)
        # 等待阻塞任务完成
        wait(tasks)
        # 合并png的ts图片
        src_path = self.path
        dst_path = self.path + '2'
        resolve_ts(src_path, dst_path)
        do_m3u8_url(dst_path)

    def get_vidio_straight_chain(self)->list:
        for each_url in self.url:
            response = requests.get(each_url)
            # 获取headers
            headers = response.headers
            session = requests.session()
            # 获取cookie
            session.get(each_url, headers=headers)
            # 携带cookie连接地址
            response = session.get(each_url, headers=headers)
            response.encoding = 'utf-8'
            data = response.text
            # 匹配获取么m3u8地址
            m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')
            # 获取m3u8文件
            response = session.get(m3u8_url, headers=headers)
            response.encoding = 'utf-8'
            data = response.text
            # 获取m3u8文件的真实地址
            self.m3u8_resl_url = data.split('/', 3)[-1].strip()
            self.m3u8_resl_url = urljoin(m3u8_url, self.m3u8_resl_url)
            self.m3u8_real_url_list.append(self.m3u8_real_url)
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp4',
                'preferredquality': 'best',
            }],
            'outtmpl': '%(id)s.%(ext)s',
            'noplaylist': True,
            'audioformat': 'mp4',
            'quiet': True,
            'audioquality': 'best',
        }
        pool = ThreadPoolExecutor(max_workers=50)
        tasks = []
        i = 0
        def get_vidio_url(i, each_m3u8_real_url):
            vidio_info = ydl.extract_info(each_m3u8_real_url, download=False)
            vidio_url = vidio_info['formats'][0]['url']
            with open('vidio_url.md', 'a', encoding='utf-8') as f:
                f.write(vidio_url + '\n')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            for each_m3u8_real_url in self.m3u8_real_url_list:
                print(i)
                tasks.append(pool.submit(get_vidio_url(get_vidio_url, i, each_m3u8_real_url)))
                i += 1
        print(i)
        wait(tasks)

    def get_audio_straight_chain(self)->list:
        for each_url in self.url:
            response = requests.get(each_url)
            # 获取headers
            headers = response.headers
            session = requests.session()
            # 获取cookie
            session.get(each_url, headers=headers)
            # 携带cookie连接地址
            response = session.get(each_url, headers=headers)
            response.encoding = 'utf-8'
            data = response.text
            # 匹配获取么m3u8地址
            m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')
            # 获取m3u8文件
            response = session.get(m3u8_url, headers = headers)
            response.encoding = 'utf-8'
            data = response.text
            # 获取m3u8文件的真实地址
            self.m3u8_resl_url = data.split('/', 3)[-1].strip()
            self.m3u8_resl_url = urljoin(m3u8_url, self.m3u8_resl_url)
            self.m3u8_real_url_list.append(self.m3u8_real_url)
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(id)s.%(ext)s',
            'noplaylist': True,
            'audioformat': 'mp3',
            'quiet': False,
            'audioquality': 192,
        }
        pool = ThreadPoolExecutor(max_workers=50)
        tasks = []
        i = 0
        def get_audio_url(i, each_m3u8_real_url):
            audio_info = ydl.extract_info(each_m3u8_real_url, download=False)
            audio_url = audio_info['formats'][0]['url']
            with open('audio_url.md', 'a', encoding = 'utf-8') as f:
                f.write(audio_url + '\n')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            for each_m3u8_real_url in self.m3u8_real_url_list:
                print(i)
                tasks.append(pool.submit(get_audio_url(get_audio_url, i, each_m3u8_real_url)))
                i += 1
        print(i)
        wait(tasks)

    def get_avdio_straight_chain(self)->list:
        for each_url in self.url:
            response = requests.get(each_url)
            # 获取headers
            headers = response.headers
            session = requests.session()
            # 获取cookie
            session.get(each_url, headers=headers)
            # 携带cookie连接地址
            response = session.get(each_url, headers=headers)
            response.encoding = 'utf-8'
            data = response.text
            # 匹配获取么m3u8地址
            m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')
            # 获取m3u8文件
            response = session.get(m3u8_url, headers = headers)
            response.encoding = 'utf-8'
            data = response.text
            # 获取m3u8文件的真实地址
            self.m3u8_resl_url = data.split('/', 3)[-1].strip()
            self.m3u8_resl_url = urljoin(m3u8_url, self.m3u8_resl_url)
            self.m3u8_real_url_list.append(self.m3u8_real_url)
        with open('avdio_straight_chain.md', 'a', encoding = 'utf-8') as f:
            f.write(self.m3u8_real_url_list + '\n')

def get_users_sort_url(share_users_url_list: list):
    '''
    :param: 获取用户所有作品链接
    :return:
    '''
    _driver_path = get_browser_driver()
    i = 0
    driver = webdriver.Chrome(execute_path=_driver_path)
    for each_user_url in share_users_url_list:
        driver.get(each_user_url)
        time.sleep(3)
        # 滑动页面加载作品
        SCROLL_PAUSE_TIME = 2
        last_height = driver.execute_script('return document.body.scrollHeight')
        while True:
            driver.execute_script('window.scrollTo(0, {});'.format(last_height))
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script('return document.body.scrollHeight')
            if new_height == last_height:
                break
            last_height = new_height
        # 获取作品链接
        videos = driver.find_elements(By.XPATH, '//a[@href and contains(@href, "/video/")]')
        current_directory = os.getpwd()
        file_name = "str(i) + '.md'"
        file_path = os.path.join(current_directory, file_name)
        temp_list.append(str(file_path))
        with open(file_path, 'w') as f:
            f.write(video.get_attribute('href') for video in videos)
            f.write('\n')
        i += 1
    driver.quit()

def get_browser_driver():
    '''
    :param: 获取浏览器驱动路径
    :param browser: 浏览器名称
    :return:
    '''
    try:
        print("正在获取浏览器驱动......")
        # 获取浏览器驱动路径
        _browser_regs = {
            'IE': r"SOFTWARE\Clients\StartMenuInternet\IEXPLORE.EXE\DefaultIcon",
            'chrome': r"SOFTWARE\Clients\StartMenuInternet\Google Chrome\DefaultIcon",
            'edge': r"SOFTWARE\Clients\StartMenuInternet\Microsoft Edge\DefaultIcon",
            'firefox': r"SOFTWARE\Clients\StartMenuInternet\FIREFOX.EXE\DefaultIcon",
            '360': r"SOFTWARE\Clients\StartMenuInternet\360Chrome\DefaultIcon",
        }
        for each_browser in _browser_regs:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, _browser_regs[str(each_browser)])
        value, type = winreg.QueryValueEx(key, "")
        return value.split(",")[0].strip('"')
        print("驱动获取成功！")
    except:
        print("获取浏览器驱动失败！请手动选择！")
        root = tk.TK()
        root.withdraw()
        f_path = filedialog.askopenfilename()
        return f_path

def download_audio_fen(url, path):
    ffmpeg.input(url).output(path, format = 'mp3', acodec = 'libmp3lame').run()

def download_vidio_fen(url, path):
    ffmpeg.input(url).output(path, format = 'mp4', vcodec = 'copy', an = None).run()

def sort_share_url(share_url: str)->list:
    if (share_url == None):
        print("获得分享链接失败，请检查输入是否正确！")
        sys.exit(0)
    else:
        share_url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        result_share_url = share_url_pattern.findall(share_url)
        print("分享链接获取成功！")
        return result_share_url

def resolve_ts(src_path, dst_path):
    '''
    如果m3u8返回的ts文件地址为
    https://p1.eckwai.com/ufile/adsocial/7ead0935-dd4f-4d2f-b17d-dd9902f8cc77.png
    即后缀为png
    则需要下面处理后 才能进行合并
    原因在于 使用Hexeditor打开后，发现文件头被描述为了PNG
    在这种情况下，只需要将其中PNG文件头部分全部使用FF填充，即可处理该问题
    :return:
    '''
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    file_list = sorted(os.listdir(src_path), key = lambda x: int(x.split('.')[0]))
    for i in file_list:
        origin_ts = os.path.join(src_path, i)
        resolved_ts = os.path.join(dst_path, i)
        try:
            infile = open(origin_ts, 'rb')  # 打开文件
            outfile = open(resolved_ts, 'wb')  # 打开输出文件
            data = infile.read()
            outfile.write(data)
            outfile.seek(0x00)
            outfile.write(b'\xff\xff\xff\xff')
            outfile.flush()
            infile.close()
            outfile.close()
        except:
            print("ts文件修正失败！")
            exit(0)
        '''
        else:
            # 删除目录
            shutil.rmtree(src_path)
            # 将副本重命名为正式文件
            os.rename(dst_path, dst_path.rstrip('2'))
        '''
        print('resolve ' + origin_ts + ' success')

def do_m3u8_url(path, m3u8_filename = 'index.m3u8'):
    # 处理m3u8中加密key的问题
    if not os.path.exists(path):
        os.mkdir(path)
    with open(m3u8_filename, mode = 'r', encoding = 'utf-8') as f:
        data = f.readlines()
    fw = open(os.path.join(path, m3u8_filename), 'w', encoding = 'utf-8')
    abs_path = os.getcwd()
    i = 0
    for line in data:
        if line.startswith("#"):
            fw.write(line)
        else:
            fw.write(f'{abs_path}/{path}/{i}.ts\n')
            i += 1

def merge(path, filename = 'output'):
    '''
    进行ts文件合并 解决视频音频不同步的问题 建议使用这种
    :param filePath:
    :return:
    '''
    os.chdir(path)
    cmd = f'ffmpeg -i index.m3u8 -c copy {filename}.mp4'
    os.system(cmd)

def download_ts(url, i, headers):
    resp = requests.get(url, headers = headers)
    with open(os.path.join(path, str(i) + 'ts'), mdoe = 'wb') as f:
        f.write(resp.content)
    print("ts文件下载成功!")

def my_decorator(func):
    def wrapper(*args, **kwargs):
        pass
    return wrapper


if __name__ == '__main__':
    print("欢迎使用抖音视频解/图片解析下载工具！")
    print("A -- 下载无声视频！")
    print("B -- 下载音频！")
    print("C -- 下载有声视频！")
    print("D -- 获取音频直链！")
    print("E -- 获取无声视频直链！")
    print("F -- 获取有声视频直链！")
    print("G -- 下载某用户所有无声视频！")
    print("H -- 下载某用户所有音频！")
    print("I -- 下载某用户所有有声视频！")
    directive = input("请输入指令选项：").strip()

    # 临时存储路径
    temp_list = []

    match directive:
        case 'A':
            share_url = input("请输入视频分享链接(可带文字会自动去除，可输入多个链接)：").strip()
            print("正在获取分享链接...")
            share_url_list = sort_share_url(share_url)
            print("分享链接获取完毕！")
            path = str(input("请输入保存路径：").strip())
            print("开始下载！")
            Douyin_Crawler().download_video()
            print("下载完毕！")

        case 'B':
            share_url = input("请输入视频分享链接(可带文字会自动去除，可输入多个链接)：").strip()
            print("正在获取分享链接...")
            share_url_list = sort_share_url(share_url)
            print("分享链接获取完毕！")
            path = str(input("请输入保存路径：").strip())
            print("开始下载！")
            Douyin_Crawler().download_video()
            print("下载完毕！")

        case 'C':
            share_url = input("请输入视频分享链接(可带文字会自动去除，可输入多个链接)：").strip()
            print("正在获取分享链接...")
            share_url_list = sort_share_url(share_url)
            print("分享链接获取完毕！")
            path = str(input("请输入保存路径：").strip())
            print("开始下载！")
            Douyin_Crawler().download_avdio()
            print("下载完毕！")

        case 'D':
            share_url = input("请输入视频分享链接(可带文字会自动去除，可输入多个链接)：").strip()
            print("正在获取分享链接...")
            share_url_list = sort_share_url(share_url)
            print("分享链接获取完毕！")
            Douyin_Crawler().get_audio_straight_chain()

        case 'E':
            share_url = input("请输入视频分享链接(可带文字会自动去除，可输入多个链接)：").strip()
            print("正在获取分享链接...")
            share_url_list = sort_share_url(share_url)
            print("分享链接获取完毕！")
            Douyin_Crawler().get_vidio_straight_chain()

        case 'F':
            share_url = input("请输入视频分享链接(可带文字会自动去除，可输入多个链接)：").strip()
            print("正在获取分享链接...")
            share_url_list = sort_share_url(share_url)
            print("分享链接获取完毕！")
            path = str(input("请输入保存路径：").strip())
            print("直链：")
            Douyin_Crawler().get_avdio_straight_chain()
            print("获取完毕！")

        case 'G':
            share_users_url = input("请输入用户分享链接或用户抖音号(可带文字会自动去除，可输入多个链接)：").strip()
            print("正在获取用户链接...")
            share_users_url_list = sort_share_url(share_users_url)
            achievement_url_list = get_users_sort_url(share_users_url_list)
            print("分享链接获取完毕！")
            path = str(input("请输入保存路径：").strip())
            print("开始下载！")
            pool1 = ThreadPoolExecutor(max_workers=50)
            tasks1 = []
            i = 0
            Douyin_Crawler().download_video = my_decorator(Douyin_Crawler().download_video())
            for each_path in temp_list:
                url = []
                with open(each_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        url.append(line.strip())
                # 待完善
                tasks1.append(pool1.submit(Douyin_Crawler().download_video(), url, i))
                print(i)
                i += 1
            wait(tasks1)
            for each_path in temp_list:
                os.remove(each_path)
            temp_list.clear()
            print("下载完毕！")

        case 'H':
            share_users_url = input("请输入用户分享链接或用户抖音号(可带文字会自动去除，可输入多个链接)：").strip()
            print("正在获取用户链接...")
            share_users_url_list = sort_share_url(share_users_url)
            achievement_url_list = get_users_sort_url(share_users_url_list)
            print("分享链接获取完毕！")
            path = str(input("请输入保存路径：").strip())
            print("开始下载！")
            pool1 = ThreadPoolExecutor(max_workers=50)
            tasks1 = []
            i = 0
            Douyin_Crawler().download_audio = my_decorator(Douyin_Crawler().download_audio)
            for each_path in temp_list:
                url = []
                with open(each_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        url.append(line.strip())
                # 待完善
                tasks1.append(pool1.submit(Douyin_Crawler().download_audio, url, i))
                print(i)
                i += 1
            wait(tasks1)
            for each_path in temp_list:
                os.remove(each_path)
            temp_list.clear()
            print("下载完毕！")

        case 'I':
            share_users_url = input("请输入用户分享链接或用户抖音号(可带文字会自动去除，可输入多个链接)：").strip()
            print("正在获取用户链接...")
            share_users_url_list = sort_share_url(share_users_url)
            achievement_url_list = get_users_sort_url(share_users_url_list)
            print("分享链接获取完毕！")
            path = str(input("请输入保存路径：").strip())
            print("开始下载！")
            pool1 = ThreadPoolExecutor(max_workers=50)
            tasks1 = []
            i = 0
            Douyin_Crawler().download_avdio = my_decorator(Douyin_Crawler().download_avdio)
            for each_path in temp_list:
                url = []
                with open(each_path, 'r', encoding = 'utf-8') as f:
                    for line in f:
                        url.append(line.strip())
                # 待完善
                tasks1.append(pool1.submit(Douyin_Crawler().download_avdio, url, i))
                print(i)
                i += 1
            wait(tasks1)
            for each_path in temp_list:
                os.remove(each_path)
            temp_list.clear()
            print("下载完毕！")

        case _:
            print("指令选项输入错误或不支持多个选项输入！")
            sys.exit(0)