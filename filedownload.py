import os
import requests
import pandas as pd
import logging
import urllib3
from urllib.parse import quote

# 配置日志记录器
from logging.handlers import TimedRotatingFileHandler
import datetime

# 创建带日期的日志文件名
log_filename = f'download_log_{datetime.datetime.now().strftime("%Y%m%d")}.log'

# 创建日志处理器，每天轮换日志文件
handler = TimedRotatingFileHandler(
    log_filename,
    when='midnight',  # 每天午夜轮换
    interval=1,  # 每天一个文件
    backupCount=7,  # 保留最近7天的日志
    encoding='utf-8'
)

# 配置日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# 创建并配置logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# 读取CSV文件数据，这里假设已经能正确读取，编码等问题已解决
#data = pd.read_csv(r'C:\Users\77820\Desktop\filedownload.csv', encoding='utf-8')
data = pd.read_csv(r'/usr/python/filedownload/file_2020.csv', encoding='filedownload.py