# requires: pip3 install pymemcache
# Be sure to update "SERVER_IP" with the IP address of your memcached server 

import argparse, glob, sys, os, requests, re, json, base64, time
from pymemcache.client.base import Client
import telnetlib 

def get_key(client):
    label = input("Which label type are you wanting to use? (hostname, domain, email, ip, hash, or user) ")
    term = input("What is the key term? ")
    key = label + '_' + term.strip()
    print(client.get(key))
    return ""

def add_key(client):
    keys = []
    label = input("Which label type are you wanting to use? (hostname, domain, email, ip, hash, or user) ")
    term = input("What is the key term? ")
    value = input("What is the value? ")
    key = label + '_' + term.strip()
    if(client.set(key, value.strip(), 0)): #15778800)):
        print(key + " added to memcached.")
        keys.append(key)
    else: 
        print(key + " failed to add . . . ")
    print("\n\n" + str(len(keys)) + " keys added.")
    print("Item count: " + str(client.stats()[b'curr_items']))
    return ""

def delete_key(client):
    keys = []
    label = input("Which label type are you wanting to use? (hostname, domain, email, ip, hash, or user) ")
    term = input("What is the key term? ")
    key = label + '_' + term.strip()
    if(client.delete(key)): #15778800)):
        print(key + " deleted from memcached.")
        keys.append(key)
    else: 
        print(key + " failed to delete. . . ")
    print("\n\n" + str(len(keys)) + " keys removed.")
    print("Item count: " + str(client.stats()[b'curr_items']))
    return ""

def delete_all_keys(client):
    print("\nLet's flush it!")
    print(client.flush_all())
    print("Item count: " + str(client.stats()[b'curr_items']))

def all_keys(count):
    client = Client(('SERVER_IP', 11211))
    print(client.stats("cachedump"))
    return ""

def delete_from_file(client, filename):
    keys = []
    label = input("Which label type are these events? (hostname, domain, email, ip, hash, or user) ")
    with open(filename) as importfile: 
        for line in importfile:
            #print(line)
            key = label + '_' + line.strip()
            if(client.delete(key)): #15778800)):
                print(key + " deleted from memcached.")
                keys.append(key)
            else: 
                print(key + " failed to delete. . . ")
    print("\n\n" + str(len(keys)) + " keys removed.")
    print("Item count: " + str(client.stats()[b'curr_items']))
    return ""

def update_from_file(client, label, filename, value): #format: hostname_workstation0123456 -> win7/watch/etc 
    #client = Client(('SERVER_IP', 11211))
    keys = []
    with open(filename) as importfile: 
        for line in importfile:
            #print(line)
            key = label + '_' + line.strip()
            if(client.set(key, value, 0)): #15778800)):
                print(key + " added to memcached.")
                keys.append(key)
    print("\n\n" + str(len(keys)) + " keys added.")
    print("Item count: " + str(client.stats()[b'curr_items']))
    return ""

def main():
    parser=argparse.ArgumentParser()
    
    # Driver Flags
    parser.add_argument('-hf','--hostFile',action='store',required=False,help='Reads file contents and uploads with HOSTNAME flag.')
    parser.add_argument('-df','--domainFile',action='store',required=False,help='Reads file contents and uploads with DOMAIN flag.')
    parser.add_argument('-ef','--emailFile',action='store',required=False,help='Reads file contents and uploads with EMAIL flag.')
    parser.add_argument('-if','--ipFile',action='store',required=False,help='Reads file contents and uploads with IP flag.')
    parser.add_argument('-uf','--userFile',action='store',required=False,help='Reads file contents and uploads with USER flag.')
    parser.add_argument('-sf','--hashFile', action='store',required=False,help='Reads file contents and uploads with HASH flag.')
    parser.add_argument('-ddf','--deleteFile',action='store',required=False,help='Reads file contents and deletes keys.')
    parser.add_argument('-m','--manual',action='store_true',required=False,help='Takes a single key:value pair and adds it per a given label.')
    parser.add_argument('-md','--manualDelete',action='store_true',required=False,help='Takes a single key and removes it per a given label.')
    parser.add_argument('-g','--getValue',action='store_true',required=False,help='Returns the value of a given key.')
    args=parser.parse_args()

    #Ascii Intro

    print("  __  __                               _              _  ")
    print(" |  \/  | ___ _ __ ___   ___ __ _  ___| |__   ___  __| | ")
    print(" | |\/| |/ _ \ '_ ` _ \ / __/ _` |/ __| '_ \ / _ \/ _` | ")
    print(" | |  | |  __/ | | | | | (_| (_| | (__| | | |  __/ (_| | ")
    print(" |_|  |_|\___|_| |_| |_|\___\__,_|\___|_| |_|\___|\__,_| ")
    print("                                                         ")

    #filename = "win7.txt"
    client = Client(('SERVER_IP', 11211))
    #keys = []
    print("Let's see some MEMCACHED MAGIC!\n")
     
    #print(dir(client))

    print("Current item count: " + str(client.stats()[b'curr_items']))

    if args.hostFile:
        update_from_file(client, "hostname", args.hostFile, "lost")
    if args.domainFile:
        update_from_file(client, "domain", args.domainFile, "malware")
    if args.emailFile: 
        update_from_file(client, "email", args.emailFile, "phishing")
    if args.ipFile:
        update_from_file(client, "ip", args.ipFile, "phishing")
    if args.userFile:
        update_from_file(client, "user", args.userFile, "suspicious")
    if args.hashFile:
        update_from_file(client, "hash", args.hashFile, "malware")
    if args.deleteFile:
        delete_from_file(client, args.deleteFile)
    if args.manual:
        add_key(client)
    if args.manualDelete:
        delete_key(client)
    if args.getValue:
        get_key(client)
    else: 
        print("\nNothing to do. . . ") 
    print("\nDone!")

if __name__ == "__main__":
    main()
