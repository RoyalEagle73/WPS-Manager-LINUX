import os
import subprocess
import re 

##GETTING FILELIST IN DIRECTORY
my_list=[]
pass_list=[]
file_list=[]
ret_data = "************** ~WIFI PASSWORDS FETCHED~ **************\n\n\n"

def script():
	global ret_data
	global my_list
	global pass_list
	global file_list
	file_list_2=[]

	p = subprocess.Popen("ls /etc/NetworkManager/system-connections", stdout=subprocess.PIPE, shell=True)
	output,err = p.communicate()
	p_status = p.wait()
		##CONVERTING BINARY OUTPUT TO NORMAL OUTPUT
	output = output.decode('ascii')

	file_list = output.split('\n')
	for i in file_list:
		file_list_2.append(i)
		try:
			file_address = "/etc/NetworkManager/system-connections/%s"%(i)
			try:
				with open(file_address, 'r') as my_file:			
					data = my_file.read()
					if(re.search("psk=\w{1,20}", data)):
						pass_list += re.findall("psk=\w{1,20}", data)
					else:
						not_present = i
						file_list_2.remove(not_present)
			except Exception as e:
				pass
		except Exception as e:
			pass

	for i in range(len(file_list_2)):
		try:
			ret_data +=  "WIFI POINT NO %d :\n"%(i+1) + "*****************************************************\n" + "WIFI NAME : %s\n"%(file_list_2[i].split('.')[0]) + "Password  : %s\n"%(pass_list[i][4:]) + "*****************************************************\n\n"
		except Exception as e:
			pass		

	return ret_data

print(script())