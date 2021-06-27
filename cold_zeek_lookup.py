import gzip, os, json, csv

filepaths = []
data = []
outputfile = '/home/user/only_evidence.txt'

Print("This script digs through gziped http ZEEK logs from cold storage.\n\n")
evil_doer = input("Which IP are you looking for? ")

print("Making list of http files")
for dirpath, subdirs, files in os.walk('/opt/zeek/logs/'):
    for x in files: 
        if x.endswith(".gz") and x.startswith("http"):
            filepaths.append(os.path.join(dirpath, x))

print("Reading Gzip files and searching for evil-doer. . . ")
for files in filepaths: 
    print("Reading: " + files)
    f = gzip.open(files, 'rb')
    file_content = f.read()
    if evil_doer in str(file_content): 
        print("IP FOUND!")
        for i in str(file_content).split('\\n'):
            if evil_doer in i: 
                data.append(i + "\n")
                print(i)
    f.close()

print("Appending findings to " + outputfile)
for line in data:
    with open(outputfile, "a") as o:
        o.write(line)

print("Good job! Now go eat a cookie. You deserve it :)")
