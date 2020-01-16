import time
import random
import requests
import hashlib

class YouDao(object):

    def __init__(self):
        self.base_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Content-Length': '239',
                    'Content-Typ': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Cookie': 'P_INFO=m13433159407; OUTFOX_SEARCH_USER_ID=-1127798087@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=1201378716.9433534; JSESSIONID=aaaGzVUC5lD517-7J9d3w; ___rl__test__cookies=1570950820373',
                    'Host': 'fanyi.youdao.com',
                    'Origin': 'http://fanyi.youdao.com',
                    'Pragma': 'no-cache',
                    'Referer': 'http://fanyi.youdao.com/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest',
        }
        self.ua = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'

    def get_md5(self,key,salt):
        bv = hashlib.md5(self.ua.encode()).hexdigest()

        string = 'fanyideskweb' + key + salt + 'n%A-rKaT5fb[Gy?;N5@Tj'

        sign = hashlib.md5(string.encode()).hexdigest()
        return bv,sign

    def get_data(self,key):
        ts = str(int(time.time() * 1000))

        salt = ts + str(int(random.random() * 10))

        action = random.choice(['FY_BY_CLICKBUTTION', 'FY_BY_REALTlME'])

        md5 = self.get_md5(key,salt)

        data = {
                'i': key,
                'from': 'AUTO',
                'to': 'AUTO',
                'smartresult': 'dict',
                'client': 'fanyideskweb',
                'salt': salt,
                'sign': md5[1],
                'ts': ts,
                'bv': md5[0],
                'doctype': 'json',
                'version': '2.1',
                'keyfrom': 'fanyi.web',
                'action': action,
        }

        res = requests.post(url=self.base_url, data=data, headers=self.headers).json()

        result = ''.join(res['smartResult']['entries'])

        print('单词{}的意思是：{}'.format(key,result))

if __name__ == '__main__':
    youdao = YouDao()
    key = input('请输入要翻译的单词：')
    # youdao.get_data(key)



















