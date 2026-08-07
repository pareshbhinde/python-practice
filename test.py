servers = ["web01", "web02", "web03", "db01", "cache01"]

cpu_usage = [45, 92, 67, 97, 58]

healthy = 0
alert = 0

print("===== Server Health Report =====")

for i in range(len(servers)):
    print(f"Checking {servers[i]} server")
    print(f"CPU Usage : {cpu_usage[i]}%")
    if cpu_usage[i] > 80:
        print("Status : High CPU alert")
        alert = alert+1
        print()
    else:
        print("Status : Healthy")
        healthy = healthy+1
        print()

print("------------------------------")
print(f"Healthy Servers: {healthy}")
print(f"Servers with alert: {alert}")
        
