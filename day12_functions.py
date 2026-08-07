def greet():
    print("Hello Paresh!")

greet()

def welcome():
    print("Welcome to Python Automation")
welcome()


#-------------------------------------------


servers = ["web01", "web02", "db01", "cache01"]
cpu_usage = [45, 91, 62, 95]


def check_server(server,cpu):
    print(f"checking {server}")
    print(f"CPU usage for {server} : {cpu}%")
    print()

for i in range(len(servers)):
    check_server(servers[i],cpu_usage[i])

print("-------------------------------------------")

services = ["nginx", "redis", "docker"]
status = ["Running", "Stopped", "Running"]

def check_service(service,status):
    print(f"Service : {service}")
    print(f"Status : {status}")
    if status == "Running":
        print ("Health : Healthy")
    else:
        print ("Health : Unhealthy")
    print()

for i in range(len(services)):
    check_service(services[i],status[i])


print("------------------------------------------------")

pods = ["nginx" , "redis" , "grafana"]
namespace = ["Default", "prod" , "monitoring"]

def show_pod(pod,namespace):
    print (f"Pod: {pod}")
    print (f"Namespace : {namespace}")
    print()

for i in range(len(pods)):
    show_pod(pods[i],namespace[i])










