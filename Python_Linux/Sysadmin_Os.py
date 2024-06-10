import os
uid=os.getuid()
print(uid)

l=os.listdir("/home/alumno")

for i in l:
    print(i)

p=os.system("ls -l")
print(p)

print(os.uname().version)
