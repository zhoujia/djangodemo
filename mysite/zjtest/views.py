from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from ucloud_api import *
import subprocess
# Create your views here.

def index(req):
    return render_to_response('index.html', {'status':checkState()})

def turnon(req):
    
    turnonCommStr = api_turnon()
    runJson = subprocess.call(["curl",turnonCommStr])

    return render_to_response('index.html', {'statusJson':runJson,'status':checkState()})

def turnoff(req):
    turnoffCommStr = api_turnoff()
    runJson = subprocess.call(["curl",turnoffCommStr])
    
    return render_to_response('index.html', {'statusJson':runJson,'status':checkState()})

#check status
def checkComStatus(req):
    return render_to_response('index.html', {'status':checkState()})


def checkState():
    checkCommStr = api_checkstatus()
    responseJson = subprocess.check_output(["curl",checkCommStr])
    responseJson = eval(responseJson)
    return responseJson['UHostSet'][0]['State']

#turnoff()
