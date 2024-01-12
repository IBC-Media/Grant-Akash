import dataPushToChain
import dataPullFromChain

def adjust(ip:str)-> str:
    op = '0x' + ip
    for i in range(len(ip),31):
        op += '0'
    return op

filename = 'devid_321_t_12094533455'
CID = '0x00000000000000000000000000001430'

dataPushToChain.pushData(adjust(filename),CID)

data = (dataPullFromChain.retrieveData(adjust(filename)).split())[4]
print("CID is ", data)