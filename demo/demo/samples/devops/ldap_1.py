#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
#date:2019/12/26
__author__ = 'xxx'
import ldap

# https://www.cnblogs.com/linxiyue/p/10250243.html

#https://support.microsoft.com/zh-cn/help/2977003/the-latest-supported-visual-c-downloads  https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads
#https://download.visualstudio.microsoft.com/download/pr/3b070396-b7fb-4eee-aa8b-102a23c3e4f4/40EA2955391C9EAE3E35619C4C24B5AAF3D17AEAA6D09424EE9672AA9372AEED/VC_redist.x64.exe
# visual c++ build tools的安装与使用 https://download.microsoft.com/download/5/f/7/5f7acaeb-8363-451f-9425-68a90f98b238/visualcppbuildtools_full.exe
# pip install python-ldap
# 还要安装一些环境，ubuntu：
#
# apt-get install build-essential python3-dev python2.7-dev \
#     libldap2-dev libsasl2-dev slapd ldap-utils python-tox \
#     lcov valgrind
# CentOS：
#
# yum groupinstall "Development tools"
# yum install openldap-devel python-devel
def get_userinfo_from_ldap():
    try:
        server = "ldap://10.10.82.222:10389"
        membersDN ="ou=people,dc=example,dc=com"
        groups_DN="ou=groups,dc=example,dc=com"

        conn = ldap.initialize(server)
        conn.set_option(ldap.OPT_REFERRALS, 0)
        conn.protocol_version = ldap.VERSION3
        filterstr = '(objectClass=organizationalPerson)'
        # 获取的字段
        attrlist = ['uid', 'displayName']
        conn.search(membersDN, ldap.SCOPE_ONELEVEL,
                    filterstr=filterstr, attrlist=attrlist)
        code, members = conn.result(timeout=3)

        name_map = {}
        for member in members:
            data = member[1]
            uid = data.get('uid', [''])[0].decode(
                encoding='utf-8')
            displayName = data.get('displayName', [''])[
                0].decode(encoding='utf-8')
            if uid:
                name_map[uid] = displayName
        conn.unbind_s()

        return True, name_map
    except ldap.LDAPError as e:

        return False
    pass

print(get_userinfo_from_ldap())


#
# from ldap3 import Server, Connection
# def Ldap_auth(username,pasword):
#     '''
#
#     :param username:你的用户名
#     :param pasword: 你的密码
#     :return: 验证成功：success 验证失败：invalidCredentials
#     '''
#     ldaphost = ("ldap://10.10.82.222:10389")
#     s = Server(ldaphost)
#     conn2 = Connection(s,user='uid={0},ou=people,dc=example,dc=com'.format(username) , password=pasword,check_names=True, lazy=False,raise_exceptions=False)
#     conn2.bind()
#     return conn2.result["description"]
#
# ret=Ldap_auth('zhanggen','zhanggen123.com')
# print(ret)