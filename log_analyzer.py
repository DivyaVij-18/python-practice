try:
    successful_logins=0
    failed_logins=0
    failed_ips={}
    with open("access.log","r") as file:
      for line in file:
        if "SUCCESS" in line:
            successful_logins+=1
        elif "FAILED" in line:
            failed_logins+=1
            ip = line.split()[0]                # parts = line.split() ip = parts[0]
            if ip not in failed_ips:
                failed_ips[ip]=1
            else:
                failed_ips[ip]+=1
    print(f"Total successful logins:{successful_logins}")
    print(f"Total failed logins:{failed_logins}")
    print("\nSuspicious IPs:")
    for ip, count in failed_ips.items():
      if failed_ips[ip] >= 3:
        print(f"{ip} attempted {count} failed logins")


except FileNotFoundError:
    print("Log file not found.")
 



