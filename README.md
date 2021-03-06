# Welcome to "wouldnt_it_be_nice..."!
This is a series of scripts I've built for completing specific tasks I've encountered. The types of things that come up where you wish you had an alternative from doing it by hand. Hopefully this could give others a starting point. 

I will be discussing more behind each of these scripts on my [blog](https://sashasec.medium.com/wouldnt-it-be-nice-1866fd18a99b) when I get a chance. 

## cold_zeek_lookup.py
Wouldn't it be nice to be able to search old zipped logs for a certain characteristic? 
This script can look for an IP in thousands of gzipped Zeek files found in raw cold storage. 
Should work for any zeek log format - here ***json*** zeek output format was used. 

## paramiko_ssh.py
Woudldn't it be nice to be able to run the same command against multiple linux hosts without needing to get an orchestration (puppet, chef, ansible) product deployed? 
Try this script to run whatever commands you want against a list of systems found in `hosts.txt`. 

## simple_simulation_report.py
Wouldn't it be nice to have a script to send personalized phishing simulation reports to managers about the participation of their direct reports? 
This script accepts the exported phishing simulation CSV report and sends an email to each manager only listing their direct reports. Not rocket science, but as of 2021, I have tested the commercial solutions from Mimecast Attata, Sophos Phish Threat, KnowB4, and Cofense Phishme and I am not aware of any of them (or others) that offer this granularity in reporting capabilities. 

Anticipates the following fields: 
    
    'Email', 'Recipient Name', 'Recipient Group', 'Department', 'Location', 'Opened Email?', 'Opened Email Timestamp', 'Clicked Link?', 'Clicked Link Timestamp', 'Reported Phish?', 'New/Repeat Reporter', 'Reported Phish Timestamp', 'Time to Report (in seconds)', 'Remote IP', 'GeoIP Country', 'GeoIP City', 'GeoIP ISP', 'Last DSN', 'Last Email Status', 'Last Email Status Timestamp', 'Language', 'Browser', 'User-Agent', 'Mobile?', 'Seconds Spent on Education Page', 'LASTNAME', 'FirstName', 'MANAGER', 'Jobtitle', 'Division', 'StateDate', 'EmployeeID', 'ManagerEmail', 'EmployeeType'

## upgrade_simulation_report.py
Script retrieves simulation report directly from the API of the phishing simulation platform instead of from a CSV. Saves a quick step. 

## asset_inventory_ad_pull.py
Wouldn't it be nice to export systems listed in Active Directory and interact with them directly in python? 

## update_memcached_server.py
Wouldn't it be nice to be able to easily update watchlists on a memcached server in python? Be sure to update "SERVER_IP" with the IP of your memcached host. 

## email_to_json.py
Wouldn't it be nice to have a python script that is able to read emails from a certain email account, convert the content to ***json***, and store the output in a newline separated file. 
This file would be ideal for ingesting into another security analytics platform of your choosing for analysis. 
Significant to note: 
- In this given scenario, the email needing to be analyzed is the attachment of another email. 
- Small detail - but thought it worth mentioning. Analyzing only the email in a mailbox folder is a little simpler. 
