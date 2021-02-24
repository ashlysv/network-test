##Show use of subprocess to call linux commands via python
#!/usr/bin/env python

import subprocess


def validate_config():
    cmd = "~/home/configfile -load | wc -l"
    value = subprocess.check_output(cmd, shell=True)
    print("Value is : " + str(value))


if __name__ == "__main__":
    validate_config()
