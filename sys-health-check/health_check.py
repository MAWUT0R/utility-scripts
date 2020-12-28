#!/usr/bin/env python3
import shutil
import psutil

def convert_bytes(bytes):
    '''Byte convertion to GB'''
    gb = (bytes/1024**3)
    return gb

def check_disk_usage(disk):
    '''Check disk usage details'''
    usage = shutil.disk_usage(disk)
    total = convert_bytes(usage.total)
    free_space = convert_bytes(usage.free)
    used_space = total - free_space
    used_ratio = (used_space/total)*100
    print("Disk usage summary:")
    print("Total({:.2f} GB), Used({:.2f} GB), Free({:.2f} GB), %Used({:.2f})".format(total, used_space, free_space, used_ratio))
    
def check_cpu_usage(time):
    '''Check cpu usage average over time in seconds'''
    usage = psutil.cpu_percent(time)
    print("Average CPU usage in the last {}s is {}%".format(time, usage))
    
check_disk_usage("/")
check_cpu_usage(1)