import dataPushToChain

def adjust(ip:str)-> str:
    op = '0x' + ip
    for i in range(len(ip),31):
        op += '0'
    return op

filename = 'devid_231_t_11694533455'
CID = '0x0000000000000000000000000000111'

dataPushToChain.pushData(adjust(filename),CID)