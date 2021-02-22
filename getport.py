#encoding:utf-8
from os import linesep
from typing import ValuesView


input1 = open('G:\PYTHON\port.txt','r')
output1 = open('G:\PYTHON\porttemp.txt','w')

lines = input1.readlines()
for line in lines:    
    if 'servers' in line:
        continue
    elif 'Local' in line:
        continue
    output1.write(line)
input1.close()
output1.close()

input2 = open('G:\PYTHON\porttemp.txt','r')
output2 = open('G:\PYTHON\portfinal.txt','w')

lines = input2.readlines()
for i in range(0,len(lines)):
    lines[i] = lines[i].split(':')[1]
    output2.writelines(lines[i])
input2.close()
output2.close()

input3 = open('G:\PYTHON\portfinal.txt','r')
port = input3.readlines()
portexist1 = {}
# print(port[0].split('\n')[0])
for i in range(0,len(port)):
    portexist1[i] = port[i].split('\n')[0]
    # portexist1 = portexist1.append(portexist1[i])
    # print(portexist1[i])
# print(portexist)
input3.close()
portexist2 = {}
for vee in portexist1.values():
    portexist2[vee] = vee
# print(portexist2)
# print(len(portexist2))
# print(type(portexist1.values()))
# print(portexist1.keys())
# print(type(portexist1))
# print(portexist1)

tac = {'baseport':0,'nginx1':1,'nginx2':2,'mng':4,'sac':5,'confd':6,'prd:master':7,'sms':18,'dnsd':19,'logd':30,'rptd1':31,'rptd2':32,
'vpninit':33,'mosquitto':37,'php':38,'iam1':40,'iam2':41,'iam3':42,'authz':43,'prdgm:master':44,'ldapimport':45,'go-adapter':50,
'athena':51,'cluster-daemon':54,'authn':55,'轻量IDA模块-基线配置模块':56,'轻量IDA模块-对TAC提供信任查询、设备管理相关接口':57,'cas server':58,
'前端页面':59,'safe':60}
print(len(tac))
#'rpc_provider':5835,'rpc_provider':5555端口暂不变更

logfile = open('G:\PYTHON\excute.log','w')
for ke,ve in portexist2.items():
    for k,v in tac.items():
        #判断端口失败
        if str(v) == ve:
            #python3
            print(k + '端口添加失败',file=logfile)
            #python2
            # print >> logfile,k + '端口添加失败'
        #判断端口成功
        elif str(v + 2000) == ve:
            #python3
            print(k + '端口添加成功',file=logfile)
            #python2
            # print >> logfile,k + '端口添加成功'
        else:
            #print >> logfile,k + '端口可能未启动'
            continue
logfile.close()
