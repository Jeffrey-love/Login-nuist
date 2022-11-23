from requests import get, post
from time import sleep
from configparser import ConfigParser
import json


print("""
@Author: Jeffrey
@repo: https://github.com/Jeffrey-love/Login-nuist
@version: 1.0

 _                _         _   _ _   _ ___ ____ _____ 
| |    ___   __ _(_)_ __   | \ | | | | |_ _/ ___|_   _|
| |   / _ \ / _` | | '_ \  |  \| | | | || |\___ \ | |  
| |__| (_) | (_| | | | | | | |\  | |_| || | ___) || |  
|_____\___/ \__, |_|_| |_| |_| \_|\___/|___|____/ |_|  
            |___/                                      

""")


def getConfig(section, key):
    config = ConfigParser()
    path = 'data.conf'
    config.read(path, encoding="ANSI")
    return config.get(section, key)


def get_ip() -> str:
    json = get(url="http://10.255.255.46/api/v1/ip").json()
    ip = json["data"]
    return str(ip)


def login(ip):
    res2 = {"username": phone, "password": password,
            "ifautologin": "0", "channel": type, "pagesign": "secondauth", "usripadd": ip}
    resp2 = post(url="http://10.255.255.46/api/v1/login",
                 data=json.dumps(res2, separators=(",", ":"))).json()
    outport = resp2["data"]["outport"]
    code = resp2["code"]
    if code == 200:
        print("[√]连接成功！")
    else:
        print("[×]连接失败。")
    if not operator == outport:
        sleep(3)
        login(ip)


# def logout(ip):
#     auth = {"username": phone, "password": password, "channel": "0", "ifautologin": "1",
#             "pagesign": "thirdauth", "usripadd": ip}
#     post(url="http://10.255.255.46/api/v1/logout",
#          data=json.dumps(auth, separators=(",", ":")))


if __name__ == '__main__':
    try:
        phone = getConfig("data", "phone")
        password = getConfig("data", "password")
        operator = getConfig("data", "operator")
        if operator == "中国移动":
            type = "2"
        elif operator == "中国电信":
            type = "3"
        else:
            type = "4"
        ip = get_ip()
        login(ip)
        # logout(ip)
    except Exception as e:
        print(e)
