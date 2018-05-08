#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = "Hero_lws"

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 没有上面一句会有以下报错：
# paramiko.ssh_exception.SSHException: Server '192.168.221.130' not found in known_hosts
# known_hosts：建立安全的签名认证

# 连接服务器
ssh.connect(hostname='192.168.221.130', port=22, username='root', password='admin@123')

# 执行命令，返回三个结果
# stdin：标准输入
# 以下两个只有一个会有结果：
	# stdout：标准输出
	# stderr：标准错误
stdin, stdout, stderr = ssh.exec_command('df')

# 获取命令结果
result = stdout.read()
print( result.decode() )
# 关闭连接
ssh.close()