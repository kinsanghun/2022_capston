import xmltodict
import requests
import json
from main.models import company


class api:
    encode_key = "%2BUmLnRMVWcggyedUWUzsaAPbD4XUYB%2FgT29MHmtCB96qyz2MZiJnlELTQI%2BJVAssqThmm9H1LXQaQw9nkRlvfw%3D%3D"
    decode_key = "+UmLnRMVWcggyedUWUzsaAPbD4XUYB/gT29MHmtCB96qyz2MZiJnlELTQI+JVAssqThmm9H1LXQaQw9nkRlvfw=="
    api_url = "https://apis.data.go.kr/1480523/Dwqualityservice/getDrinkWaterORGWATR"

    def get_encode_key(self):
        return self.encode_key

    def get_decode_key(self):
        return self.decode_key

    def get_data(self, pageNo=1, numOfRows=10000000, types="json"):
        url = f"{self.api_url}?serviceKey={self.encode_key}&pageNo={pageNo}&numOfRows={numOfRows}&type={types}"
        response = requests.get(url, verify=False)
        rD = xmltodict.parse(response.text)
        rDJ = json.dumps(rD)
        rDD = json.loads(rDJ)

        datas = rDD["response"]["body"]["items"]["item"]

        for data in datas:
            q = company(year=data["year"],
                          ht=data["ht"],
                          mgc=data["mgc"],
                          entrpsNm=data["entrpsNm"],
                          chckDe=data["chckDe"],
                          chcklnstt=data["chckInstt"],
                          wtrsmpleDe=data["wtrsmpleDe"],
                          chckAt=data["chckAt"],
                          unchckPrvonsh=data["unchckPrvonsh"])
            q.save()
