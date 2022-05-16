from django.shortcuts import render
from django.core.paginator import Paginator
from .models import company, allDB
from .apiclass import api
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def ilheiyoung():
    a = api()

    datas = a.get_data()

    for data in datas:
        db = allDB(
        year = data["year"],
        ht = data["ht"],
        mgc = data["mgc"],
        entrpsNm = data["entrpsNm"],
        wellNm = data["wellNm"],
        chckAt = data["chckAt"],
        unchckPrvonsh = data["unchckPrvonsh"],
        chckDe = data["chckDe"],
        chckInstt = data["chckInstt"],
        wtrsmpleDe = data["wtrsmpleDe"],
        pcbacValue = data["pcbacValue"],
        pcbacStbltAt = data["pcbacStbltAt"],
        msbacValue = data["msbacValue"],
        msbacStbltAt = data["msbacStbltAt"],
        tcoliValue = data["tcoliValue"],
        tcoliStbltAt = data["tcoliStbltAt"],
        fcstrValue = data["fcstrValue"],
        fcstrStbltAt = data["fcstrStbltAt"],
        psaerValue = data["psaerValue"],
        psaerStbltAt = data["psaerStbltAt"],
        smnlaValue = data["smnlaValue"],
        smnlaStbltAt = data["smnlaStbltAt"],
        shglaValue = data["shglaValue"],
        shglaStbltAt = data["shglaStbltAt"],
        sfsraValue = data["sfsraValue"],
        sfsraStbltAt = data["sfsraStbltAt"],
        pbValue = data["pbValue"],
        pbStbltAt = data["pbStbltAt"],
        flrnValue = data["flrnValue"],
        flrnStbltAt = data["flrnStbltAt"],
        asValue = data["asValue"],
        asStbltAt = data["asStbltAt"],
        slnumValue = data["slnumValue"],
        slnumStbltAt = data["slnumStbltAt"],
        mrcValue = data["mrcValue"],
        mrcStbltAt = data["mrcStbltAt"],
        cynValue = data["cynValue"],
        cynStbltAt = data["cynStbltAt"],
        crValue = data["crValue"],
        crStbltAt = data["crStbltAt"],
        nh4nValue = data["nh4nValue"],
        nh4nStbltAt = data["nh4nStbltAt"],
        no3nValue = data["no3nValue"],
        no3nStbltAt = data["no3nStbltAt"],
        cdmmValue = data["cdmmValue"],
        cdmmStbltAt = data["cdmmStbltAt"],
        boronValue = data["boronValue"],
        boronStbltAt = data["boronStbltAt"],
        phnlValue = data["phnlValue"],
        phnlStbltAt = data["phnlStbltAt"],
        diaznValue = data["diaznValue"],
        diaznStbltAt = data["diaznStbltAt"],
        prtoValue = data["prtoValue"],
        prtoStbltAt = data["prtoStbltAt"],
        fntrtoValue = data["fntrtoValue"],
        fntrtoStbltAt = data["fntrtoStbltAt"],
        cbrylValue = data["cbrylValue"],
        cbrylStbltAt = data["cbrylStbltAt"],
        trch111Value = data["trch111Value"],
        trch111StbltAt = data["trch111StbltAt"],
        ttcelValue = data["ttcelValue"],
        ttcelStbltAt = data["ttcelStbltAt"],
        tceValue = data["tceValue"],
        tceStbltAt = data["tceStbltAt"],
        dcmValue = data["dcmValue"],
        dcmStbltAt = data["dcmStbltAt"],
        c6h6Value = data["c6h6Value"],
        c6h6StbltAt = data["c6h6StbltAt"],
        tlnValue = data["tlnValue"],
        tlnStbltAt = data["tlnStbltAt"],
        chchValue = data["chchValue"],
        chchStbltAt = data["chchStbltAt"],
        zylnValue = data["zylnValue"],
        zylnStbltAt = data["zylnStbltAt"],
        dch11Value = data["dch11Value"],
        dch11StbltAt = data["dch11StbltAt"],
        cbttcValue = data["cbttcValue"],
        cbttcStbltAt = data["cbttcStbltAt"],
        db12ch3Value = data["db12ch3Value"],
        db12ch3StbltAt = data["db12ch3StbltAt"],
        diox14Value = data["diox14Value"],
        diox14StbltAt = data["diox14StbltAt"],
        ppconValue = data["ppconValue"],
        ppconStbltAt = data["ppconStbltAt"],
        smellValue = data["smellValue"],
        smellStbltAt = data["smellStbltAt"],
        copprValue = data["copprValue"],
        copprStbltAt = data["copprStbltAt"],
        chmaValue = data["chmaValue"],
        chmaStbltAt = data["chmaStbltAt"],
        anosurValue = data["anosurValue"],
        anosurStbltAt = data["anosurStbltAt"],
        phValue = data["phValue"],
        phStbltAt = data["phStbltAt"],
        zincValue = data["zincValue"],
        zincStbltAt = data["zincStbltAt"],
        chloionValue = data["chloionValue"],
        chloionStbltAt = data["chloionStbltAt"],
        turValue = data["turValue"],
        turStbltAt = data["turStbltAt"],
        slftionValue = data["slftionValue"],
        slftionStbltAt = data["slftionStbltAt"],
        almnmValue = data["almnmValue"],
        almnmStbltAt = data["almnmStbltAt"]
        )
        db.save()

