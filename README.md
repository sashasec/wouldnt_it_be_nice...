# wouldnt_it_be_nice...
collection of minor automation tasks

## cold_zeek_lookup.py
This script can look for an IP in gzipped Zeek files found in raw cold storage. 
Should work for any zeek log format - here ***json*** zeek output format was used. 

## simple_simulation_report.py
Accepts the exported phishing simulation CSV report and sends an email to each manager in the company listing only their direct reports. 
Anticipates the following fields: 
    
    'Email', 'Recipient Name', 'Recipient Group', 'Department', 'Location', 'Opened Email?', 'Opened Email Timestamp', 'Clicked Link?', 'Clicked Link Timestamp', 'Reported Phish?', 'New/Repeat Reporter', 'Reported Phish Timestamp', 'Time to Report (in seconds)', 'Remote IP', 'GeoIP Country', 'GeoIP City', 'GeoIP ISP', 'Last DSN', 'Last Email Status', 'Last Email Status Timestamp', 'Language', 'Browser', 'User-Agent', 'Mobile?', 'Seconds Spent on Education Page', 'LASTNAME', 'FirstName', 'MANAGER', 'Jobtitle', 'Division', 'StateDate', 'EmployeeID', 'ManagerEmail', 'EmployeeType'

## upgrade_simulation_report.py
Logs in to cofense and downloads the report direction for the desired simulation. 
