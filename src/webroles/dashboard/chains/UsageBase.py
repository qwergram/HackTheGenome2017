try:
    from dashboard.chains.AppChains import AppChains
    from dashboard.chains.AppChains import Result
    from dashboard.chains.AppChains import ResultValue
    from dashboard.chains.AppChains import FileResultValue
    from dashboard.chains.AppChains import Report
except ImportError:
    from AppChains import AppChains
    from AppChains import Result
    from AppChains import ResultValue
    from AppChains import FileResultValue
    from AppChains import Report

class UsageExample(object):
    token = '2031d2c60358fc08c1a12bece9f89586c59ea935'
    url = 'api.sequencing.com'
    bot = 'StartApp'
    chain = 'Chain9'
    fileId = '227679'

    def __init__(self):
        self.chains = AppChains(self.token, self.url)
        #print(self.get_public_beacon_test())
        #print(self.get_raw_report_test())
        self.get_report()
        #self.get_report_batch_test()


    def get_public_beacon_test(self):
        beacon_result = self.chains.getPublicBeacon(1, 2, 'A')
        return beacon_result

    def get_raw_report_test(self):
        chains_raw_result = self.chains.getRawReport(
            self.bot, self.chain, self.fileId)
        return chains_raw_result

    def get_report(self):
        chains_result = self.chains.getReport(
            self.bot, self.chain, self.fileId)
        if chains_result.isSucceeded():
            print('Request has succeeded')
        else:
            print('Request has failed')
        return chains_result.getResults()

    def get_report_batch_test(self):
        chains_results = self.chains.getReportBatch(
            'StartAppBatch', {'Chain85': '227680', 'Chain88': '227680'})
        for chains_result in chains_results:
            if chains_results[chains_result].isSucceeded():
                print('Request has succeeded')
            else:
                print('Request has failed')
            for r in chains_results[chains_result].getResults():
                file_type = r.getValue().getType()
                v = r.getValue()
                if file_type == 'TEXT':
                    print('-> text result type {} = {}'.format(
                        r.getName(), v.getData()))
                elif file_type == 'FILE':
                    print(' -> file result type {} = {}'.format(
                        r.getName(), v.getUrl()
                    ))
                    v.saveTo('/tmp')

class ChainWrapper(object):
    
    def __init__(self, token, chain, fileid):
        self.token = token
        self.chain = chain
        self.fileid = fileid
        self.eg = UsageExample()
        self.eg.token = token
        self.eg.chain = chain
        self.eg.fileId = fileid

    def get_report(self):
        return self.eg.get_report()


    