def reports(request):

    datas = allDB.objects.filter(
        Q(pcbacStbltAt='N')|
        Q(msbacStbltAt='N')|
        Q(tcoliStbltAt='N')|
        Q(fcstrStbltAt='N')|
        Q(psaerStbltAt='N')|
        Q(smnlaStbltAt='N')|
        Q(shglaStbltAt='N')|
        Q(sfsraStbltAt='N')|
        Q(pbStbltAt='N')|
        Q(flrnStbltAt='N')|
        Q(asStbltAt='N')|
        Q(slnumStbltAt='N')|
        Q(mrcStbltAt='N')|
        Q(cynStbltAt='N')|
        Q(crStbltAt='N')|
        Q(nh4nStbltAt='N')|
        Q(no3nStbltAt='N')|
        Q(cdmmStbltAt='N')|
        Q(boronStbltAt='N')|
        Q(phnlStbltAt='N')|
        Q(diaznStbltAt='N')|
        Q(prtoStbltAt='N')|
        Q(fntrtoStbltAt='N')|
        Q(cbrylStbltAt='N')|
        Q(trch111StbltAt='N')|
        Q(ttcelStbltAt='N')|
        Q(tceStbltAt='N')|
        Q(dcmStbltAt='N')|
        Q(c6h6StbltAt='N')|
        Q(tlnStbltAt='N')|
        Q(chchStbltAt='N')|
        Q(zylnStbltAt='N')|
        Q(dch11StbltAt='N')|
        Q(cbttcStbltAt='N')|
        Q(db12ch3StbltAt='N')|
        Q(diox14StbltAt='N')|
        Q(ppconStbltAt='N')|
        Q(smellStbltAt='N')|
        Q(copprStbltAt='N')|
        Q(chmaStbltAt='N')|
        Q(anosurStbltAt='N')|
        Q(phStbltAt='N')|
        Q(zincStbltAt='N')|
        Q(chloionStbltAt='N')|
        Q(turStbltAt='N')|
        Q(slftionStbltAt='N')|
        Q(almnmStbltAt='N')).order_by("-year", "-ht")

    context = {
        'datas': datas,
    }
    return render(request, "reports/reports.html", context)

def companylist(request):
    companys = company.objects.all()
    context = {
        'companys': companys,
    }
    return render(request, "company/company.html", context)

def contact(request):
    return render(request, "contact/contact.html")