appKey = '60f68a3247adc'

appSecret = 'ae0ca8209c43ef0d062655f4ec4ae449'

from dtk_open_platform import DtkOpenPlatform

send = DtkOpenPlatform()


def reqData(method,url,data):
    data["appKey"]=appKey
    response = send.open_platform_send(method=method, url=url, args=data, key=appSecret)
    # print(response)
    return response


def postData(url,data):

    return reqData("post",url,data)


def getData(url,data):

    return reqData("get", url, data)