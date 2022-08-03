from django.shortcuts import render
from django.views import View
from .models import Schedule, Equipment
from django.utils import timezone


class MainPageView(View):
    template_name = 'MainPage/index.html'

    def get(self, request, *args, **kwargs):
        schedule = Schedule.objects.filter(
            date__gte=timezone.now().date(),
            date__lt=timezone.now().date() + timezone.timedelta(10)
        )
        schedule = [(item.date, True) for item in schedule]  # True means working day

        for day in range(0, 10):
            cur_date = timezone.now().date() + timezone.timedelta(day)
            if (cur_date, True) not in schedule:
                schedule.append((cur_date, False))  # False means not working day
        schedule.sort(key=lambda x: x[0])

        equipment = Equipment.objects.all()
        context = {'schedule': schedule,
                   'equipment': equipment}
        return render(request, self.template_name, context)
