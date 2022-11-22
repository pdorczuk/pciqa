""" This file contains all the functions that will derive the data needed by other modules in the program."""

from typing import List
from collections import namedtuple
from datetime import date
import docx2txt

import globals as g



def make_binder():
    """Iterate every file in the WORKDIR and append it to the globals.py BINDER list.

        This only grabs basic data about the file in an immutable NamedTuple.
        Later functions will parse and process this data.
    """
    def get_pci_version(text) -> float:
        """Return the PCI version of the file based on unique text in each.
        
            Args:
                text: A string containing the text of the file.

            Returns:
                pci_version: A float containing the PCI version of the file.
        """
        unique_text = {
            '3.2': "PCI DSS v3.2.1 Template for Report on Compliance",
            '4.0': "PCI DSS v4.0 Report on Compliance Template"
        }
        
        for key, value in unique_text.items():
            if value in text:
                return float(key)

    for word_doc in g.WORKDIR.glob('*.docx'):
        File = namedtuple('File', ['filename', 'text', 'pci_version'])
        g.BINDER.append(File(filename=word_doc.name, text=docx2txt.process(word_doc), pci_version=get_pci_version(docx2txt.process(word_doc))))
