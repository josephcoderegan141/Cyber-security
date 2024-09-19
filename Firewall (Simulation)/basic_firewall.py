import random


def randomIPfunc():

    return f"192.168.1.{random.randint(0, 20)}"

def check_rules(ip,rule):
    for rule_ip,action in rule.items():
        if ip == rule_ip:
            return action
        
    return "allow"


def main():
    firewall_rules ={
        "192.168.1.1": "Block",
        "192.168.1.4": "Block",
        "192.168.1.7": "Block",
        "192.168.1.13": "Block",
        "192.168.1.16": "Block",
        "192.168.1.19": "Block",
    }

    for i in range(10):
        ip_address = randomIPfunc()
        check = check_rules(ip_address,firewall_rules)

        print("IP:",ip_address,"Action:",check,"Count",i)


main()








