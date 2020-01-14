from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
import requests
from .forms import Upload
from django.conf import settings
from django.urls import reverse
import os
import shutil
from django.core.files.storage import FileSystemStorage
from .source.extract_embeddings import feature_extraction
from .source.train_model import train_model
from .source.recognize_video import loader
from .source.storage_connect_Original import Videos
import datetime
from django.views import View
import json


def index(req):
    
    #city_weather = {"City": r[0]}
    return render(req, "index.html", {})
   # return HttpResponse("Welcome Home")
   
def getWeather(req):
    #urlC = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=dd3c7f19e254ddb73ac1bd4d0d360490"
    datas = {'coord': {'lon': -0.13, 'lat': 51.51}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'base': 'stations', 'main': {'temp': 295.89, 'pressure': 1019, 'humidity': 56, 'temp_min': 293.71, 'temp_max': 298.15}, 'visibility': 10000, 'wind': {'speed': 2.6}, 'clouds': {'all': 40}, 'dt': 1564747660, 'sys': {'type': 1, 'id': 1414, 'message': 0.0122, 'country': 'GB', 'sunrise': 1564719907, 'sunset': 1564775303}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}
    #urCall = urlC.format(city);
    #r = requests.get(urlC).json()
    r = datas
    cord = r['coord']
    weather = r['weather']
    #print(weather)
    description = weather[0]['description']
    longitude = cord['lon']
    latitude = cord['lat']
    temp = r['main']['temp']
    #print(temps)
    #temp = temps['temp']
    return render(req, "weather.html", {"temp":temp, "desc":description, "lon":longitude, "lat":latitude, "city":"Lagos"})

def search(req):
    
    if(req.POST):
        
        
        frm = Upload(req.POST, req.FILES)
        if(frm.is_valid()):
            img = req.FILES['image']
            stdate = req.POST['startdate']
            endate = req.POST['enddate']
            nam = req.POST['name']

            name = img.name
            src = os.path.join(nam,name)
            src = os.path.join("output", src)
            src = os.path.join("source", src)
            loc = os.path.join(settings.OUT, nam)
            fs = FileSystemStorage(location = loc)
            filename = fs.save(img.name, img)
            link = fs.url(filename) #os.path.join(loc, name)      #fs.url(filename)
            imgsrc = os.path.join(settings.IMGSRC, nam) 
            imgsrc = os.path.join(imgsrc, filename) 
            #name = settings.MEDIA_URL + 

            stdate = datetime.datetime.strptime(stdate, "%Y-%m-%d").date()  #(stdate)
            endate = datetime.datetime.strptime(endate, "%Y-%m-%d").date()
            stdate = stdate.__str__()
            endate = endate.__str__()

            vids = [os.path.join(settings.BASE_DIR, "media/videos/h.mp4"),os.path.join(settings.BASE_DIR, "media/videos/damo.mp4") , os.path.join(settings.BASE_DIR, "media/videos/kamal.mp4"),os.path.join(settings.BASE_DIR, "media/videos/ibro.mp4"),os.path.join(settings.BASE_DIR, "media/videos/g.mp4")] 
                    #,os.path.join(settings.VID, "index4.mp4")]
            #vids = [os.path.join(settings.BASE_DIR, "media/videos/h.mp4"),os.path.join(settings.BASE_DIR, "media/videos/b.mp4"), os.path.join(settings.BASE_DIR, "media/videos/c.mp4"),os.path.join(settings.BASE_DIR, "media/videos/d.mp4"),os.path.join(settings.BASE_DIR, "media/videos/e.mp4"),os.path.join(settings.BASE_DIR, "media/videos/f.mp4"),os.path.join(settings.BASE_DIR, "media/videos/g.mp4")] 
            #vid = Videos(stdate, endate)
            #vids = vid.blob_video()
            videos, msg = loader(vids,imgsrc)

            data = {'Videos':videos, "image":src , "stdate":stdate,"endate":endate, "link":link, 'msg':"welcome"}
            #return render(req, "update/result.html", {'Videos':videos, "image":src, "stdate":stdate, "endate":endate, "link":link, 'msg':msg})
            
            data = json.dumps(data)
            return HttpResponse(data, content_type="application/json")
            
        
        else:
            return HttpResponse(frm.errors)
            
            
def moveImg(f, name):
    #baseDir = settings.BASE_DIR
    
    path = settings.MEDIA_URL +"images/"+name
    with open(path) as dir:
        for chunk in f.chunks():
            dir.write(chunk)
        

    return path #"Images/" + name #os.path.join(sear, name)   

def testAjax(req):
    if(req.is_ajax()):
        
        vids = [os.path.join(settings.BASE_DIR, "media/videos/h.mp4"),os.path.join(settings.BASE_DIR, "media/videos/damo.mp4"), os.path.join(settings.BASE_DIR, "media/videos/kamal.mp4")]
        data = {'Videos':vids, "image":'src', "stdate":'stdate'}
        
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return Http404
    return {'working':True}
def loadform(req):
    
    frm = Upload()
    #st = static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    return render(req, 'update/design.html', {'form':frm})

def methodTest(req):
    
    return HttpResponse("Welcome")


