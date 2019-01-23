import os
import yaml


def config_builder():
    tests_to_run = list()
    current_directory = os.path.dirname(os.getcwd())
    with open(current_directory + "\Resources\config.yaml") as config:
        config_file = yaml.safe_load(config)
        test_cases_file = config_file["TestCasesPath"]
        test_cases = config_file["TestCases"]
        tests_output_file = config_file["OutputPath"]
        if type(test_cases) is int:
            tests_to_run.append(1)
        elif "-" in test_cases:
            first = int(test_cases.split("-")[0])
            last = int(test_cases.split("-")[1])
            for i in range(first, last+1):
                tests_to_run.append(i)

        elif "," in test_cases:
            tests_to_run = test_cases.split(",")

        else:
            tests_to_run.append(test_cases)
    return test_cases_file, tests_to_run, tests_output_file


print(config_builder())
