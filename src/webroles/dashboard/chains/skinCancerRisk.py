try:
    from dashboard.chains.UsageBase import ChainWrapper
    from dashboard.secrets import *
except ImportError:
    from UsageBase import ChainWrapper
    TOKEN = None
from django.views import View
from django.http import HttpResponse

import json

def _result(token, fileId):
    payload = ChainWrapper(token, 'Chain9', fileId).get_report()
    return_val = {}
    for item in payload:
        return_val[item.getName()] = item.getValue().getData()
    return return_val


class SkinCancerRiskView(View):
    
    def get(self, request):
        response = json.dumps(_result(TOKEN, request.GET['fileid']), indent=2)
        qualitative = json.loads(response.lower())['riskdescription']
        if 'low' in qualitative:     
            return HttpResponse('{"value": 1}')
        if 'normal' in qualitative:
            return HttpResponse('{"value": 2}')
        if 'increased' in qualitative:
            return HttpResponse('{"value": 2.5}')
        if 'moderate' in qualitative:
            return HttpResponse('{"value": 5}')
        if 'very hi' in qualitative:
            return HttpResponse('{"value": 20}')
        if 'hi' in qualitative:
            return HttpResponse('{"value": 15}')


if __name__ == "__main__":
    x = _result('2af4f10acac15b8acf577360d5825616898bcd72', '227679')
    import pdb; pdb.set_trace()