
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect, request
from pytube import YouTube



# Create your views here.
def index(request):
    return render(request,'index.html')
    
def youtubevideo(request):
    qulity360pbt = False
    qulity480pbt =False
    qulity720pbt =False
    
    if request.method =='POST':
        yturl =request.POST.get('url')
        yt = YouTube(yturl)
        title = yt.title
        thumbnail = yt.thumbnail_url
        st =yt.streams.filter(progressive=True)
        if st !=0:
                qulity360p = yt.streams.filter(res="360p",progressive=True)
                if qulity360p !=0:
                    print("360p Avalable")
                    print(qulity360p[0].url)
                    qulity360pbt =True
                    url360 = qulity360p[0].url
                    
                # qulity480p = yt.streams.filter(res="480p", progressive=True)
                # if qulity480p != 0:
                #     print("480p Avalable")
                #     print(qulity480p[0].url)
                #     qulity480pbt =True    
                #     url480 =qulity480p[0].url
                qulity720p = yt.streams.filter(res="720p",progressive=True)
                if qulity720p !=0:
                    print("720p Avalable")
                    print(qulity720p[0].url)
                    qulity720pbt =True
                    url720 =qulity720p[0].url
        return render(request,'avalableformat.html',context={'qulity360pbt':qulity360pbt,'qulity480pbt':qulity480pbt,
                                                                 'qulity720pbt':qulity720pbt,'url360':url360,'url720':url720,
                                                                 'title':title,'thumbnail':thumbnail})
        
   
        
    return render(request,'index.html')