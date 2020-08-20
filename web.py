#!/usr/bin/python3

import subprocess
import cgi

print("content-type: text/html")
print()
mydata = cgi.FieldStorage()
myx = mydata.getvalue("x")
myy = mydata.getvalue("y")
myz = mydata.getvalue("z")
osname = mydata.getvalue("os")
volname = mydata.getvalue("vol")
volpath = mydata.getvalue("pathofvolume")
patting = mydata.getvalue("patting")
patting2 = mydata.getvalue("pattingpath")
imagename = mydata.getvalue("image")
newvolumecreate = mydata.getvalue("createvol")
newnetworkcreate = mydata.getvalue("newnetwork")
newnetworkcreatename = mydata.getvalue("networkname")
pullimage = mydata.getvalue("pullimg")
pullversion = mydata.getvalue("version")
outputofdocker = mydata.getvalue("mydocker")
startcontainer = mydata.getvalue("start")
stopcontainer = mydata.getvalue("stop")
useraddc = mydata.getvalue("user")
if(myx):
    centos = "sudo docker run -dit --name {} centos:7".format(myx)
    o = subprocess.getoutput(centos)
    print(o)
if(outputofdocker):
    subprocess.getoutput("sleep 2")
    k = "sudo docker {}".format(outputofdocker)
    newout = subprocess.getoutput(k)
    print(newout)
if(pullimage or pullversion):
    imagepull = "sudo docker pull {}:{}".format(pullimage,pullversion)
    pulling = subprocess.getoutput(imagepull)
    print(pulling)
if(newnetworkcreate or newnetworkcreatename):
    network = "sudo docker network create --driver {} {}".format(newnetworkcreate,newnetworkcreatename)
    networkoutput = subprocess.getoutput(network)
    print(networkoutput)
if(newvolumecreate):
    vol1 = "sudo docker volume create {}".format(newvolumecreate)
    voloutput = subprocess.getoutput(vol1)
    print(voloutput)
if(myy):
    ubuntu = "sudo docker run -dit --name {} ubuntu:14.04".format(myy)
    o2 = subprocess.getoutput(ubuntu)
    print(o2)
if(myz):
    httpd = "sudo docker run -dit --name {} httpd".format(myz)
    o3 = subprocess.getoutput(httpd)
    print(o3)
if(osname or volname or volpath or patting or patting2 or imagename):
   container = "sudo docker run -dit --name {} -v {}:{} -p {}:{} {}".format(osname,volname,volpath,patting,patting2,imagename)
   o4 = subprocess.getoutput(container)
   print(o4)
if(startcontainer):
    container = "sudo docker start {}".format(startcontainer)
    o = subprocess.getoutput(container)
    print(o)
if(stopcontainer):
    container = "sudo docker stop {}".format(stopcontainer)
    o = subprocess.getoutput(container)
    print(o)
if(useraddc):
    use = "sudo useradd {}".format(useraddc)
    o = subprocess.getoutput(use)
    print(o)

