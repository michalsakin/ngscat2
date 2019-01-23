import json

class Report():
    def __init__(self, outdir):
        self.outdir = outdir

    def report(self, coveragefiles, target_distribution_result):

        with open(self.outdir + '/data/coveragesummary.json', 'w') as outfile:
            json.dump(target_distribution_result, outfile)

