# backend.py

web_address_dict = {
    '10:45:25_31/11/2023': './assets/loading.gif',
    # Add more button-web address mappings as needed
}

def downloadAndDecrypt(filename: str):
    print(filename)


def fetch_web_address(button_name):
    web_address = './assets/'
    web_address += button_name
    web_address += '.jpg'
    if web_address is not None:
        return web_address
    else:
        raise ValueError('Button not found')
