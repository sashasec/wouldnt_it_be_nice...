# Welcome to "wouldnt_it_be_nice..."!
This is a series of scripts I've built for completing specific - yet common tasks. The types of things that come up where you wish you had an alternative from doing it by hand.

## cold_zeek_lookup.py
Wouldn't it be nice to be able to search old zipped logs for a certain characteristic? 
This script can look for an IP in thousands of gzipped Zeek files found in raw cold storage. 
Should work for any zeek log format - here ***json*** zeek output format was used. 

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
Wouldn't it be nice to be able to easily update watchlists on a memcached server in python? 

## ip2location_lookup.py
Wouldn't it be nice to perform a reliable whois lookup and get an estimated geolocation that is actually close to real assett location? 

## email_to_json.py
Wouldn't it be nice to have a python script be able to read emails from a certain abuse mailbox, convert to ***json***, and store in a newline separated file. 
This file would be ideal for ingesting into another security analytics platform of your choosing. 
