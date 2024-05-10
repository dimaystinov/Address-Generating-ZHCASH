from bitcoinaddress import Wallet
import json
import pprint

def get_new_address():
    wallet = Wallet()
    # print(wallet)
    wallet_dict = json.loads(str(wallet))
    pprint.pprint(wallet_dict)
    return {"address": wallet_dict["Public_Address_1_compressed"], "privkey": wallet_dict["Private_Key_WIF_compressed"]}


print(get_new_address())
