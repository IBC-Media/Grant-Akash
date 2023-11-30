# import json
# import requests

# header ={
#     'authorization':"Bearer ya29.a0AfB_byCst9G8jtXSfWwAbThXlTfwNy_V3FE1daCyMqlsJXoRB5KkukVKUYIRQhpjM_T9VDMtViOV0yPWEWyKGDokLZ5w1P_fEyoJ0lLNLDa7Tuf-jRWuJSXaPVm3agwBw01TsNdLvN-55PlaKbd3awSeeDyKjLvbMBmHaCgYKAY8SARISFQHGX2MiB1amtnjbNW2YPPeZ1s8VXw0171"
# }

# param = {
#     'name':'test.jpg',
#     'parents':[1OCZ1AtZMjkM_sL2vEn5psaVN1oLHXri9?hl=en_GB]
# }

# file={
#     "data" :()'metadata',json.dumps(param),application/json;charset=UTF-8),
#     'file' :('test.jpg',open('filename',rb),'image/jpeg')

# }
# responce = requests.post(
#     "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"
#     headers=header,
#     files=files
# )

# if  responce.status_code==200:
#     print("File uploaded sucessfully")
# else:
#     print ("Unsucessful file upload")
    
    
    
import json
import requests
def demo():
    headers = {
    'Authorization': 'Bearer ya29.a0AfB_byAUA0CpAp_nbY8zpRM9b0C3Byjo4Nw5F_isA-6_nTkxbjLtlQFTIIpNHS4UjIut3CiPKD7NbTpBCYy8_kKyMYNynaDcZgHVF1bV_btkmkjd8b0ke7fRXDZ7_qGG2pb4-uSd3SswQH_lfMoq3HamGWuOw0a4c3rpaCgYKAQISARISFQHGX2MihuITcscJK5uHJX6UIJHikA0171',
    }

    params = {
    'name': 'test.txt',
    'parents': ['1OCZ1AtZMjkM_sL2vEn5psaVN1oLHXri9'],
    }

    files = {
    'data': ('metadata', json.dumps(params), 'application/json;charset=UTF-8'),
    'file': ('test.txt', open('C:/xampp/htdocs/blob1/images_encrypted/encrypted_images.json', 'rb'), 'image/jpeg'),
    }

    response = requests.post(

    'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart',
    headers=headers,
    files=files
    )

    if response.status_code == 200:
        print("File uploaded successfully")
    else:
        print("Unsuccessful file upload")
    print(response.text)
