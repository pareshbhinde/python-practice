err_count = 0
warn_count = 0
info_count = 0

file = open("application.log","r")

for line in file:
    if "ERROR" in line:
        err_count = err_count + 1
    elif "WARNING" in line:
        warn_count = warn_count + 1
    else:
        info_count = info_count + 1

print(f"Number of errors --> {err_count}")
print(f"Number of Warning--> {warn_count}")
print(f"Number of Info--> {info_count}")

if err_count > 5:
    print("Critical application health")
else:
    print("Application is health")

file.close()
