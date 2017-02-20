import urllib.request
import socket
import re
import sys
from pprint import pprint
import os
targetDir = r"D:\PythonWorkPlace\load"  #文件保存路径
def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir, path[pos+1:])
    return t
if __name__ == "__main__":  #程序运行入口
    weburl = "http://www.douban.com/"
    webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    req = urllib.request.Request(url=weburl, headers=webheaders)  #构造请求报头
    webpage = urllib.request.urlopen(req)  #发送请求报头
    contentBytes = webpage.read().decode()
    print(contentBytes)
    for link, t in re.findall(r'src="(https?:\/\/.+\.(jpg|gif|png))', str(contentBytes)):  #正则表达式查找所有的图片
         print(link)
         try:
            urllib.request.urlretrieve(link, destFile(link)) #下载图片
         except:
            print('失败')

