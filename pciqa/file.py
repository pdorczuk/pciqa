""" This file contains all the functions that will derive the data needed by other modules in the program."""

from dataclasses import dataclass, field
from typing import List
import docx2txt
import globals as g


@dataclass
class File:
    name: str
    text: str

    '''
    def __post_init__(self):
        self.pci_version = get_pci_version(self.text)

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
    '''

        
def make_binder():
    """
    Iterate every file in the WORKDIR and create a File object for each.

    This only grabs basic data about the file in a dataclass.
    Later methods will parse and process this data.
    """
    #return [(r, s) for s in SUITS for r in RANKS]
    return [File(word_doc.name, docx2txt.process(word_doc)) for word_doc in g.WORKDIR.glob('*.docx')]

@dataclass
class Binder:
    cards: List[File] = field(default_factory=make_binder)

