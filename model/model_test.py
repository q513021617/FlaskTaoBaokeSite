# -*- coding:utf-8 -*-
import traceback

from model.user import addIntegration,appendproxyId,queryAll,User
from model.proxy import queryVIPsbyId, queryAll,Proxy
from model.excle2sql import excle2sql
print("执行")
num = 1

print(queryAll(User).username)
