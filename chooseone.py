#每天一个人加班
import random
data = ['薛永龙','裴根','邓石林','王鸿','张琳']
for i in range(1,6):
    name = random.choice(data)
    data.remove(name)
    print('星期'+str(i)+'加班人员是:',name)   