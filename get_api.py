from re import A
import socket
from types import CoroutineType
from urllib import response
# from getmac import get_mac_address as gma
import requests






# # mac=gma()
# # print("Your mac address=",mac)


# hostname = socket.gethostname()   
# ip = socket.gethostbyname(hostname)   
# # print(gma())
# # print("Your Computer Name is:" + hostname)   
# # print("Your Computer IP Address is:" + IPAddr) 




# cn=input("Enter Your Company Name=")
# # u=input("Enter Your User Name=")
# # a=input("Enter Your address=")
# p=input("Enter Your Phone Number=")
# e=input("Enter Your E-mail=")
# # pas=input("Enter Your Password=")
# print("=================================")
# print("Your Company Name=",cn)
# # print("Your User Name=",u)
# # print("Your Address=",a)
# print("Your Phone Number=",p)
# print("Your E-mail=",e)
# # print("Your Password =",pas)

# # print("Your ip address=",ip)
# mac=gma()
# # print("Your mac address=",mac)



import json 
import requests 


# url = "http://127.0.0.1:8000/api/all"


# # api_url1 = "project/getapi.py"
# data={
#     "name":a,
#     "address":b,
#     "phonenumber":c,
#     "email":d,
#     "ip":IPAddr,
#     "mac":mac
# }
# re = requests.post(url=url,data=data)
# re.json()




# api_url = "http://127.0.0.1:8000/api/create/"
# todo = {
#         "name": "xyz",
#         "phone_number": "/95378402362",
#         "gmail": "names@gmail.com",
#         "address": "rajkot"
#     }
# headers =  {"Content-Type":"application/json"}
# response = requests.post(api_url, data=json.dumps(todo), headers=headers)
# print(response.json())


# response.status_code


def add_data(): 
    URL="http://127.0.0.1:8000/api/all/" 
    # URL="https://3duser.infiniteai.co.in/api/key-generate"     ip_address mac_address id=23
    # URL="https://3duser.infiniteai.co.in/api/key-verify"        key 
    data= {
        # "name": cn,
        # # "username":u,8000705534 test@argus.com
        # "mobile": p,
        # "email": e,
        # "address": a,
        # "password":pas,
        # "ipaddress":ip,
        # "macaddress":mac,

         
    } 
    # json_data=json.dumps(data) 
        # r=requests.post(url=URL, data=json_data )
    
    # r = requests.post(URL OR VARIABLE, data=YOUR VARIABLE, headers={ 'user-agent': 'I am a BOT script' })
    #     print(r.json()) 
    
    
    r=requests.get(url=URL, data=data,headers={ 'user-agent': 'I am a BOT script' }) 
    # print(r)
    # data=r.json() 
    print("====================== api data ======================")

    print(r.json()) 

    # r=requests.post(url=URL, data=data,headers={ 'user-agent': 'I am a BOT script' }) 
    datas=r.json() 


    # a=datas['details']['customer_name']
    # b=datas['details']['address1']
    # c=datas['details']['state']
    # d=datas['details']['city']
    # es=datas['details']['pincode']
    # global id
    # id=datas['details']['id']
    # print("===================== show data =======================")
    # print('customer_name => ',a)    
    # print('address1 => ',b)
    # print('state => ',c)
    # print('city => ',d)
    # print('pincode => ',es)
    

add_data()

