import configparser
from ftplib import FTP
from subprocess import Popen, PIPE
import os
# print(ftp_user)
# print(ftp_password)
# print(ftp_url)
# print(ftp_port)
# print(ftp_path)

process = Popen(["git", "show", "--pretty=format:", "--name-only", "-1"], stdout=PIPE, stderr=PIPE)
changed_files = set(process.stdout)
formatted_files = []

if len(changed_files) == 0:
    print("No files found to upload, are you sure this is a git directory?")
    quit()

config = configparser.ConfigParser()
config.read('uploader.ini')

ftp_user = config['SERVER']['user']
ftp_password = config['SERVER']['password']
ftp_url = config['SERVER']['server_url']
ftp_port = config['SERVER']['server_port']
ftp_path = config['SERVER']['base_path']


# format the files and print them so the user can double check the files
for file in changed_files:
    file = file.decode("utf-8")
    file = file.replace('\n', "")
    formatted_files.append(file)
    print(file)

confirm_prompt = input("Are you sure you want to upload the above files? y/n")

# make the user confirm
if confirm_prompt == 'y':
    print("ok copying files")
    ftp = FTP(ftp_url)
    ftp.login(user=ftp_user, passwd=ftp_password)
    # ftp.cwd(ftp_path)
    # ftp.retrlines('LIST')

    # loop files
    for formatted_file in formatted_files:
        ftp.cwd(ftp_path)
        sub_dir = os.path.dirname(formatted_file)
        folders = sub_dir.split('/')

        # navigate trough the directories and create them if required
        for folder in folders:
            if folder not in ftp.nlst():
                ftp.mkd(folder)
                ftp.cwd(folder)
            else:
                ftp.cwd(folder)

        file_name = os.path.basename(formatted_file)
        local_file = open(formatted_file, 'rb')
        ftp.storlines("STOR "+file_name, local_file)
        local_file.close()
    print("All files uploaded")
else:
    print("No files uploaded")
