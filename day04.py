pod_status = "pending"
print(f"Current pod status: {pod_status}")

pod_status = "Running"
print(f"Current pod status: {pod_status}")

pod_status = "Succeeded"
print(f"Current pod status: {pod_status}")

cluster = "eks-prod"

nodes = 3

print(f"The name of my k8s cluster is : {cluster}")
print(f"There are {nodes} nodes in my cluster")

nodes = 5

print(f"2 new nodes got added to my {cluster} and I have {nodes} in my cluster now")

