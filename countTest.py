##To run in LINUX server below line is needed
#!/usr/bin/env python

import os
import time


def main():
    startdate = input('\033[1m#Enter date(YYYY-MM-DD):\033[0M')
    cmd = input("Enter command to search: ")
    cs_count = 0
    cs_fail = 0
    cs_succ = 0
    pattern = '%Y-%m-%d'
    epoch = int(time.mktime(time.strptime(startdate, pattern)))

    filename = "/home/var/log/NBI.log"
    filelist = []
    faillist = {'Wrong test': 0,
                'Wrong value': 0}
    for i in range(0, 151):
        try:
            if (os.path.isfile(filename)):
                modi_date = os.path.getmtime(filename)
                if epoch <= modi_date:
                    filelist.append(filename)
                    i = i + 1
                filename = filename[:37] + "." + str(i)
            else:
                i = 160
        except:
            i = 155

    length = len(filelist)
    for i in range(0, length - 2):
        filelist.pop(0)

    for name in filelist:
        nbifile = open(name, "r")
        print("Reading file ", nbifile.name)
        modi_date = os.path.getmtime(nbifile.name)
        for line in nbifile:
            if (startdate in line):
                if cmd in line:
                    cs_count = cs_count + 1
            if sid in line:
                if 'None' in line:
                    t = 0
                    cs_fail = cs_fail + 1
                    for key in faillist:
                        if key in line:
                            t = 1
                            faillist[key] = faillist[key] + 1
                        if t == 0:
                            print(line)
                elif 'OK' in line:
                    cs_succ = cs_succ + 1
        nbifile.close()

    print("Values : ", cs_count, cs_succ, cs_fail)


if __name__ == "__main__":
    main()
