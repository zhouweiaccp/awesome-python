#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates.pop()
print('classmates =', classmates)
va=[{'domain': 'ke.qq.com', 'expiry': 1579311979, 'httpOnly': False, 'name': 'iswebp', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.ke.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_0c196c536f609d373a16d246a117fd44', 'path': '/', 'secure': False, 'value': '1576719979'}, {'domain': '.ke.qq.com', 'expiry': 1608255978, 'httpOnly': False, 'name': 'Hm_lvt_0c196c536f609d373a16d246a117fd44', 'path': '/', 'secure': False, 'value': '1576719979'}, {'domain': '.ke.qq.com', 'httpOnly': False, 'name': 'tdw_first_visited', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s5272657190'}, {'domain': '.ke.qq.com', 'expiry': 1576727178, 'httpOnly': False, 'name': '_pathcode', 'path': '/', 'secure': False, 'value': '0.6339875495023273'}, {'domain': '.ke.qq.com', 'httpOnly': False, 'name': 'tdw_data_sessionid', 'path': '/', 'secure': False, 'value': '157671997860051833646841'}, {'domain': '.ke.qq.com', 'httpOnly': False, 'name': 'tdw_data_testid', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.ke.qq.com', 'httpOnly': False, 'name': 'tdw_auin_data', 'path': '/', 'secure': False, 'value': '-'}, {'domain': '.ke.qq.com', 'httpOnly': False, 'name': 'tdw_data', 'path': '/', 'secure': False, 'value': '{"ver4":"4","ver6":"","refer":"","from_channel":"","path":"b-0.6339875495023273","auin":"-","uin":null,"real_uin":null}'}, {'domain': '.ke.qq.com', 'httpOnly': False, 'name': 'tdw_data_flowid', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.ke.qq.com', 'httpOnly': False, 'name': 'tdw_data_new_2', 'path': '/', 'secure': False, 'value': '{"auin":"-","sourcetype":"","sourcefrom":"","uin":"","visitor_id":"27069376021859215"}'}, {'domain': '.ke.qq.com', 'expiry': 1639791978, 'httpOnly': False, 'name': 'ts_uid', 'path': '/', 'secure': False, 'value': '8417595606'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '5784222450'}, {'domain': '.ke.qq.com', 'expiry': 1576721777, 'httpOnly': False, 'name': 'ts_last', 'path': '/', 'secure': False, 'value': 'ke.qq.com/course/list'}]
for x in va:
    print(x["name"]+"  "+x["value"])