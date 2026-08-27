servers = [
    {
        "name": "web01",
        "cpu": 45,
        "memory": 60, 
        "status": "Running"

    },

    {
        "name":  "web02",
        "cpu": 91,
        "memory": 85, 
        "status": "Not Running"
    },
    
    {
        "name": "db01",
        "cpu": 82,
        "memory": 55,
        "status": "Running"
    }
]

healthy_count = 0 
alert_count = 0

for server in servers:
    server_alert = False
    print (f"Checking server: {server['name']}")
    print (f"CPU usage: {server['cpu']}%")
    print (f"Memory usage: {server['memory']}%")
    print(f"Server status: {server['status']}")
    
    if server['cpu'] > 80:
        print("Alert: High CPU")
        server_alert = True 

    if server['memory'] > 80:
        print("Alert: High Memory")
        server_alert = True
    
    if server['status'] != "Running":
        print("Alert: Server is not running")
        server_alert = True

    if server_alert:
        alert_count = alert_count + 1
    else: 
        healthy_count =  healthy_count + 1
    
    print()
   # if server['cpu'] > 80 or server['memory'] > 80 or server['status'] != "Running":
   #     alert_count = alert_count + 1
   # else:
   #     healthy_count = healthy_count + 1


print(f"Healthy server count = {healthy_count}")
print(f"Alerting server count = {alert_count}")    


