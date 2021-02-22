# import datetime
# from time import time
# a = datetime.date.today()
# b = int(time())
# print(a,b)
# tac = {'baseport':0,'nginx':2,'nginx':3,'mng':4,'sac':5,'confd':6,'prd:master':7,'sms':18,'dnsd':19,'logd':30,'rptd':31,'rptd':32,
# 'vpninit':33,'mosquitto':37,'php':38,'iam':40,'iam':41,'iam':42,'authz':43,'prdgm:master':44,'ldapimport':45,'go-adapter':50,
# 'athena':51,'cluster-daemon':54,'authn':55,'轻量IDA模块-基线配置模块':56,'轻量IDA模块-对TAC提供信任查询、设备管理相关接口':57,'cas server':58,
# '前端页面':59,'safe':60}
# #'rpc_provider':5835,'rpc_provider':5555端口暂不变更
# #baseport =[]
# portfinal = []
# for k,v in tac.items():
#     if v is in portfinal：
# #     print(k,v)
# #     print(type(v))
# #     baseport.append(v)
# # print(baseport)
# for i in range(0,4):
#     print(i)
import os

# vpnip = '10.92.2.237'

# # input = open('G:\PYTHON\devicelist.txt','r')
input = open(os.getcwd() + '\devicelist.txt','r')

# lines = input.readlines()

# # print(lines)

# datagroup = []

# for line in lines:
#     line = line.strip('\n')
#     data = line.split(':')
#     datagroup.append(data)

# # print(datagroup)
# # print(datagroup[0])

# for i in range(len(datagroup)):
#     if datagroup[i][0] == vpnip:
#         networkport = datagroup[i][1]
#         innerip = datagroup[i][2]

# print(networkport,innerip)


# print(os.getcwd())


inputa = open(os.getcwd() + '\\vpnip.txt','r')

vpnip = inputa.readline()

print(vpnip,type(vpnip))


#to do