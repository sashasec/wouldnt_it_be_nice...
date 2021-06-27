import pyad.adquery
import csv, json
from copy import deepcopy

all_dict = {}
ad_devices = []

#Powershell Command: Get-ADComputer -Properties * | Export-Csv -Path .\ad_computers.csv -Append
q = pyad.adquery.ADQuery()
q.execute_query(attributes = ["Name", "CanonicalName", "OperatingSystem", "whenChanged", "DisplayName", "ObjectCategory"], where_clause = "ObjectClass = 'computer'")
for row in q.get_all_results():
	ad_devices.append(row)
  
print("\nTotal system count: " + str(len(ad_devices)) + "\n\n")
with open("devices.csv" , "a") as p:
	for entry in ad_devices:
		p.write(entry + "\n")

print("\nAll done.\n")

#if __name__ == "__main__":
#	main()
