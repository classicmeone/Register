from django.shortcuts import render
from django.http import HttpResponse
from .forms import Upload
from django.conf import settings
from .recognise import searchVid
from django.core.files.storage import FileSystemStorage
import os
import datetime
import json
# Create your views here.
def index(request):
    
    return HttpResponse("Welcome")

def loadform(req):
    
    frm = Upload()
    #st = static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    return render(req, 'faces/design.html', {'form':frm})


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
            link = fs.url(filename)
            imgsrc = os.path.join(settings.IMGSRC, nam) 
            imgsrc = os.path.join(imgsrc, filename) 
            stdate = datetime.datetime.strptime(stdate, "%Y-%m-%d").date() 
            endate = datetime.datetime.strptime(endate, "%Y-%m-%d").date()
            stdate = stdate.__str__()
            endate = endate.__str__()

            vids = [os.path.join(settings.MEDIA_URL, "videos/h.mp4"),os.path.join(settings.MEDIA_URL, "videos/damo.mp4")] # , os.path.join(setting.MEDIA_URL, "videos/kamal.mp4"),os.path.join(setting.MEDIA_URL, "videos/ibro.mp4"),os.path.join(setting.MEDIA_URL, "videos/g.mp4")] 
            
            result = searchVid(vids, imgsrc)


            data = {'Videos':result, "image":src , "stdate":stdate,"endate":endate, "link":link, 'msg':"welcome"}
            data = json.dumps(data)
            return HttpResponse(data, content_type="application/json")
            '''

            return render(req, "faces/result.html", data)
            
        
        else:
            return HttpResponse(frm.errors)
            '''
          
            
        
        else:
            return HttpResponse(frm.errors)