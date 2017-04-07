from AppChains import AppChains
from AppChains import Result
from AppChains import ResultValue
from AppChains import FileResultValue
from AppChains import Report




chains = AppChains('c68bc5dbb7907b0be2d44a672788f685810b56a5', 'api.sequencing.com')
chains_result = chains.getReport('StartApp', 'Chain961', '80599')
if chains_result.isSucceeded():
    print('Request has succeeded')
    for result in chains_result.getResults():
        file_type = result.getValue().getType()
        v = result.getValue()
        if file_type == 'TEXT':
            import pdb; pdb.set_trace()
            print('-> text result type {} = {}'.format(
                r.getName(), v.getData()))
else:
    print('Request has failed')
