import glob
import os
from Bio import SeqIO
#import pathlib
from shutil import copyfile
import argparse

"""Shuffle sequences of all Bralibase raw fasta files

This script will triverse to all Bralibase directorys and shuffle for
all found raw files the sequences within that file.

Example:
shuffle_bralibase.py

Attributes Inputparameters:
    - bralibase_dir
    - bralibase_name
    - new_bralibase_dir
    - new_bralibase_name

Todo:
    * test if it is working.


.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""


##import parameters

parser = argparse.ArgumentParser()
 parser.add_argument('--bralibase_dir', dest='bralibase_dir', type=str,
    default='/home/muellert/Dokumente/locarna_parameteropt/Data/',
    help='bralibase dir to change')
parser.add_argument('--bralibase_name', dest='bralibase_name', type=str,
   default='BRALIBASEk2',
   help='name of bralibase to change')
parser.add_argument('--new_bralibase_dir', dest='new_bralibase_dir', type=str,
   default='/home/muellert/Dokumente/locarna_parameteropt/Data/',
   help='new bralibase dir')
parser.add_argument('--new_bralibase_name', dest='new_bralibase_name', type=str,
    default='BRALIBASE-SHUFFLED',
    help='new bralibase name')


#bralibase_dir = '/home/muellert/Dokumente/locarna_parameteropt/Data/'
#bralibase_name = 'BRALIBASEk2'
bralibase_path = bralibase_dir + bralibase_name

#new_bralibase_dir = '/home/muellert/Dokumente/locarna_parameteropt/Data/'
#new_bralibase_name = 'BRALIBASE-SHUFFLED'
new_bralibase_path = new_bralibase_dir + new_bralibase_name
shuffle_fasta_tool = 'fasta-shuffle-letters -kmer 2 '


families = glob.glob(bralibase_path + '/k2/*')
#print families
for famdir in families:
    #print famdir
    famdir_shuf = famdir.replace(bralibase_path,new_bralibase_path)
    #print famdir_shuf
    # test if dir already exist
    if os.path.isdir(famdir_shuf)==False:
        # make new dir
        os.makedirs(famdir_shuf)
    else:
        print 'Warning: the shuffled directory does already exist'
    for unshuffa in glob.glob(famdir+'/*.raw.fa'):
        #print unshuffa
        output_file = unshuffa.replace(bralibase_name, new_bralibase_name)
        #print output_file
        cmd_call = shuffle_fasta_tool + unshuffa + ' ' + output_file
        os.system(cmd_call)
    for unshuffa in glob.glob(famdir+'/*.ref.fa'):
        new_ref_location = unshuffa.replace(bralibase_name, new_bralibase_name)
        copyfile(unshuffa, new_ref_location)
