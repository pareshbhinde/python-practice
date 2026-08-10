filename = "application.log"

def count_errors(filename):
    error_count=0
    file = open(filename,"r")
    for line in file:
        if "ERROR" in line:
            error_count = error_count + 1
    file.close()
    return error_count

def count_warnings(filename):
    warn_count=0
    file = open(filename,"r")
    for line in file:
        if "WARNING" in line:
            warn_count = warn_count + 1
    file.close()
    return warn_count

def count_info(filename):
    info_count=0
    file = open(filename,"r")
    for line in file:
        if "INFO" in line:
            info_count = info_count + 1
    file.close()
    return info_count

def print_report(errors, warnings, info):
    print(f"Number of errors: {errors}")
    print(f"Number of Warnings: {warnings}")
    print(f"Number of Info:{info}")    



errors = count_errors(filename)
warnings = count_warnings(filename)
info = count_info(filename)

print_report(errors,warnings,info)
