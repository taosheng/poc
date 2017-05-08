#!/usr/bin/env python
import os 
import commands
import sys

if len(sys.argv) < 3 :
    print("usage ./<cmd> <apache_log_Path> <result_output_prefix")
    exit(0)

logPath=sys.argv[1]
resultPre=sys.argv[2]

toUnzipfilelist=[]
logfilelist=[]
prefix="access.log."
alllog=resultPre+"_all_log.csv"
print "mv previous log to another file..."
mv_log="mv "+alllog+" "+alllog+".tmp"
commands.getoutput(mv_log)

for r in range(1,20):
    toUnzipfilelist.append(prefix+str(r)+".gz")
    logfilelist.append(prefix+str(r))
    

print toUnzipfilelist
for (dirpath, dirnames, filenames) in os.walk(logPath):   
    for filename in filenames:
        if filename in toUnzipfilelist:
            cmd = "gunzip "+dirpath+ filename
            print cmd
            print commands.getoutput(cmd)


for f in logfilelist:
    cmd="cat {0}/{1} >> {2}".format(logPath, f,alllog)
    print cmd
    commands.getoutput(cmd)

aggregate_cmd ="cat "+alllog +"| awk '{split($6,array,\":\")} {print $5 \",\" array[1] \",\" $14}' | grep -v \"^-\" | sort | uniq -c | awk '{print $1 \",\" $2}'> "+resultPre+"_result.csv"
print "quick generate users/client statistics"
print aggregate_cmd
commands.getoutput(aggregate_cmd)
print "quick generate top 20 downloads"
top20_cmd ="cat "+alllog +"| grep GET | grep -v 'ClientSoftwareUpdates.xml' | grep -v 'favicon.ico' | grep -v '\/api\/v' | grep -v '\/B\/3\/Styles' | grep -v 'GET \/ '| grep -v 'robots.txt'| grep -v 'GET \/login' | grep -v 'GET \/\! ' |grep -v '\/Pages\/'| grep -v 'home '| awk '{print $9  }' | sort | uniq -c | sort -r | head -n20 | awk '{print $1 \",\" $2}'> "+resultPre+"_top_20download.csv"
relation_get_cmd ="cat "+alllog +"| grep GET | grep -v 'ClientSoftwareUpdates.xml' | grep -v 'favicon.ico' | grep -v '\/api\/v' | grep -v '\/B\/3\/Styles' | grep -v 'GET \/ '| grep -v 'robots.txt'| grep -v 'GET \/login' | grep -v 'GET \/\! ' |grep -v '\/Pages\/'| grep -v 'home '| awk '{print $9\"#\"$5  }' | sort -k1 | uniq  > "+resultPre+"_file_access.csv"


commands.getoutput(top20_cmd)
commands.getoutput(relation_get_cmd)
