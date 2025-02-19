# coding:utf-8
# package util
import numpy as np 
import pandas as pd
import os
import logging
import logging.handlers
import datetime
import time

def get_train_data(train_data_path, _base=1, col=256):
    # 获取数据转换为矩阵
    train_data, labels = [], []
    with open(train_data_path) as f:
        for x, line in enumerate(f.readlines()):
            try:
                line_data = line[:-1].strip().split("\t")
                # print("[DEBUG] len(line_data) : {}".format(len(line_data)))
                _data = []
                for d in line_data[_base:-1]:
                    if len(d.split('\n')) > 1:
                        print("[ERROR] 这里居然有换行符! line number: {}".format(x))
                        break
                    _data.append(float(d))
                if len(_data) != col:
                    print("[ERROR] 不够长, 当前长度为: {} line number: {}".format(len(_data), x ))
                    continue
                train_data.append(_data)
                labels.append(int(line_data[-1]))
                # print("[DEBUG] line number: {}, _data.size(): {}, labels: {}".format(line_data[0], len(_data), line_data[-1]))
            except:
                print("[ERROR] 未知错误, line_data: {}".format(line_data))
                continue
    return np.array(train_data), np.array(labels).T


def pre_process(data, alpha=0.99, is_total=False):
    """离差标准化(0, 1)"""
    m, n = np.shape(data)
    ret = np.zeros((m, n))
    for i in range(m):
        total = np.sum(data[i, :])
        max_value = np.max(data[i, :])
        for j in range(n):
            if is_total:
                ret[i, j] = data[i, j] / total * alpha
            else:
                ret[i, j] = [data[i, j], 1][data[i, j] == 0] / max_value * alpha
    return ret


def mkdirs(file_list):
    """
    创建文件目录
    """
    if isinstance(file_list, list):
        for f in file_list:
            if not os.path.isdir(f):
                os.makedirs(f)
    else:
        if not os.path.isdir(file_list):
            os.makedirs(file_list)
    return 


def get_logger(logger_path):
    """设置日志"""
    # LOG_FORMAT = "%(asctime)s - %(levelname)s - %(user)s[%(ip)s] - %(message)s"
    # DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

    # logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT)
    if logger_path:
        mkdirs(logger_path)
        
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    all_log = os.path.join(logger_path, "all.log")
    error_log = os.path.join(logger_path, "error.log")


    rf_handler = logging.handlers.TimedRotatingFileHandler(all_log, when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line: %(lineno)d] - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler(error_log)
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line: %(lineno)d] - %(levelname)s - %(message)s"))

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter("%(asctime)s - [%(levelname)s] %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    logger.addHandler(console)

    return logger