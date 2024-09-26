from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget3"],
        "greeting": "THAnk you FOR visitING",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context
    
#Assignment Add-Ons from this point

class ProductsPageView(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):           #just gonna shdow about page creation exactly
        context = super().get_context_data(**kwargs)
        #Context and added 4 products
        #So i guess products should be here
        context['products'] = [
            "guns",
            "cars",
            "money",
            "tigers"
        ]
        return context  #oh yeah gotta actually return the context
# Create your views here.
