import os
import requests
import time

prefixes = ["/usr", "/bin", "/etc", "/var"]

filename = input("Enter temporary file name: ")
filename = os.path.abspath(filename)

folder = os.path.dirname(filename)

if not os.path.exists(folder):
    print("Folder does not exist")
    exit(1)
if any([folder.startswith(prefix) for prefix in prefixes]):
    print("Folder is on deny list!")
    exit(1)

try:
    file = os.open(filename, os.O_WRONLY | os.O_CREAT | os.O_NOFOLLOW)
except PermissionError:
    print("Permission denied!")
    exit(1)
except Exception as e:
    print("Error opening file", e)
    exit(1)

try:
    lines = int(input("Enter the number of urls: "))
    if lines <= 0:
        print("Number must be above 0")
        exit(1)
    if lines > 100:
        print("Number must be less than 100")
        exit(1)

except ValueError:
    print("Invalid number")
    os.close(file)
    exit(1)

timesum = 0
for i in range(lines):
    url = input("Enter url: ")
    
    start = time.time()

    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Connection error")
        continue
    except requests.exceptions.RequestException as e:
        print("Connection error")
        continue
    except Exception as e:
        print("Exception")
        continue

    end = time.time()

    os.write(file, (str(response.status_code) + "\n").encode())
    timesum += end - start

os.write(file, ("Finished in " + str(timesum) + " seconds\n").encode())
os.write(file, ("Average time: " + str(timesum / lines) + " seconds\n").encode())
os.close(file)
