#!/usr/bin/env python
# coding=utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import weibo_api

setup(
    name='weibo-api',
    keywords=['weibo', 'network', 'http', 'JSON'],
    version=weibo_api.__version__,
    packages=['weibo_api', 'weibo_api.weibo', 'weibo_api.config', 'weibo_api.utils'],
    url='https://github.com/hukaixuan/weibo-api',
    license='MIT',
    author='hukaixuan',
    author_email='hukx.michael@gmail.com',
    description='对微博m站API进行封装，提供简单易用的用户接口来免登陆获取微博数据',
    install_requires=[
        'requests>=2.10.0',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
