import requests
from requests.sessions import TooManyRedirects

ip = '10.92.2.192'
url1 = 'https://%s:8443/admin/' % ip
url2 = 'https://%s:8443/admin/account/mod_password_action.php' % ip
s = requests.session()
headers2 = {'Host': '%s:8443' % ip,
            'Refer':url2}
postdata = {'oldpassword': '!1fw@2soc#3vpn',
            'password': 'admin@1234',
            'repassword': 'admin@1234'}
r = s.post(url2, postdata, headers=headers2, verify=False, allow_redirects=False)
print(r)


