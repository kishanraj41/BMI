from django.shortcuts import render
from django.views import View

class BMIForm(View):
    def get(self,request):
        errorMessage = ""
        bmi = 0

        try:
            weight = int(request.GET.get("weight",0))
            if weight <= 0:
                errorMessage = errorMessage + "weight must be > 0; weight = " + weight + "\n"
        except(TypeError):
            errorMessage = errorMessage + "invalid weight: " + request.GET["weight"] + "\n"

        try:
            height = int(request.GET.get("height",0))
            if height <= 0:
                errorMessage = errorMessage + "height must be > 0; height = " + height + "\n"
        except(TypeError):
            errorMessage = errorMessage + "invalid height: " + request.GET["height"] + "\n"

        if len(errorMessage) == 0:
            bmi = 703*weight/(height*height)
        return render(request,"form.html",{"bmi":bmi,"message":errorMessage})
        #bonus question: what should be done to this code to eliminate redundancy?



