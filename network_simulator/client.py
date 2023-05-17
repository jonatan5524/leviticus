#!/usr/bin/env python

import sys
import random
import requests
from time import sleep

NORMAL_HOSTS = [
    "10.0.2.48",
    "10.0.2.123",
    "10.0.2.89",
]

ILLEGAL_HOSTS = [
    "10.0.2.57",
    "10.0.2.32",
]

def send_request(hosts):
    host = random.choice(hosts)
    requests.get(f"https://{host}/")


## A normal user only sends packets to normal hosts
def normal_routine():
    while True:
        send_request(NORMAL_HOSTS)
        sleep(random.randint(3, 10))


## An addict usually sends packets to normal hosts, but also sends packets to illegal hosts
## from time to time
def addict_routine(illegal_host_indices):
    illegal_hosts = [host for i, host in enumerate(ILLEGAL_HOSTS) if i in illegal_host_indices]
    while True:
        if random.random() > 0.05:
            send_request(NORMAL_HOSTS)
        else:
            send_request(illegal_hosts)

        sleep(random.randint(3, 10))


def print_help():
    print("Usage: lev_client normal/addict [illegal hosts]")


def main():
    if len(sys.argv) == 1:
        print("no arguements provided")
        print_help()
        exit(1)

    role = sys.argv[1]
    if role not in ("normal", "addict") or (role == "addict" and len(sys.argv) == 2):
        print_help()
        exit(1)

    if role == "addict":
        try:
            illegal_host_indices = [int(i) for i in sys.argv[2:]]
        except ValueError:
            print("indices should be numbers")
            print_help()
            exit(1)
        addict_routine(illegal_host_indices)
    else:
        normal_routine()

if __name__ == "__main__":
    main()
