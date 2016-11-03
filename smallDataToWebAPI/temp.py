
from string import Template
all = open('autoGenConfig.xml.temp','r').read()

output = Template(all)
d = {"jdbc-connection-URL":'sqlite::xxx/itTalent','jdbc-driver':"",
"jdbc-driver-classname":""}
print output.substitute(d)
         #>>> s.substitute(driver='sqlite.jdbc.driver')

#output = output.substitute(jdbc-driver='net.org.sqlite')
# s = Template('<jdbc driver="${driver}">')

print output
