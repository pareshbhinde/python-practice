pods = ["nginx","redis", "Grafana","Prometheus","Jenkins"]
status = ["Running","CrashLoopBackOff","Running","Pending","Running"]

print("-------Kubernetes Pod Health Report---------")

healthy = 0
unhealthy = 0

for i in range(len(pods)):
    print(f"Checking pods: {pods[i]}")
    print(f"status : {status[i]}")
    if status[i] == "Running":
        print("Health: Healthy")
        healthy=healthy+1
    else: 
        print("Health : Unhealthy")
        unhealthy=unhealthy+1

    print()

print("---------------------------------------------")
print(f"Healthy pods: {healthy}")
print(f"Unhealthy pods: {unhealthy}")
        

