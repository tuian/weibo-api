# Weibo-api

一个免登陆获取新浪微博数据的Python库，简单易用

## Getting Started

```python
from weibo_api.client import WeiboClient
client = WeiboClient()

p = client.people('5623741644')
print(type(p.name))
print(u"用户名：{}".format(p.name))
print(u"用户简介：{}".format(p.description))
print(u"他关注的用户数：{}".format(p.follow_count))
print(u"关注他的用户数：{}".format(p.followers_count))
print(u"他最近发布的微博：")
print("==================================================")
for status in p.statuses.page(1):
    print(u"微博动态：{}".format(status.id))
    print(u"发布时间：{}".format(status.created_at))
    print(u"微博内容概要：{}".format(status.text))
    print(u"转发数：{}".format(status.reposts_count))
    print(u"点赞数：{}".format(status.attitudes_count))
    print(u"评论数：{}".format(status.comments_count))
    print(u"发布于：{}".format(status.source))
    print("==================================================")
```

### Installing

```
pip install weibo-api
```

### TODO

- 搜索接口
- 根据用户昵称创建用户
- 头条文章获取
- 文章评论
- 文档
- 测试


