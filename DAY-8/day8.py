try:
    print("Connecting to monitoring server....")
    number = int("N/A")
    print(number)
except ValueError:
    print("invalid cpu value is received.")
finally:
    print("closing monitoring connection")
print("monitoring Ended")
