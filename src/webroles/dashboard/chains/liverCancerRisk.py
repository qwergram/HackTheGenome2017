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
    payload = ChainWrapper(token, 'Chain961', fileId).get_report()
    return_val = {}
    for item in payload:
        return_val[item.getName()] = item.getValue().getData()
    return return_val

class LiverCancerRiskView(View):
    
    def get(self, request):
        return HttpResponse(json.dumps(_result(TOKEN, request.GET['fileid'])))

        response = json.dumps(_result(TOKEN, request.GET['fileid']), indent=2)
        qualitative = json.loads(response.lower())['riskdescription']
        return HttpResponse(response.lower())
    
        
        if 'carrier' in qualitative:     
            return HttpResponse('{"value": 1}')
        if 'possible' in qualitative:
            return HttpResponse('{"value": 2}')
        if 'not detect' in qualitative:
            return HttpResponse('{"value": 2.5}')
        return HttpResponse('{"value": 0}')