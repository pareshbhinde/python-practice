filename = "application.log"


def count_errors(filename):
    err_count = 0
    file = open(filename, "r")

    for line in file:
        if "ERROR" in line:
            err_count = err_count + 1

    file.close()
    return err_count


def count_warnings(filename):
    warn_count = 0
    file = open(filename, "r")

    for line in file:
        if "WARNING" in line:
            warn_count = warn_count + 1

    file.close()
    return warn_count


def count_info(filename):
    info_count = 0
    file = open(filename, "r")

    for line in file:
        if "INFO" in line:
            info_count = info_count + 1

    file.close()
    return info_count


def print_report(errors, warnings, info):
    print("\n========== LOG ANALYSIS REPORT ==========")
    print(f"Total ERROR Logs   : {errors}")
    print(f"Total WARNING Logs : {warnings}")
    print(f"Total INFO Logs    : {info}")

    if errors > 5:
        print("\nApplication Status : CRITICAL")
    else:
        print("\nApplication Status : HEALTHY")

    print("=========================================")


# Main Program

errors = count_errors(filename)
warnings = count_warnings(filename)
info = count_info(filename)

print_report(errors, warnings, info)
