from django.shortcuts import render
from django.db.models import Sum, Count
from . import models
from .models import Stats
from django.views.generic import ListView,TemplateView,CreateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

"""
class StatsListView(ListView):
    template_name = 'mobile/stats_list.html'
    context_object_name = 'list'
    model = models.Stats

    def get_queryset(self):

        first_five = Stats.objects.all().order_by('current_rent')[:5]

        return first_five
"""

def stats_list(request):
    stats = Stats.objects.all()
    order = request.GET.get('order', 'current_rent')  # Set 'current_rent' as a default value
    stats = stats.order_by(order)
    total_rent = Stats.objects.all().aggregate(total=Sum('current_rent'))

    #num_masts = Stats.objects.filter(tenant_name='O2 (UK) Ltd').count()

    #print("it works look > ",num_masts)

    fieldname = 'tenant_name'
    num_masts = Stats.objects.values(fieldname).annotate(the_count=Count(fieldname))

    print("it works look > ", num_masts)

    return render(request, 'mobile/stats_list.html', {
        'stats': stats[:5],
        'total_rent': total_rent['total']
    })

def create_dict(request):
    stats = Stats.objects.all()


class CreateStatView(CreateView):
    model = models.Stats
    fields = ['property_name', 'property_address1', 'property_address2', 'property_address3',
              'property_address4','unit_name', 'tenant_name', 'lease_start',
              'lease_end', 'lease_years', 'current_rent']

    redirect_field_name = 'mobile/stats_list.html'