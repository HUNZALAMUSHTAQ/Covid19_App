from django.http import JsonResponse
from urllib import response
from django.shortcuts import render , HttpResponse 
import requests
from django.views import View
import pandas as pd


# Create your views here.
# def handler404(request, exception):
#     response.status_code = 404
#     return render(request , "404.html",{"exception" : exception})

class IndexView(View):
    def get(self, request):
        data = True
        response = None 
        countries = None 
        while data :
            try :
                response = requests.get("https://api.covid19api.com/summary")
                data = False
            except : 
                data = True 
        globalData = response.json()["Global"]
        countries = response.json()["Countries"]
        result = {"result":globalData , "countries" : countries }
        return render(request , 'index.html',result)
    
    
    
class CountryView(View) : 
    def post(self,request) : 
        country_name = request.POST["countryname"]
        if country_name : 
            result = {}
            response = None 
            Data = True 
                
            while Data : 
                try : 
                    response = requests.get(f"https://api.covid19api.com/country/{country_name}")
                    Data = False 
                except : 
                    Data = True
                    
            result["Data"] = response.json()
            if "message" in result["Data"] : 
                pass
            else :
                result["Data"] = response.json()[-1]
            
            return render(request , 'countrydata.html' , result)
        else :
            return HttpResponse("Enter Country Name Please" )

def get_data(request ,countryname ,  *args, **kwargs) :
    flag = True
    response = None 
    countryname = countryname       
    print(request.POST , request.GET)
    print(countryname)
    Data = {"sucess":False,"alldata" : "" , "labels" : ""}
    while flag : 
        try : 
            response = requests.get(f"https://api.covid19api.com/country/{countryname}")
            flag = False

        except : 
            flag = True
    Data["sucess"] =response.json()
    if "message" in Data["sucess"] : 
        print("=============Sadly")
    else : 
        data = response.json()
        df = pd.DataFrame.from_records(data)
        dic = {"Date": "t" , "Confirmed" : "y"}
        alldata  = df[["Date", "Confirmed"]]
        pd.options.mode.chained_assignment = None 
        alldata.rename(columns=dic,inplace=True)
        max_data = alldata.groupby(alldata['t'], as_index=False).agg(int).to_dict(orient="records")
        label = alldata["t"].tolist()
        
        Data['alldata'] = max_data
        Data['labels'] = label
        Data['sucess']  = True
    
    return JsonResponse(Data)