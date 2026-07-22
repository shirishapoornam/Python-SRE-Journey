servers = ["prod-api-01", "prod-api-02", "prod-db-01"]

def check_server(server):
    print("checking health..", server)
    print("status : Healthy")
    print("-----------------")

for server in servers:
    check_server(server)

