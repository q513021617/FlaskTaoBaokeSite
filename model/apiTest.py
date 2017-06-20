# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import top

req = top.TbkItemRecommendGetRequest(url, port)
req.set_app_info(top.appinfo(appkey, secret))

req.fields = "num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url"
req.num_iid = 123
req.count = 20
req.platform = 1

resp = req.getResponse()
print(resp)
