import os
from collections import defaultdict
import datetime
from dateutil.relativedelta import relativedelta
  
# adding years to a particular date
dataAfter3year = str(datetime.date.today()+ relativedelta(years=3))
print(dataAfter3year)

with open("userlist.txt","r") as file:
    groups=defaultdict(list)
    for line in file:
        userinfo = line
        data = userinfo[0:-1].split(" ")
        name = data[0]
        role = data[1]
        password = data[2]
        roles = role.split(",")
        commant_role = ",".join(roles)
        print(commant_role)
        os.system(f"sudo -S useradd {name} -c {commant_role} -e {dataAfter3year}")
        os.system(f"echo {name}:{password} | sudo -S chpasswd")
        for group in roles:
            groups[group].append(name)
    for group_name,users in groups.items():
      os.system(f"sudo -S groupadd {group_name}")
      os.system(f"sudo -S mkdir ~/{group_name}")
      os.system(f"sudo -S chgrp {group_name} ~/{group_name}")
      users_name = ",".join(users)
      os.system(f"sudo -S gpasswd -M {users_name} {group_name}")
      print (f"{group_name} ")

