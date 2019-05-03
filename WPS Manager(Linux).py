import os
import subprocess
import re 

##GETTING FILELIST IN DIRECTORY
my_list=[]
pass_list=[]

p = subprocess.Popen("ls /etc/NetworkManager/system-connections", stdout=subprocess.PIPE, shell=True)
output,err = p.communicate()
p_status = p.wait()

##CONVERTING BINARY OUTPUT TO NORMAL OUTPUT
output = output.decode('ascii')

file_list = output.split('\n')

for i in file_list:
	try:
		file_address = "/etc/NetworkManager/system-connections/%s"%(i)
		with open(file_address, 'r') as my_file:
			
			data = my_file.read()
			if(re.search("psk=\w{1,20}", data)):
				pass_list += re.findall("psk=\w{1,20}", data)
				my_list += re.findall("ssid=\w{1,20}",data)
			
	except Exception as e:
		pass

for i in range(len(my_list)):
	print("WIFI POINT NO %d :"%(i+1))
	print("*****************************************************")
	print("WIFI NAME = ", end='')
	print(file_list[i].split('.')[0])
	print("Password :", end='')
	print(pass_list[i][4:])
	print("*****************************************************\n\n")


