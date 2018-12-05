# import json
#
# with open('/home/agarcia/Documents/prueba.json', 'r') as f:
#     prueba_dict = json.load(f)
#
# [print(i) for i in prueba_dict['results']['whole_genome']['chrs'][0].values()]
#
from timeit import timeit

from report import percentage_target
import multiprocessing
import coverage_file
import time
from metric import target_coverage
import bam_file
import coverage_file
from metric import region_coverage
from report import target_coverage_report
def main():

    # Test code for percentage target(duplicates no duplicates)
    # bam1 = bam_file.bam_file('/home/agarcia/PycharmProjects/ngscat/example1.bam')
    # print(bam1.filename.decode('utf-8'))
    #
    # #bam1.sort_bam()
    # #bam1.mapped()
    # #bam1.issorted()
    # #bam1.filename.decode('utf-8')

    ###==================================================
    ## Class generation and mycoberage test
    start = time.time()
    print(start)
    # bam = bam_file.bam_file('/home/agarcia/PycharmProjects/ngscat/hg00096.bam')
    #bam = bam_file.bam_file('/home/agarcia/PycharmProjects/ngscat/1_T_25309.sorted.dedup.filtered.bam')
    bam1 = bam_file.bam_file('/home/agarcia/PycharmProjects/ngscat/sort_example1.bam')
    bam = bam_file.bam_file('/home/agarcia/PycharmProjects/ngscat/example2.bam')
    #
    # cover, x = bam.myCoverageBed('/home/agarcia/PycharmProjects/ngscat/exome.targets.g1k.bed')
    #cover, x = bam.myCoverageBed('/home/agarcia/PycharmProjects/ngscat/talidomida_v2_primary_targets.bed')
    cover, y = bam.myCoverageBed('/home/agarcia/PycharmProjects/ngscat/seqcap.example2.bed')
    cover2, y = bam1.myCoverageBed('/home/agarcia/PycharmProjects/ngscat/seqcap.example2.bed')
    end = time.time()

    print(end - start)
    #result, covlist = target_coverage.target_distribution([bam], [cover], "/home/agarcia/PycharmProjects/ngscat3/", bins = 100)
    #z = target_coverage_report.coverage_per_chr([cover,cover2], 20 ,'/home/agarcia/PycharmProjects/ngscat/')
    #region_coverage.zeroCoverageRegions(cover, '/home/agarcia/PycharmProjects/ngscat/')
    region_coverage.region_std_distribution([cover],'/home/agarcia/PycharmProjects/ngscat/')
    # target_coverage_report.target_distribution_histplot(result)
    # target_coverage_report.target_distribution_boxplot(result, covlist)

    # cov = target_coverage.target_distribution([bam], [cover], "/home/agarcia/PycharmProjects/ngscat3/",bins = 5)



    # bam = bam_file.bam_file('/home/agarcia/Downloads/hg00096.bam')
    # inter = bam.myCoverageBed('/home/agarcia/Downloads/exome.targets.g1k.bed',writeToFile='/home/agarcia/PycharmProjects/ngscat3/prueba_exome')

    # #bam.myCoverageBed('/home/agarcia/PycharmProjects/ngscat/seqcap.example2.bed',writeToFile='/home/agarcia/PycharmProjects/ngscat3/coveragefile')




    # print(bam.mapped)

    ###=================================================
    # Targets on read and derivate results test

    # #jsonfile,__,__ = bam.reads_on_target('/home/agarcia/PycharmProjects/ngscat/seqcap.example2.bed','/home/agarcia/PycharmProjects/ngscat3/',[bam_file.bam_file('/home/agarcia/PycharmProjects/ngscat/example2.bam')])
    # jsonfile,__,__ = bam.reads_on_target('/home/agarcia/PycharmProjects/ngscat/seqcap.example2.bed','/home/agarcia/PycharmProjects/ngscat3/', maxduplicates=7)
    # print(jsonfile.keys())
    # percentage_target.on_target_plot(jsonfile)
    # percentage_target.on_target_xls(jsonfile)
    # percentage_target.duplicates_plot(jsonfile)
    # percentage_target.duplicates_xls(jsonfile)

    import pysam
    ###=================================================

    # start = time.time()
    # #Test code for coverage class
    # print(start)
    # cover = coverage_file.coverage_file("/home/agarcia/PycharmProjects/ngscat3/coveragefile")
    # #cover = coverage_file.coverage_file("/home/agarcia/PycharmProjects/ngscat/coverage_exome.txt")
    end = time.time()
    print(end-start)


    # coveragefiles = [cover]
    # # z = cover.getInit()
    # print(end - start)
    # #print(cover.data[2:4,:])
    # #print(cover.getCov())
    #
    # target_coverage_result = target_coverage.target_coverage([bam],coveragefiles, [1,10,20,30,40],"/home/agarcia/PycharmProjects/ngscat3/")
    # target_coverage_report.target_coverage_plot(target_coverage_result)
    # target_coverage_report.target_coverage_xls(target_coverage_result)
    # cov = cover.getCov()
    # target_distribution_result,covnozero = target_coverage.target_distribution([bam], coveragefiles, "/home/agarcia/PycharmProjects/ngscat3/",bins = 5)
    # target_coverage_report.target_distribution_histplot(target_distribution_result)
    # target_coverage_report.target_distribution_xls(target_distribution_result)
    # target_coverage_report.target_distribution_boxplot(target_distribution_result,covnozero)



    print ("a")


if __name__=='__main__':
    main()
