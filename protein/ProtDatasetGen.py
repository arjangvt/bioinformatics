"""
This code extracts AA from a PDB file. The format is suitable for 
a Baysian model that we work on.

The output format is 
AA1 AA2 ... AAd SS(concatenated for d residues) SS1 SS2 ... SSd

The input paramaters:
k: is the slidng windows size
path: folder that contains pdp files. 

How to run the code:
python -W ignore ProtDatasetGen.py k=2 p=PDB/*.pdb

in my case:
python3 -W ignore ProtDatasetGen.py k=2 p=PDB/*.pdb

Requirements:
    1- https://biopython.org/
    2- sudo apt-get install dssp

Written by:
    Gerardo Lopez
    Arjang Fahim

Version 1.0.0

Bugs:

"""

import sys
from Bio.PDB import *
from tempfile import gettempdir
import os
import glob
from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP


def ReadProteinDir(folder):

	filenames_list = []
	filespath_list = []
	files = glob.glob(folder)
	for file in files:
		file_path = file.split("/")
		filespath_list.append(file)
		filenames_list.append(file_path[len(file_path)-1])
		
	return filenames_list, filespath_list

def CreateKmers(dssp, k):
    ss = ""
    s_s = ""

    dssp_len = len(list(dssp.keys()))
    for key_index in range(dssp_len-k+1):
        a_key = list(dssp.keys())[key_index:key_index+k]
        for item in a_key:
            print(dssp[item][1], end=" ")
            ss = ss + dssp[item][2]
            s_s = dssp[item][2] + " " + s_s   
        print(ss, s_s[::-1], end = "\n")
        ss = ""
        s_s = ""


def getSS(files_list, path_list, k):
    for i in range(len(files_list)):
        p = PDBParser()
        structure = p.get_structure(files_list[i].split(".")[0], path_list[i])
        model = structure[0]
        dssp = DSSP(model, path_list[i])
        CreateKmers(dssp, k)
        #return dssp


for item in sys.argv:
    arg = item.split("=")
    if arg[0] == "k":
        k = int(arg[1])

    if arg[0] == "p":
        protein_folder = arg[1]

filenames_list, filespath_list = ReadProteinDir(protein_folder)
getSS(filenames_list, filespath_list, k)
