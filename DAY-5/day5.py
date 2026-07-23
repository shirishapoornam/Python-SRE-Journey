servers = [
{
    "name" : "prod-api-01",
    "cpu" : 45,
    "memory" : 60,
    "status" : "unknown"
},
{
  "name" : "prod-db-01",
    "cpu" : 95,
    "memory" : 82,
    "status" : "unknown"  
},
{
    "name" : "prod-cache-01",
    "cpu" : 75,
    "memory" : 72,
    "status" : "unknown"
}
]
Healthy_count  = 0
Warning_count  = 0
Critical_count = 0

for server in servers:
    if server["cpu"] > 90 or server["memory"] > 90:
        server["status"] = "Critical"
        Critical_count += 1
    elif server["cpu"] > 70 or server["memory"] > 70:
        server["status"] = "Warning"
        Warning_count += 1
    else:
        server["status"] = "Healthy"
        Healthy_count += 1
    print("------------------------")
    print("Server :", server["name"])
    print("Cpu    :", server["cpu"], "%")
    print("memory :", server["memory"], "%")
    print("Status :", server["status"])
print("---------------------------")
print("Healthy Servers  :", Healthy_count)
print("Warning Servers  :", Warning_count)
print("Critical servers :", Critical_count)







#Loop through each server
#If CPU > 90 OR Memory > 90 , update: server ["status"] ="critical"
#Else if CPU > 70 OR Memory > 70 , update: Status = "Warning"
#otherwise keep the status as "Healthy"