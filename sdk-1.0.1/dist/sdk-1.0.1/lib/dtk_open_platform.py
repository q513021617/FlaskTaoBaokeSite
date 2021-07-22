import operator
import hashlib
import copy
import subprocess
import logging
import json
logging.captureWarnings(True)
try:
    import requests
except:
    print('尚未安装requests库，正在安装，请稍后！')
    subprocess.call('pip install requests')
    print('requests库安装成功！第一次调用接口！')
    import requests
class DtkOpenPlatform():
    def md5(self,arg):
        md5 = hashlib.md5()
        loc_bytes_utf8 = arg.encode(encoding="utf-8")
        md5.update(loc_bytes_utf8)
        return md5.hexdigest()
    def md5_sign(self,args=None,key=None):
        copy_args =copy.deepcopy(args)
        sorted_args = sorted(copy_args.items(), key=operator.itemgetter(0))
        tmp = []
        for i in sorted_args:
            tmp.append('{}={}'.format(list(i)[0], list(i)[1]))
        sign = self.md5('&'.join(tmp) + '&' + 'key={}'.format(key)).upper()
        copy_args['sign'] = sign
        return copy_args
    def open_platform_send(self,method,url,args,key,UserAgent=None,ContentType=None,type='data'):
        if UserAgent == None:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
                       'Content-Type':ContentType}
        else:
            headers = {"User-Agent": UserAgent,'Content-Type': ContentType}
        data = self.md5_sign(args=args,key=key)
        method_tmp = method.lower()
        if method_tmp == 'get':
            response = requests.request(method=method_tmp,url=url,params=data,headers=headers,verify=False).json()
            return response
        elif method_tmp == 'post':
            if type == 'data':
                response = requests.request(method=method_tmp,url=url,data=data,headers=headers,verify=False).json()
                return response
            elif type == 'json':
                response = requests.request(method=method_tmp, url=url, data=json.dumps(data), headers=headers, verify=False).json()
                return response
