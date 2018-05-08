#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
import getpass
usename = "lin"
passworld = "abcdefg"

_usename = str(input("usename:"))
_passworld = str(getpass.getpass("passworld:"))

if  _usename == usename and _passworld == passworld:
    print("Welcome to user {name} login...".format(name = usename))
else:
    print("invalid username or passworld...")