import os
import sys
import platform
import socket

# machine and processor type
print(platform.machine())
print(platform.architecture())

# get default socket timeout
print(socket.getdefaulttimeout())
# set default time for socket to 50 seconds
socket.setdefaulttimeout(50)
print(socket.getdefaulttimeout())

# get operating system name
print(os.name)
print(platform.system())

# get process id
print(os.getpid())

# open file using os module instead of with open
f_name = "fdpractice.txt"
f = os.open(f_name, os.O_RDWR | os.O_CREAT)
print(f)

f_obj = os.fdopen(f, "a+")
print(f_obj)
f_obj.close()

# ----- fork a new process for mac and linux ------
# print("Before fork: ", os.getpid())
# p = os.fork()
# print("After fork: ", p)
# if p == 0:
#     print("Child process")
#     print("Parent process PID ", os.getppid())
# else:
#     print("Parent process")
#     os.wait()
#     print("Child process PID ", p)

# ------ fork a new process for windows -----
# context = mp.get_context('spawn')
# p = context.Process(target=function_name, args=(q,))
# p.start()
# p.join()
