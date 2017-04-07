try:
    from dashboard.chains.UsageBase import ChainWrapper
    from dashboard.secrets import TOKEN
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
        return HttpResponse(json.dumps(_result(TOKEN, request.GET['fileid']), indent=2))


if __name__ == "__main__":
    x = _result('59aff2f9a6dcaa1d403666f62e68b862b880e88a', '227679')
    import pdb; pdb.set_trace()