from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "Thank you for visiting!", 
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context
            
class ProductsPageView(TemplateView):
    template_name = "products.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = [
            {"name": "Football", "price": "$15.99"},
            {"name": "NBA Jersey", "price": "$220.00"},
            {"name": "Baseball Cards", "price": "$7.99"},
            {"name": "Hockey Stick", "price": "$359.99"},
        ]
        return context