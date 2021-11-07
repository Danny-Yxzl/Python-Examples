import http.client
import hashlib
import urllib
import random
import json

appid = '20200724000525479'  # 填写你的appid
secretKey = '1HJ76T3fVhmfyybrbPjy'  # 填写你的密钥


def translate(fromLang='auto', toLang="zh", q="apple"):
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = '/api/trans/vip/translate' + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    result = "error"
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        # print(result)
        # print(result['trans_result'][0]['dst'])
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
        return result


translate()