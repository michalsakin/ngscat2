import plotly.graph_objs as go
import plotly
import numpy as np
class Report():
    def __init__(self, mainreporter):
        mainreporter.addsection('onoff', self)
        self.mainreporter = mainreporter
        self.summary = {}
        self.plot_dir_duplicates = []
    def report(self, read_on_results):
        self.on_target_plot(read_on_results)
        self.duplicates_plot(read_on_results)

        for i, bam in enumerate(read_on_results['results']):
            self.summary['percontotal'].append(bam['percontotal'])
            self.summary['enrichment'].append(bam['enrichment'])
            self.summary['onoffstatus'].append(bam['onoff_status'])
            self.summary['duplicates_status'].append(bam['duplicates_status'])
            self.summary['perconduplicates'].append(bam['perconduplicates'])
            self.summary['percoffduplicates'].append(bam['percoffduplicates'])
            self.summary['warnthreshold'] = bam['percontotal']
        self.summary['maxduplicates'] = read_on_results['maxduplicates']

    def summary(self, read_on_results, key):
        return read_on_results[key]
    def on_target_plot(self, read_on_results):
        """*****************************************************************************************************************
            Task:ALEGARSAN this method is dependant on bam."reads_on_target".
                Generates a graph interactive plot
            Inputs:
                read_on_results: Dict, with same data as json generated.
                Data used results_on_target['results'] = list of dictionaries with reads data of each

                bamlist: list of bam_file objects.
                nread: list of integers, each containing the number of on-target reads in the corresponding bam file.
                tread: list of integers, each containing the total number of reads in the corresponding bam file.
                onperchr: list of dictionaries. There must be one dictionary for each bam file in bamlist.
                    Each dictionary contains data about the number of on-target
                    reads per chromosome. Keys of the dictionary are contig ids (e.g. 'chr1').
                    Elements are the number of on-target reads mapped in that contig.
                totalperchr: list of dictionaries. There must be one dictionary for each bam file in bamlist.
                    Each dictionary contains data about the total number of
                    reads mapped in each chromosome. Keys of the dictionary are contig ids (e.g. 'chr1').
                    Elements are the total number of reads mapped in that contig.
                enrichment: list or multiprocessing.
                    Array object containing the enrichment value for each bam (on-target reads per Kb)/(off target reads per Kb)
                percontarget: list or multiprocessing.
                    Array object containing the percentaje of reads on target for each bam file
                outdir: string containing the full path to the directory were result files will be saved.
                legend: list of strings containing the label to tag each bam file in the xls and png files that will be created.
            Outputs: a new bar plot will be created named outdir/reads_on_target.png.
                    This is a bar plot which indicates for each bam, the percentaje of on-target
                    reads in each chromosome. In addition, a new outdir/reads_on_target.html

            ************************************************************************************************************"""
        colors = ['rgb(0,102,0)', 'rgb(255,0,0)', 'rgb(102,178,255)', 'rgb(178,102,255)']
        data = []
        layout_comp = []
        for i, bam in enumerate(read_on_results['results']):
            trace = go.Bar(
                x=list(bam['perconperchr'].keys()),
                y=list(bam['perconperchr'].values()),
                hoverinfo='text',
                hoverlabel=dict(font=dict(color=['black'])),
                text=['Percentage:' + str(value) + '%' for value in list(bam['perconperchr'].values())],
                # mode='lines',
                name=bam['legend'],
                marker=dict(color=colors[i]))

            data.append(trace)

            layout_comp = go.Layout(
                title='Reads on target',
                hovermode='closest',
                barmode='group',
                xaxis=dict(showticklabels=True, showgrid=True, title='Chromosome/Contig'),
                yaxis=dict(title='% on-target reads'),
                shapes =[{
                    'type': 'line',
                    'x0': -0.5,
                    'y0': bam['percontotal'],
                    'x1': len(bam['perconperchr'])-0.5,
                    'y1': bam['percontotal'],
                    'line': {
                        'color': 'rgb(50, 171, 96)',
                        'width': 4,
                        'dash': 'dot'}}])

        fig = go.Figure(data=data, layout=layout_comp)
        plotly.offline.plot(fig, filename=self.mainreporter.outdir + '/data/reads_on_target.html',
                            auto_open=True, config=dict(displaylogo=False, modeBarButtonsToRemove=['sendDataToCloud']))

    def duplicates_plot(self, read_on_results):

        for i, bam in enumerate(read_on_results['results']):
            # Extract dictionary values
            # x = []
            # yon= []
            # yoff= []

            onkeys = list(bam['perconduplicates'].keys())

            offkeys = list(bam['percoffduplicates'].keys())
            onvalues = list(bam['perconduplicates'].values())
            offvalues = list(bam['percoffduplicates'].values())
            maxduplicates = read_on_results['maxduplicates']

            # Select the maximum number of times duplicates to show
            if maxduplicates > len(onkeys) and len(offkeys):
                maxduplicates = max(len(onkeys), len(offkeys))

            x = onkeys[0:maxduplicates - 1]
            x += ['>=' + str(len(x) + 1) + 'X']
            yon = onvalues[0:maxduplicates - 1]
            yon.append(sum(onvalues[maxduplicates - 1:]))
            yoff = offvalues[0:maxduplicates - 1]
            yoff.append(sum(offvalues[maxduplicates - 1:]))

            data = []
            traceon = go.Bar(
                x=x,
                y=yon,
                hoverinfo='text',
                hoverlabel=dict(font=dict(color=['black'] * len(x))),
                text=['Percentage on: ' + str(value) + '%' for value in yon],
                # mode='lines',
                name='on target duplicates')
            # marker=dict(color=colors[i]))
            data.append(traceon)

            traceoff = go.Bar(
                x=x,
                y=yoff,
                hoverinfo='text',
                hoverlabel=dict(font=dict(color=['black'])),
                text=['Percentage off: ' + str(value) + '%' for value in yoff],
                name='off target duplicates')
            # marker=dict(color=colors[i]))
            data.append(traceoff)

            layout_comp = go.Layout(
                title='Duplicates',
                hovermode='closest',
                barmode='group',
                xaxis=dict(showticklabels=True, showgrid=True, title='# of duplicates'),
                yaxis=dict(title='% of reads'))

            fig = go.Figure(data=data, layout=layout_comp)
            plotly.offline.plot(fig, filename= self.mainreporter.outdir + '/data/duplicates_' + bam['legend'] + '.html',
                                auto_open=True,
                                config=dict(displaylogo=False, modeBarButtonsToRemove=['sendDataToCloud']))

            self.plot_dir_duplicates.append(self.mainreporter.outdir + '/data/duplicates_' + bam['legend'] + '.html')