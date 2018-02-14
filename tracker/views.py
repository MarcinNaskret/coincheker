from django.shortcuts import render
from tracker.forms import indexForm





def index(request):
    template_name = 'tracker/home.html'







    def get(self,request):
        form = indexForm()
        return render(request,self.template_name, {'form':form})





    return render(request, 'tracker/home.html')


