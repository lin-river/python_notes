#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author = Hero lws
import hashlib
#用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
#SHA，MD5都是基于哈希的加密算法，原则上SHA比MD5更安全，因为SHA512算法更复杂
print("---------------------------MD5----------------------------")
secret = hashlib.md5()		#生成一个MD5的hashlib对象
#向对象里加入内容,b为byte类型
secret.update(b"Hello!")
print( secret.hexdigest() )		#以十六进制的格式去加密的
secret.update(b"I love you")
print( secret.hexdigest() )		#这里的md5代表的是"hello"+"I love you"

#MD5值是不能反解的,如何证明md5代表的是"hello"+"I love you"？
secret2 = hashlib.md5()
secret2.update(b"Hello!I love you")
print( secret2.hexdigest() )	#与上面的md5一模一样

print("中文的加密处理：")
secret2.update("你好世界".encode(encoding = "utf-8"))
print( secret2.hexdigest() )


print("----------------SHA1(快被淘汰了，通用256，用最大的512)----------------")
secret3 = hashlib.sha1()	#生成一个SHA1的hashlib对象
secret3.update(b"Hello!I love you")
print( secret3.hexdigest() )

secret3 = hashlib.sha256()
secret3.update(b"Hello!I love you")
print( secret3.hexdigest() )

secret3 = hashlib.sha512()
secret3.update(b"Hello!I love you")
print( secret3.hexdigest() )

print("中文的加密处理：")
secret3.update("你好世界".encode(encoding = "utf-8"))
print( secret3.hexdigest() )

print("---------------------------hmac----------------------------")
import hmac		#高级加密，速度快
# python 有一个 hmac 模块，它内部对我们创建 key 和 内容 再进行处理然后再加密
# 散列消息鉴别码，简称HMAC，是一种基于消息鉴别码MAC（Message Authentication Code）的鉴别机制。
# 使用HMAC时,消息通讯的双方，通过验证消息中加入的鉴别密钥K来鉴别消息的真伪；
# 一般用于网络通信中消息加密，前提是双方先要约定好key,就像接头暗号一样，然后消息发送把用key把消息加密，
# 接收方用key ＋ 消息明文再加密，拿加密后的值 跟 发送者的相对比是否相等，这样就能验证消息的真实性，及发送者的合法性了。
secret4 = hmac.new(b"12345",b"I love you")		#key和内容只能是byte类型，而且只能是ASCII字符（中文不行）
print( secret4.hexdigest())
print( secret4.digest())

print("中文的加密处理：")
secret4 = hmac.new("天王盖地虎".encode(encoding = "utf-8"),"宝塔镇河妖".encode(encoding = "utf-8"))
print( secret4.hexdigest() )