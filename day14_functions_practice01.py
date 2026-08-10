servers = ["web01","web02","db01","cache01"]
cpu = [82,91,78,88]
memory = [85,70,92,55]



def check_cpu(server,cpu,memory):
    cpu_alert = 0
    mem_alert = 0
    unhealthy_servers = 0
    healthy_servers = 0

    print("================== SERVER HEALTH REPORT ===================")
    print()
    
    for i in range(len(server)):
        
        print(f"Checking {server[i]}")
        print(f"CPU Usage: {cpu[i]}%")
        if cpu[i] > 80:
            print("CPU_Status :  Unhealthy")
        else:
            print("CPU State : Healthy")
        
        print(f"Memory Usage: {memory[i]}%")
        if memory[i] > 80:
            print("Memory status : Memory alert")
        else:
            print("Memory status: Healthy")
        
        if cpu[i] > 80 and  memory[i] > 80:
            #print(f"{server[i]}: CPU and Memory alert")
            cpu_alert = cpu_alert + 1
            mem_alert = mem_alert + 1
            unhealthy_servers = unhealthy_servers + 1
            print()

        elif cpu[i] > 80 and memory[i] <= 80:
            #print(f"{server[i]}: CPU unhealthy")
            cpu_alert = cpu_alert + 1
            unhealthy_servers = unhealthy_servers + 1
            print()

        elif cpu[i] <=80 and memory[i] > 80:
            #print(f"{server[i]}: Memory Unealthy")
            mem_alert = mem_alert + 1
            unhealthy_servers = unhealthy_servers + 1
            print()
        
        else:
            #print(f"{server[i]} : Overall healthy")
            healthy_servers = healthy_servers + 1
        print()
    print(f"total number of cpu and Memory alerts : {cpu_alert} , {mem_alert}")
    print(f"Total unhealthy servers: {unhealthy_servers}")
    print(f"Total Healthy Servers: {healthy_servers}")

check_cpu(servers,cpu,memory)

