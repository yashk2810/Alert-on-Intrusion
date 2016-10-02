import re

new_file=open("/home/yash/auth",'w')
f=open("/var/log/auth.log",'r')
text=f.read()
failed=re.findall(r'failed|FAILED',text)
new_file.write(str(failed))
new_file.close()
