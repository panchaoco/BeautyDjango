# -*- coding: utf-8 -*-
__author__ = 'panchao'

import socket

print('当前主机名称为 : ' + socket.gethostname())

# 根据主机名称获取当前IP
print('当前主机的IP为: ' + socket.gethostbyname(socket.gethostname()))