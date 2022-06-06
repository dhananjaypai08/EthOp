from django.shortcuts import render
import eth_tester
from web3 import Web3
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/17f47a2bd9d44d81b5c002e6b6fbb045'))
# Create your views here.

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
            
            try:
                data = web3.eth.get_block(address)
                msg["msg"] = "Data generated Successfully"
                msg["data"] = data
                dflag = 2
            except:
                msg = {"msg": "Please add correct block hash or number"}
                dflag = 3
        msg['signal']=dflag
        print(msg)
        
    return render(request, 'lookup.html',msg)