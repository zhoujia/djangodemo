from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from ucloud_api import *
import subprocess
# Create your views here.

def index(req):
    return render_to_response('index.html', {'name':'zhoujia1227'})

def turnon(req):
    
    turnonCommStr = api_turnon()
    responseJson = subprocess.call(["curl",turnonCommStr])
    return render_to_response('index.html', {'statusJson':responseJson})

def turnoff(req):
    turnoffCommStr = api_turnoff()
    responseJson = subprocess.call(["curl",turnoffCommStr])
    return render_to_response('index.html', {'statusJson':responseJson})

def checkComStatus():
    checkCommStr = api_checkstatus()
    responseJson = subprocess.call(["curl",checkCommStr])
    return render_to_response('index.html', {'status':responseJson})


#turnoff()