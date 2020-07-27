import requests
from bs4 import BeautifulSoup
url = 'http://apitest.frontierutilities.com/WebAPI.asmx'
body= """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
<soap:Body>
<Authentication xmlns="http://tempuri.org/">
<Authenticate>
<UserName>WTB_01</UserName>
<Password>OmhY6397</Password>
</Authenticate>
</Authentication>
</soap:Body>
</soap:Envelope>"""
headers =  {'Content-Type' : 'text/xml', 'Cookie' : 'AspxAutoDetectCookieSupport=1'}
response = requests.post(url, data=body , headers = headers)
soup = BeautifulSoup(response.text,'xml')
ID = soup.find('SessionID')
# print(k.text)
xml = '''<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <GetProducts xmlns="http://tempuri.org/">
                    <SessionID>a^IrpEKnZqRSq%WKb0Ci37Ig6</SessionID>
                </GetProducts>
            </soap:Body>
        </soap:Envelope>'''
plans = {'sessionid': 'a^IrpEKnZqRSq%WKb0Ci37Ig6','Cookie' : 'AspxAutoDetectCookieSupport=1','Content-Type' : 'text/xml'}
plans_data = requests.post(url, data=xml, headers=h)
print(plans_data.text)









