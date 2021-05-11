#!/usr/bin/env python
"""
    Created by howie.hu at 2021/4/7.
    Description：配置文件
    Changelog: all notable changes to this file will be documented
"""

import os


class Config:
    """
    配置类
    """

    # 基础配置
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    MODEL_DIR = os.path.join(BASE_DIR, "model_data")
    FILE_DIR = os.path.join(os.path.dirname(BASE_DIR), ".files")
    DS_DIR = os.path.join(FILE_DIR, "datasets")

    # Flask API配置
    DEBUG = bool(os.getenv("CC_FLASK_DEBUG", "0") == "1")
    TIMEZONE = "Asia/Shanghai"
    HOST = os.getenv("CC_HOST", "127.0.0.1")
    HTTP_PORT = int(os.getenv("CC_HTTP_PORT", "8060"))
    WORKERS = int(os.getenv("CC_WORKERS", "1"))
    AUTH_KEY = os.getenv("CC_AUTH_KEY", "123456")

    # 数据库配置
    MONGODB_CONFIG = {
        # "mongodb://0.0.0.0:27017"
        "username": os.getenv("CC_M_USER", ""),
        "password": os.getenv("CC_M_PASS", ""),
        "host": os.getenv("CC_M_HOST", "0.0.0.0"),
        "port": int(os.getenv("CC_M_PORT", "27017")),
        "db": os.getenv("CC_M_DB", "2c"),
    }

    # 采集器配置
    # 是否为爬虫设置代理
    PROXY = os.getenv("CC_PROXY", "http://0.0.0.0:1087")

    # 分类器配置
    # 余弦相似度阈值
    COS_VALUE = float(os.getenv("CC_COS_VALUE", "0.60"))

    # 分发器配置
    # 分发终端配置，设置环境变量：CC_SENDER_NAME="ding;wecom"
    # 目标支持：ding[钉钉]、wecom[企业微信]
    # 多终端记得使用;分割
    SENDER_LIST = str(os.getenv("CC_SENDER_NAME", "")).split(";")
    # 钉钉分发器参数配置，如果 SENDER_LIST 包含 ding ，CC_D_TOKEN 配置就必须填写
    # 申请钉钉TOKEN时候，关键字必须带有 [2c]
    DD_TOKEN = os.getenv("CC_D_TOKEN", "")
    # 企业微信配置
    WECOM_ID = os.getenv("CC_WECOM_ID", "")
    WECOM_AGENT_ID = int(os.getenv("CC_WECOM_AGENT_ID", "-1"))
    WECOM_SECRET = os.getenv("CC_WECOM_SECRET", "")
    # 订阅的公众号配置
    WECHAT_LIST = [
        "小道消息",
        "是不是很酷",
        "机器之心",
        "caoz的梦呓",
        "Sunbelife",
        "TGO鲲鹏会",
        "低并发编程",
        "美团技术团队",
        "阿里技术",
        "ThoughtWorks洞见",
        "老胡的储物柜",
        "stormzhang",
        "InfoQ",
        "从码农到工匠",
        "真没什么逻辑",
    ]


if __name__ == "__main__":
    print(Config.DS_DIR)
