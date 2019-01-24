# apiautomation_keyword_driven

Coding Challenge: Open Weather API test automation challenge


Goal Description:
Challenge is to automate a process to get current weather using OpenWeatherAPI. The
API returns the current weather of any given place. The place can be provided in different ways
like “city name” , “Zipcode”, “Coordinates” and “CityID”

Tools / Frameworks used :
Language: Python
IDE: PyCharm community edition
Packages: os, json, requests, xlrd, openpyxl, collections, time and yaml

 This is a Data Driven framework which tests API’s to get weather data for different combinations of data.
Following is the rough flow of how framework works:
1. The Framework contains 3 main directories as following:
APITests_Adidas: Python source files
Resources : Contain Config.yaml, which contains the configuration data for test execution like: TestCasesPath, TestCases and OutputPath
Outputs : Stores the output folders of each run
2. Based upon the values you enter in the config file, the framework takes all the test cases from TestCasesInputFile.xlsx from “InputFiles” Directory. Each row in the TestCaseInputFile.xlsx serves as a test case
3. The framework will construct the api request uri with the supplied input apikey / appid
and will hit the api to get Weather data
4. The Framework stores the api response data for each entry in the input file and creates
the output file for that particular test case, with the test case ID
5. Once the framework reads all the input test cases and hits the api for all available
locations from the input file, it’ll create a output xlsx file containing all the Test cases the
framework executed and stamps its status
6. Also, the framework will print the temperature data and test execution status to the
Console

