from globals import BINDER
import file


""" All the functions in this file will be called by pciqa.py. They will be called in the order they are defined."""

def checkboxes():
    for f in BINDER:
        if f.pci_version == 3.2:
            pass
