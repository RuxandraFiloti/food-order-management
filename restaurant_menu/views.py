from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE

class MenuList(generic.ListView): #displays pages that are a list of items or blog links
    queryset = Item.objects.order_by("-date_created") #order by date created
    template_name = "index.html"  # Specify your template name here
    
    def get_context_data(self, **kwargs):
        #context = {} #context -> dictionary with keys and values
        context = super().get_context_data(**kwargs) 
        context['meals'] = MEAL_TYPE
        return context
    
class MenuDetail(generic.DetailView): #the page that displays the details of a single item -> opens the blog link
    model = Item
    template_name = "menu_item_detail.html"  # Specify your template name here