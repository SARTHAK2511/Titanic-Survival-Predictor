
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import pickle
from matplotlib import image 
import numpy as np
# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")

def result(request):
   
    predictor=pickle.load(open('ModelTrainedDeploy',"rb"))
    lis=[]
    lis.append(int(request.GET['Pclass']))
    lis.append(int(request.GET['Age']))
    lis.append(int(request.GET['SibSp']))
    lis.append(int(request.GET['Parch']))
    lis.append(int(request.GET['Fare']))
    lis.append(int(request.GET['Male']))
    lis.append(int(request.GET['Q']))
    lis.append(int(request.GET['S']))
    print(lis)
  
    
    print(lis)
    
    prediction =predictor.predict([lis])
    print(type(prediction))
    
    # return render(request,'result.html',{'result':prediction})
    if result==1:
        return render(request,'result.html',{'result':'Sorry , the passender died '})
    else :
        return render(request,'result.html',{'result':'Hurray ! the passenger survived '})
