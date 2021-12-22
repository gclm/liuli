"""
    Created by howie.hu at 2021-12-22.
    Description: 基于 Ruia 的微信页面 Item 提取类
    Changelog: all notable changes to this file will be documented
"""
from ruia import AttrField, Item, RegexField, Spider, TextField


class WechatItem(Item):
    """
    基于 Ruia 的微信页面 Item 提取类
    示例：https://mp.weixin.qq.com/s/NKnTiLixjB9h8fSd7Gq8lw
    """

    # 文章标题
    # doc_name = AttrField(css_select='meta[property="og:title"]', attr="content")
    doc_name = AttrField(css_select='meta[property="og:title"]', attr="content")
    # 描述
    doc_des = AttrField(
        css_select='meta[property="og:description"]', attr="content", default=""
    )
    # 文章作者
    doc_author = AttrField(
        css_select='meta[property="og:article:author"]', attr="content", default=""
    )
    # 文章链接，这里的链接有过期时间，但是在微信体系内打开并不会过期，所以可以用
    doc_link = AttrField(
        css_select='meta[property="og:url"]', attr="content", default=""
    )
    # 文章类型
    doc_type = AttrField(
        css_select='meta[property="og:type"]', attr="content", default=""
    )
    # 文章图
    doc_image = AttrField(
        css_select='meta[property="og:image"]', attr="content", default=""
    )
    # 公众号名称
    doc_source_name = TextField(
        css_select="div.profile_inner>strong.profile_nickname", default=""
    )
    # 公众号元数据
    doc_source_meta_list = TextField(
        css_select="p.profile_meta>span.profile_meta_value", many=True, default=["", ""]
    )
    # 公众号昵称
    doc_source_account_nick = ""
    # 公众号介绍
    doc_source_account_intro = ""
    # 文本内容，兼容
    doc_content = ""
    # 文章关键字
    doc_keywords = []
    # 常量
    # 信息来源
    doc_source = "2c_wechat"

    async def clean_doc_source_meta_list(self, value: list):
        """从doc_source_meta_list提取公众号昵称和介绍"""
        self.doc_source_account_nick = value[0]
        self.doc_source_account_intro = value[1]
        return value


class WechatSpider(Spider):
    name = "WechatSpider"
    start_urls = ["https://mp.weixin.qq.com/s/NKnTiLixjB9h8fSd7Gq8lw"]
    request_config = {"RETRIES": 3, "DELAY": 0, "TIMEOUT": 20}
    concurrency = 10
    # aiohttp config
    aiohttp_kwargs = {}

    async def parse(self, response):
        html = await response.text()
        item = await WechatItem.get_item(html=html)
        yield item


if __name__ == "__main__":
    WechatSpider.start()
