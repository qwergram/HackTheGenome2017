from AppChains import AppChains
from AppChains import Result
from AppChains import ResultValue
from AppChains import FileResultValue
from AppChains import Report




chains = AppChains('5de67613bf4e146517a3a63d21cfa9448d9ea65e', 'api.sequencing.com')
chains_result = chains.getReport('StartApp', 'Chain961', '<FILE ID HERE>')
if chains_result.isSucceeded():
    print('Request has succeeded')
else:
    print('Request has failed')
    for r in chains_result.getResults():
        file_type = r.getValue().getType()
        v = r.getValue()
        if file_type == 'TEXT':
            print('-> text result type {} = {}'.format(
                r.getName(), v.getData()))
