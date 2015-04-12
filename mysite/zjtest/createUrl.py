'''
Created on 2015-4-8

@author: zhoujia
'''
import hashlib
import urlparse
import urllib
import base64

baseUrl = 'https://api.ucloud.cn/'
public_key = 'ucloudliao@tarena.com.cn14280420270002130655531'
private_key = 'a169cf0457da7acf918a1e423847944ae6b255be'


def paramURL(url):
    str = url.split("&")
    str.sort();
    #print str
    d={}
    for par in str:
        key = par.split("=")[0]
        value = par.split("=")[1]
        if key == 'Password' or key == 'password':
            value = base64.b64encode(value)
        d[key] = value
    return d
    #end paramURL

def _verfy_ac(private_key, params):
    items=params.items()

    items.sort()

    params_data = "";
    for key, value in items:
        params_data = params_data + str(key) + str(value)
    params_data = params_data + private_key

    sign = hashlib.sha1()
    sign.update(params_data)
    signature = sign.hexdigest()

    return signature
    #end _verfy_ac

def createURL(url):
    params = paramURL(url)
    signature = _verfy_ac(private_key, params)
    paramArray = url.split("&")
    i = 0
    for par in paramArray:
        key = par.split("=")[0]
        value=par.split("=")[1]
        if key == 'password' or key == 'Password':
            value = base64.b64encode(value)
            paramArray[i] = key + "=" +value
        i+=1
            
    newUrl = ''
    i = 0
    for par in paramArray:
        if i < len(paramArray)-1:
            newUrl = newUrl + par + "&"
        elif i == len(paramArray)-1:
            newUrl = newUrl + par
    url = baseUrl + '?' +newUrl + 'Signature='+signature
    return url
    #end createURL
    


#example   uhost-0oahn4

#print createURL('Action=CreateUHostInstance&CPU=1&ChargeType=Trial&DiskSpace=50&ImageId=uimage-qiut5g&LoginMode=Password&Memory=2048&Name=UCloudExample01&PublicKey=ucloudliao@tarena.com.cn14280420270002130655531&Password=123456&Region=cn-north-03')
    
    
    