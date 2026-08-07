k8s_clusters = ["dev-cluster", "stg-cluster", "UAT-cluster", "preprod-cluster", "prod-cluster"]
for i in k8s_clusters:
    print(f"Checking cluster: {i}")


cpu_usage = [65,82,91,75,88]
for j in cpu_usage:
    if j > 80:
        print(f"high cpu : {j}")
    else:
        print(f"Normal cpu: {j}")

running_pods = ["nginx","redis","prometheus","grafana"]
for k in running_pods:
    print(f"Checking pods: {k}")

tools = ["Prometheus","Grafana","Splunk","CloudWatch"]
for l in tools:
    print(f"Monitoring tools: {l}")

cpu_alert = [95,65,72,99,83]
for m in cpu_alert:
    if m > 90:
        print("Critical Alert")
    else:
        print("all ok")

servers = ["web01","web02","web03","db01"]
for n in servers:
    print(f"Connecting to {n}")

deployment_status = ["Success","Success","Failed","Success"]
for status in deployment_status:
    if status == "Failed":
        print("Rollback Deployment")
    else:
        print("Deployment Successful")


services = ["Nginx","Redis","Kafka","Grafana"]
for service in services:
    print(f"Service {service} is running")

memory_usage = [45,78,91,65,99]
for o in memory_usage:
    if o > 80:
        print("Memory alert")
    else:
        print("Memory healthy")

