read_file = open("DAY-6/servers.txt", "r")
write_file = open("DAY-6/server_report.txt", "w")

for line in read_file:
    line = line.strip()
    if line == "":
        continue

    print(repr(line))

    parts = line.split(",")
    print(parts)

    name = parts[0]
    cpu = int(parts[1])
    memory = int(parts[2])
    print(line)
    if cpu > 90 or memory > 90:
        status = "Critical"
    elif cpu > 70 or memory > 70:
        status = "Warning"
    else:
        status = "Healthy"
    print(name, cpu, memory, status)
    write_file.write("server :" + name +"\n")
    write_file.write("cpu :" + str(cpu) + "\n")
    write_file.write("memory :" + str(memory) + "\n")
    write_file.write("status :" + status + "\n")
    write_file.write("---------------" + "\n")

read_file.close()
write_file.close()

#Opens servers.txt in read mode.
#Reads each server name one by one.
#Removes the newline using .strip().
#Prints the server name to the terminal.
#Opens another file called server_report.txt in write mode.
#Writes the following for every server: