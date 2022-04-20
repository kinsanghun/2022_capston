from django.db import models

class company(models.Model):
    year = models.CharField(max_length=30 ,null=True, blank=True)
    ht = models.CharField(max_length=30 ,null=True, blank=True)
    mgc = models.CharField(max_length=30 ,null=True, blank=True)
    entrpsNm = models.CharField(max_length=30 ,null=True, blank=True)
    chckDe = models.CharField(max_length=30 ,null=True, blank=True)
    chcklnstt = models.CharField(max_length=30 ,null=True, blank=True)
    wtrsmpleDe = models.CharField(max_length=30 ,null=True, blank=True)
    chckAt = models.CharField(max_length=30 ,null=True, blank=True)
    unchckPrvonsh = models.TextField(null=True, blank=True)
