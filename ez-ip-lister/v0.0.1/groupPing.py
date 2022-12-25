import os

osType = ["Windows", "Linux"]
osSelect = 0

print("Select your OS")
print("[0] Windows")
print("[1] Linux")

osSelected = int(input("Press 0 for Windows and 1 for Linux: "))

if (osSelected == 0 or osSelected == 1):
    osSelect = osSelected
    print("Pinging for " + osType[osSelect])
else: 
    print("Invalid input. Taking default value [0]")

with open("ip_list.txt") as file:
    park = file.read()
    park = park.splitlines()
    print(" {park}  \n")
    # ping for each ip in the file
    
for ip in park:
    
    if (osSelected == 1): 
	    response = os.popen(f"ping -c 1 {ip} ").read()
    if (osSelected == 0): 
	    response = os.popen(f"ping -n 1 {ip} ").read()
    # Pinging each IP address 1 time
    
    #saving some ping output details to output file
    if("Request timed out." or "unreachable") in response:
	    print("UP")
	    print(response)
	    f = open("ip_output.txt","a")
	    f.write(response + '\n')
	    f.write("===========================================================================================" + '\n')
	    f.close() 
    else:
	    print("DOWN")
	    print(response)
	    f = open("ip_output.txt","a")  
	    f.write(response + '\n')
	    f.write("===========================================================================================" + '\n')
	    f.close() 
    # print output file to screen
with open("ip_output.txt") as file:
    output = file.read()
    f.close()
    print(output)
with open("ip_output.txt","w") as file:    
	pass
