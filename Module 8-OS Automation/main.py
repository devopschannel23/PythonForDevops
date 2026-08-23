import os
import re
#os.system("terraform plan && sleep 120 && terraform apply")

#walk through direction tree
# for root,dirs,files in os.walk("."):
#     for file in files:
#         if re.match(r"app\d+\.log", file ):
#             print(file)

#absolute or rel path
# print(os.path.relpath("main.py"))

#path joints
# paths = os.path.join("logs", "abc")
# print(paths)

#Mini Project 1
#cleanup old logs file
# for file in os.listdir():
#     if file.endswith(".log"):
#         os.remove(file)
#         print(f"{file} deleted!")

#Mini Project 2
#To check env variable validators
# required_env = ["DB_USERNAME", "DB_PASSWORD", "DB_HOST"]
# for var in required_env:
#     if os.environ.get(var):
#         print(f"{var} found!")
#     else:
#         print(f"{var} not found!")

#mini project 3
#required files
required_files =  ["Dockerfile", "requirements.txt", "app.py"]
for file in required_files:
    if os.path.exists(file):
        print(f"{file} found, you may use this program!")
    else:
        raise FileNotFoundError (f"{file} doesn't found, to make sure your code runs successfully, these files should be present!")


