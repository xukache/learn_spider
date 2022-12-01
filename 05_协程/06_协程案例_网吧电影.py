# 整体步骤
"""
1. 想办法找到M3U8文件
2. 判别是否需要下载第二层M3U8
3. 提取ts文件的下载路径
4. 下载
5. 判别是否需要解密
6. 如果需要解密，拿到密钥
7. 解密
8. 根据M3U8的正确顺序来合并所有的ts文件 => MP4
"""
import asyncio

import requests
from lxml import etree
import re
from urllib.parse import urljoin
import os

import asyncio
import aiohttp
import aiofiles

from Crypto.Cipher import AES  # pip install pycryptodome

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

def get_iframe_src(url):

    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)
    src = tree.xpath("//iframe/@src")[0]
    return src


def get_m3u8_url(url):
    resp = requests.get(url, headers=headers)
    obj = re.compile(r'url: "(?P<m3u8>.*?)"', re.S)
    m3u8 = obj.search(resp.text).group("m3u8")
    return m3u8


def download_m3u8(url):
    resp = requests.get(url, headers=headers)
    with open("first.txt", mode="w", encoding="utf-8") as f1:
        f1.write(resp.text)
    with open("first.txt", mode="r", encoding="utf-8") as f2:
        for line in f2:
            if line.startswith("#"):
                continue
            # 此时的line就是第二层的m3u8地址
            line = line.strip()  # 注意要strip()

            line = urljoin(url, line)  # 拼接一下
            # 下载第二层M3U8
            resp1 = requests.get(line, headers=headers)
            with open("second.txt", mode="w", encoding="utf-8") as f3:
                f3.write(resp1.text)


async def download_one(url, sem):
    async with sem:  # 使用信号量控制访问频率
        file_name = url.split("/")[-1]
        file_path = "./解密前/" + file_name
        print(file_name, '开始工作了!')
        for i in range(10):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as resp:
                        content = await resp.content.read()
                        # 写入文件
                        async with aiofiles.open(file_path, mode="wb") as f:
                            await f.write(content)
                print(file_name, '下载完成!')
                break
            except Exception as e:
                print(file_name, '出错了，马上重试', e)  # 给个提示，看到错误信息

async def download_all_videos(url):
    # 信号量，用来控制协程的并发量
    sem = asyncio.Semaphore(100)
    # 提取所用的url
    url2 = re.search(".*?.com", url).group()
    # 1. 读取文件
    tasks = []
    with open("second.txt", mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            line = url2 + line
            # 此时line就是下载地址
            # 2. 创建任务
            t = asyncio.create_task(download_one(line, sem))
            tasks.append(t)
    # 3. 统一等待
    await asyncio.wait(tasks)


def get_key(url):
    with open("second.txt", mode="r", encoding="utf-8") as f:
        file_content = f.read()  # 读取所有内容
        obj = re.compile(r'URI="(?P<key_url>.*?)"')
        key_url = obj.search(file_content).group("key_url")
        # 提取所用的url
        url2 = re.search(".*?.com", url).group()
        key_url = url2 + key_url
        resp = requests.get(key_url, headers=headers)  # 发请求，拿密钥
        return resp.content  # 直接拿字节，为了解密的时候，直接丢进去就可以了


async def desc_one(file_path, key):
    file_name = file_path.split("/")[-1]
    new_file_path = "./解密后/" + file_name
    # 解密
    async with aiofiles.open(file_path, mode="rb") as f1, \
            aiofiles.open(new_file_path, mode="wb") as f2:
                content = await f1.read()
                # 解密
                # 固定逻辑，创建一个加密器
                aes = AES.new(key=key, mode=AES.MODE_CBC, IV=b"0000000000000000")
                new_content = aes.decrypt(content)
                await f2.write(new_content)  # 写入新文件
    print(new_file_path, "解密成功")


# 解密的协程逻辑
# 读m3u8文件，拿到文件名称和路径
# 每个ts文件一个任务
# 在每个任务中，解密即可
async def desc_all(key):
    tasks = []
    with open("second.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            file_name = line.split("/")[-1]
            file_path = "./解密前/"+file_name
            # 创建任务，去解密
            t = asyncio.create_task(desc_one(file_path, key))
            tasks.append(t)
    await asyncio.wait(tasks)


def merge():
    # 视频片段合成
    # 需要一个命令
    # windows: copy /b a.ts+b.ts+c.ts "xxx.mp4"
    pass
    # 需要分段合并
    # 采用popen执行命令，可以避免乱码
    # 只需关注，是否合并成功
    # os.system("dir")  # 会有乱码
    # r = os.popen("dir")
    # print(r.read())  # 暂时避免乱码

    # 分段合并
    # 合并，顺序
    file_list = []
    with open("second.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            file_name = line.split("/")[-1]
            file_list.append(file_name)

    # 进入到文件夹内
    os.chdir("./解密后")  # 更换工作目录
    # file_list 所有文件名称
    n = 1
    temp = []
    for i in range(len(file_list)):
        # 每20个合并一次
        file_name = file_list[i]
        temp.append(file_name)
        if i != 0 and i % 20 == 0:
            # 可以合并一次
            cmd = f"copy /b {'+'.join(temp)} {n}.ts"
            r = os.popen(cmd)
            print(r.read())
            temp = []  # 新列表
            n += 1
    # 把剩余的ts进行合并
    cmd = f"copy /b {'+'.join(temp)} {n}.ts"
    r = os.popen(cmd)
    print(r.read())

    # 第二次大合并
    last_temp = []
    for i in range(1, n+1):
        last_temp.append(f"{i}.ts")
    # 最后一次合并
    cmd = f"copy /b {'+'.join(last_temp)} 一部电影.mp4"
    r = os.popen(cmd)
    print(r.read())

    # 回来
    os.chdir("../")  # ../表示上层文件夹



def main():
    url = "https://www.wbdyba.com/play/102462_1_1.html"
    # 1. 拿到iframe的src属性值
    # src = get_iframe_src(url)
    # print(src)
    # 2. 发送请求到iframe的src路径，获取到M3U8地址
    # src = urljoin(url, src)  # 拼接一下
    # m3u8_url = get_m3u8_url(src)
    # print(m3u8_url)
    # # 3. 下载m3u8文件
    # download_m3u8(m3u8_url)
    # # 4. 下载视频, 上协程
    # # asyncio.run(download_all_videos())
    # event_loop = asyncio.get_event_loop()
    # event_loop.run_until_complete(download_all_videos(m3u8_url))
    # 5. 拿密钥
    # key = get_key(m3u8_url)
    # 6. 解密
    # event_loop = asyncio.get_event_loop()
    # event_loop.run_until_complete(desc_all(key))
    # print("全部完成")
    # 7. 合成
    merge()

if __name__ == '__main__':
    main()
