servername = "prod-api-01"
cpu = 92
memory = 90
print("=====================")
print("server health check")
print("======================")
print("Server Name :", servername)
print("CPU Usage :", cpu)
print("Memory :", memory)

if cpu <70 or memory < 70:
    print("Healthy")
elif 70 <= cpu <= 80 or 70 <= memory <= 80:
    print("Warning")
else:
    print("Critical")

if cpu >90 or memory >90:
    print("immediate investigation required")

#if cpu is less than 70 print healthy
#if cpu is less than or equal to 90 print warning
#otherwise print critical
#If CPU > 90 OR Memory > 90

