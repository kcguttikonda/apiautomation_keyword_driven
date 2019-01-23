import collections
import xlrd
import os

from APITests_Adidas.ConfigBuilder import config_builder


def testdatabuilder():
    testcases_dictionary = collections.OrderedDict()
    TestCasesFile, TestCasesToRun, TestCasesOutputFile = config_builder()
    testcasesworkbook = xlrd.open_workbook(os.path.dirname(os.getcwd()) + "\\" + TestCasesFile)
    testcasessheet = testcasesworkbook.sheet_by_name("Sheet1")
    for row in range(1, testcasessheet.nrows):
        if testcasessheet.cell_value(row,0) != '' and (testcasessheet.cell_value(row,0)) in TestCasesToRun:
            testcases_dictionary[int(row)] = [testcasessheet.cell_value(row,0),
                                              testcasessheet.cell_value(row,1),
                                              testcasessheet.cell_value(row,2),
                                              testcasessheet.cell_value(row,3),
                                              testcasessheet.cell_value(row,4),
                                              testcasessheet.cell_value(row,5),
                                              testcasessheet.cell_value(row,6)]

    return testcases_dictionary