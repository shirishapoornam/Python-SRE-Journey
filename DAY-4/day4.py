servers = ["prod-api-01", "prod-api-02", "prod-db-01"]

def check_server(server):
    print("checking health..", server)
    print("status : Healthy")
    print("-----------------")

for server in servers:
    check_server(server)

#def - define a function
#function() - calling a function
#parameter - value which is present inside a function
#return - return a values instead of saying it gives a value back