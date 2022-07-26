from django.shortcuts import render
from django.views import View
from .models import Timing, Equipment

# Create your views here.
class MainPageView(View):
    template_name = 'MainPage/index.html'


    def get(self, request, *args, **kwargs):
        timing = Timing.objects.all()
        equipment = Equipment.objects.all()
        context = {'times': timing,
                   'equipment': equipment}
        return render(request, self.template_name, context)
