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
    select_company = request.GET.get('entrpsNm', 'none')
    print(select_company)

    chckAt = request.GET.get("chckAt", 'Y')

    if request.method == "POST":
        if request.POST["entrpsNm"] == "none":
            datas = company.objects.filter(chckAt=request.POST["chckAt"]).values().order_by("-year")
            chckAt = request.POST["chckAt"]


        else:
            datas = company.objects.filter(entrpsNm=request.POST["entrpsNm"],
                                        chckAt=request.POST["chckAt"]).values().order_by("-year")
            select_company = request.POST["entrpsNm"]
            chckAt = request.POST["chckAt"]

    else:
        if select_company == "none":
            datas = company.objects.filter(chckAt=chckAt).values().order_by("-year")
        else:
            datas = company.objects.filter(entrpsNm=select_company, chckAt=chckAt).values().order_by("-year")

        chckAt = "Y"

    cname = company.objects.values("entrpsNm").distinct()
    paginator = Paginator(datas, 10)
    page_obj = paginator.get_page(page)

    context = {
        'datas' : page_obj,
        'cname' : cname,
        'entrpsNm' : select_company,
        'chckAt' : chckAt
    }
    return render(request, "company/company.html", context)

def contact(request):
    return render(request, "contact/contact.html")