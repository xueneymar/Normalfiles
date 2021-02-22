#每天两个人加班
import random,numpy
data = ['薛永龙','裴根','邓石林','王鸿','张琳']
unit = []
firstname = random.choice(data)
secondname = random.choice(data.remove(firstname))
unitelement = firstname + ',' + secondname
unit.append(unitelement)
print(unit)  