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
    API_DIR = os.path.join(BASE_DIR, "api")
    API_TEM_DIR = os.path.join(API_DIR, "templates")
    API_TEM_RSS_DIR = os.path.join(API_TEM_DIR, "rss")

    # 版本设置
    SCHEDULE_VERSION = "0.1.2"

    # Flask API配置
    DEBUG = bool(os.getenv("LL_FLASK_DEBUG", "0") == "1")
    TIMEZONE = "Asia/Shanghai"
    HOST = os.getenv("LL_HOST", "127.0.0.1")
    HTTP_PORT = int(os.getenv("LL_HTTP_PORT", "8060"))
    WORKERS = int(os.getenv("LL_WORKERS", "1"))
    AUTH_KEY = os.getenv("LL_AUTH_KEY", "123456")

    # 数据库配置
    MONGODB_CONFIG = {
        # "mongodb://0.0.0.0:27017"
        "username": os.getenv("LL_M_USER", ""),
        "password": os.getenv("LL_M_PASS", ""),
        "host": os.getenv("LL_M_HOST", "0.0.0.0"),
        "port": int(os.getenv("LL_M_PORT", "27017")),
        "db": os.getenv("LL_M_DB", "liuli"),
    }

    # 采集器配置
    # 是否为爬虫设置代理
    PROXY = os.getenv("LL_PROXY", "http://0.0.0.0:1087")

    # 分类器配置
    # 余弦相似度阈值
    COS_VALUE = float(os.getenv("LL_COS_VALUE", "0.60"))

    # 分发器配置
    # 分发终端配置，设置环境变量：LL_SENDER_NAME="ding;wecom;tg"
    # 目标支持：ding[钉钉]、wecom[企业微信]、tg[Telegram]
    # 多终端记得使用;分割
    SENDER_LIST = str(os.getenv("LL_SENDER_NAME", "")).split(";")
    # 钉钉分发器参数配置，如果 SENDER_LIST 包含 ding ，LL_D_TOKEN 配置就必须填写
    # 申请钉钉TOKEN时候，关键字必须带有 [liuli]
    DD_TOKEN = os.getenv("LL_D_TOKEN", "")
    # 企业微信配置
    WECOM_ID = os.getenv("LL_WECOM_ID", "")
    WECOM_AGENT_ID = int(os.getenv("LL_WECOM_AGENT_ID", "-1"))
    WECOM_SECRET = os.getenv("LL_WECOM_SECRET", "")
    # 企业微信分发部门，多个部门用;分割
    WECOM_PARTY_LIST = os.getenv("LL_WECOM_PARTY", "").split(";")
    # 企业微信分发用户，多个用户用;分割
    WECOM_TO_USER = os.getenv("LL_WECOM_TO_USER", "").replace(";", "|")
    # 订阅的公众号配置
    WECHAT_LIST = os.getenv(
        "LL_WECHAT_ACCOUNT",
        "小众消息;是不是很酷;caoz的梦呓;阿里技术;Thoughtworks洞见;老胡的储物柜",
    ).split(";")
    # TG分发器参数配置
    TG_CHAT_ID = os.getenv("LL_TG_CHAT_ID", "")
    TG_TOKEN = os.getenv("LL_TG_TOKEN", "")
    # Bark 分发器参数配置
    BARK_URL = os.getenv("LL_BARK_URL", "")