'''
Created on 2015-4-12

@author: zhoujia

'''
from createUrl import *

turnonCommand = '''Action=StartUHostInstance&PublicKey=ucloudliao@tarena.com.cn14280420270002130655531&Region=cn-north-03&UHostId=uhost-05bide'''
turnoffCommand = '''Action=StopUHostInstance&PublicKey=ucloudliao@tarena.com.cn14280420270002130655531&Region=cn-north-03&UHostId=uhost-05bide'''
checkCommand = '''Action=DescribeUHostInstance&PublicKey=ucloudliao@tarena.com.cn14280420270002130655531&Region=cn-north-03&UHostIds.0=uhost-05bide&Offset=0&Limit=20'''
def api_turnon():
    allCommand = createURL(turnonCommand)
    return allCommand

def api_turnoff():
    allCommand = createURL(turnoffCommand)
    return allCommand

def api_checkstatus():
    allCommand = createURL(checkCommand)
    return allCommand

