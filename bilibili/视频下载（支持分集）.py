import asyncio
from bilibili_api import video, Credential, exceptions
import aiohttp
import os
from icecream import ic

# SESSDATA = "523546a7%2C1655213102%2Ce382a%2Ac1"
# BILI_JCT = "d5f924a59b19a007ce7b6a460f06f068"
# BUVID3 = "E6038BB3-E448-40FF-BF01-3181726679C6167632infoc"
SESSDATA = BILI_JCT = BUVID3 = ""

FFMPEG_PATH = "D:/ffmpeg/bin/ffmpeg.exe"
PATH = "E:/Desktop/cpp/"
BV = "BV1K54y147Rd"
NAME = ""

cnt = 1


async def main(p=0):
    credential = Credential(sessdata=SESSDATA,
                            bili_jct=BILI_JCT,
                            buvid3=BUVID3)
    v = video.Video(bvid=BV, credential=credential)
    
    info = await v.get_info()
    url = await v.get_download_url(p)  # 编号从0开始计数
    video_url = url["dash"]["video"][0]['baseUrl']
    audio_url = url["dash"]["audio"][0]['baseUrl']
    video_name = info["pages"][p]["part"].replace(" ", "_")
    HEADERS = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.bilibili.com/"
    }
    async with aiohttp.ClientSession() as sess:
        async with sess.get(video_url, headers=HEADERS) as resp:
            length = resp.headers.get('content-length')
            with open(f'video_temp_{p}.m4s', 'wb') as f:
                process = 0
                while True:
                    chunk = await resp.content.read(1024)
                    if not chunk:
                        break
                    process += len(chunk)
                    # print(f'下载视频流 {process} / {length}')
                    f.write(chunk)

        async with sess.get(audio_url, headers=HEADERS) as resp:
            length = resp.headers.get('content-length')
            with open(f'audio_temp_{p}.m4s', 'wb') as f:
                process = 0
                while True:
                    chunk = await resp.content.read(1024)
                    if not chunk:
                        break

                    process += len(chunk)
                    # print(f'下载音频流 {process} / {length}')
                    f.write(chunk)

        # 混流
        # print('混流中')
        os.system(
            f'{FFMPEG_PATH} -i video_temp_{p}.m4s -i audio_temp_{p}.m4s -vcodec copy -acodec copy {PATH}/{video_name}.mp4'
        )

        # 删除临时文件
        os.remove(f"video_temp_{p}.m4s")
        os.remove(f"audio_temp_{p}.m4s")

        print(f'已下载为：{video_name}.mp4')


if __name__ == '__main__':
    i = 0
    while (True):
        try:
            asyncio.get_event_loop().run_until_complete(main(p=i))
            i += 1
        except:
            break
    print(f"总计视频数量为{i}")
