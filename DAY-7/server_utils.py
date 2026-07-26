def check_health(cpu):
    if cpu > 90:
        return "Critical"
    elif cpu > 70:
        return "Warning"
    else:
        return "Healthy"
    
