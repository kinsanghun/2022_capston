from django.shortcuts import render
from django.core.paginator import Paginator
from .models import company

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def reports(request):
    return render(request, "reports/reports.html")

def companylist(request):
    page = request.GET.get('page', '1')  # 페이지
    datas = company.objects.order_by("-year")

    paginator = Paginator(datas, 10)
    page_obj = paginator.get_page(page)

    context = {
        'datas' : page_obj
    }
    return render(request, "company/company.html", context)

def contact(request):
    return render(request, "contact/contact.html")