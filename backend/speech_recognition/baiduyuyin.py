import wave
from pyaudio import PyAudio, paInt16
import json
import base64
import os
import requests
import time


RATE = "16000"
FORMAT = "wav"  # 语音文件的格式，
CUID = "wate_play"
DEV_PID = "1536"    # 不填写lan参数生效，都不填写，默认1537（普通话 输入法模型）

framerate = 16000   # 采样率，16000，固定值
NUM_SAMPLES = 2000
channels = 1    # 声道数，仅支持单声道，请填写固定值 1
sampwidth = 2
TIME = 3    # 录制秒数


def get_token():
    server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    # API Key
    client_id = "2ZGdgMqB8l90nDMfWqxtlOxg"
    # Secret Key
    client_secret = "ZGYEE7k5WwEwozu4bBGSULEKqvR8CyXT"

    # 拼url
    url = "%sgrant_type=%s&client_id=%s&client_secret=%s" % (server, grant_type, client_id, client_secret)
    # 获取token
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    return token


def get_word(path, token):
    with open(path + '\\01.wav', "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf8')
    size = os.path.getsize(path + '\\01.wav')
    headers = {'Content-Type': 'application/json'}
    url = "https://vop.baidu.com/server_api"
    data = {
        "format": FORMAT,
        "rate": RATE,
        "dev_pid": DEV_PID,
        "speech": speech,
        "cuid": CUID,
        "len": size,
        "channel": 1,
        "token": token,
    }

    req = requests.post(url, json.dumps(data), headers)
    result = json.loads(req.text)
    # print(result)
    ret = result["result"][0]
    return result


def save_wave_file(filename, data):
    '''save the date to the wavfile'''
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()


def my_record(path):
    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=1,
                     rate=framerate, input=True,
                     frames_per_buffer=NUM_SAMPLES)
    my_buf = []
    count = 0
    while count < TIME * 10:  # 控制录音时间
        # print("正在录音:", '还剩', TIME * 10 - count, '秒')
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)

        count += 1

    save_wave_file(path + '\\01.wav', my_buf)
    stream.close()


chunk = 2014


# def play():
#     wf = wave.open(r"01.wav", 'rb')
#     p = PyAudio()
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=
#     wf.getnchannels(), rate=wf.getframerate(), output=True)
#     while True:
#         data = wf.readframes(chunk)
#         if data == "": break
#         stream.write(data)
#     stream.close()
#     p.terminate()


def main():
    time.sleep(2)
    print('正在倾听：')
    # 音频文件保存路径
    path = os.path.split(os.path.realpath(__file__))[0] + '\\' + 'wav'
    my_record(path)

    # print("识别中...")
    token = get_token()
    try:
        ret = get_word(path, token)
        result = ret['result'][0]
    except:
        result = '系统错误，请稍后再试！'
    return result





# if __name__ == '__main__':
#
#     path = os.path.split(os.path.realpath(__file__))[0] + '\\' + 'wav'
#     # print(path)
#
#     while True:
#         time.sleep(5)
#         print("开始录音：")
#         my_record(path)
#
#         print("识别中...")
#         token = get_token()
#         try:
#             ret = get_word(path, token)
#             print(ret['result'][0])
#         except:
#             print('系统错误，请稍后再试！')
