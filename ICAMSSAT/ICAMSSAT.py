#!/usr/bin/env python3

import sys
import os
import subprocess
import hashlib

HASH_256_INSTALL_CHOCOLATEY_BAT = 'c6703b70d61b37e62f5252130dbc654739f66e370fc27864a8abd956928af63c'



plat = sys.platform


def get_sha256_hash(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def linux():
    print("Linux!")
    print("Sorry... this platform isn't supported yet.")


def windows():
    print("Windows!")
    print("This program is in early alpha.")

    import ctypes
    if ctypes.windll.shell32.IsUserAnAdmin():
        win_choc_installer = os.path.normpath(sys.path[0] + '/Windows/install_chocolatey.bat')
        if os.path.isfile(win_choc_installer):

            file_hash = get_sha256_hash(win_choc_installer)

            if file_hash == HASH_256_INSTALL_CHOCOLATEY_BAT:
                print("Stage 1: Installing chocolatey...")
                subprocess.call(win_choc_installer)

            else:
                print("Error! Warning! Hash did not match! This shouldn't happen, and means files were tampered.")
                print("Expected hash:\t", HASH_256_INSTALL_CHOCOLATEY_BAT)
                print("Actual hash:\t", file_hash)

        else:
            print("Error, could not find chocolatey installer script:", win_choc_installer)
    else:
        print("Error! Insufficient permissions. Please re-run as admin.")

    print("All done!")


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
