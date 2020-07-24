import subprocess
import time, sys, os
import getpass

GIT = "https://github.com/aboul3la/Sublist3r.git"
PATH = '../AutoXss/Sublist3r'
username = getpass.getuser() # kullanıcın sistemdeki username ni alıyoruz

if os.path.exists('/home/'+username+'/AutoXss/'+'Sublist3r'):
    print("You have the sublist3r :) ")
else:
    subprocess.check_output("git clone "+GIT, shell=True)
    print("Sublist3r installed :) ")
