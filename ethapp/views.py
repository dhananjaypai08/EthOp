from tabnanny import check
from django.shortcuts import render
import eth_tester
from web3 import Web3
import json
from decouple import config

web3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{str(config("NODEKEY"))}'))
# Create your views here.



# Manually added functions
def add_json_data(data):
    ''' This is to convert dict to json and write it into json file'''
    
    ddata = dict(data)
    for k,v in ddata.items():
        k = str(k)
        v = str(v)
        ddata[k] = v
    ddata = str(ddata)
    json_data = json.dumps(ddata, indent=4)
    with open("C:/Users/dhana/coding/Personal Projects/web3/web3django/ethproject/static/data.json", 'w') as file:
        file.write(json_data)
    print("data added")





def home(request):
    return render(request, 'index.html')
                

def blocklookup(request):
    msg = {}
    dflag = 0
    if request.method=='POST':
        if not web3.isConnected():
            msg = {"msg": "HTTPProvider not connected to web3"}
            dflag = 1
        else:
            address = request.POST.get('address')
            checkconnection = request.POST.get('checkconnection')
            print(checkconnection)
            try:
                data = web3.eth.get_block(address)
                if checkconnection:
                    msg["Connected"] = web3.isConnected()

                msg["msg"] = "Data generated Successfully"
                msg["data"] = data
                add_json_data(msg["data"])
                dflag = 2
                
            except:
                msg = {"msg": "Please add correct block hash or number"}
                dflag = 3
        msg['signal']=dflag
        print(msg)
        
    return render(request, 'lookup.html',msg)

def getBalance(request):
    """ find the amount of ether owned by an account."""
    msg = {}
    msg['signal'] = -1
    if request.method=='POST':
        address = request.POST.get('publicaddress')
        ans = request.POST.get('exampleRadios')
        try:
            balance = web3.eth.get_balance(address)
            if ans=='eth':
                balance = web3.fromWei(balance, 'ether')
            msg['signal'] = 1
            msg['balance'] = balance
        except:
            msg['signal'] = 0
            msg['msg'] = "PUBLIC ADDRESS NOT FOUND"
    return render(request, 'checkbalance.html',msg)