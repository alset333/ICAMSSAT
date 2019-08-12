#!/usr/bin/env python3

import sys

plat = sys.platform


def linux():
    print("Linux!")
    print("Sorry... this platform isn't supported yet.")


def windows():
    print("Windows!")
    print("This program is in early alpha.")


def cygwin():
    print("Cygwin!")
    print("Sorry... this platform isn't supported yet.")


def mac_os():
    print("MacOS!")
    print("Sorry... this platform isn't supported yet.")


if __name__ == "__main__":
    print("Plat:", plat)

    os_options = {
        'linux': linux,
        'win32': windows,
        'cygwin': cygwin,
        'darwin': mac_os,
    }

    if plat in os_options:
        os_options[plat]()
    else:
        print("Sorry... the platform", plat, "isn't recognized.")
