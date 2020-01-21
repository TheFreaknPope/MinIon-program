""" Python Program """
from Bio import SeqIO
import re
import pandas as pd
import numpy as np


#----------------------------------------------------------------------------

"""
Class creation setion
"""

class References():
    """
    Turns the Fasta file into a Pandas DataFrame, which can then be used for
    downstream processes.
    """
    def __init__(self):
        self.ref_all_reads = pd.DataFrame()





    def to_df(self, file):
        count = 0


        for seqio_object in SeqIO.parse(file, format='fasta'):
            seq = str(seqio_object.seq)
            idtoknow = re.sub(r'ORF_ID: ', '', seqio_object.description.split('|')[1])
            length = re.sub(r'ORF_SIZE:', '', seqio_object.description.split('|')[2])
            gene_id = re.sub(r'GENE_ID: ', '', seqio_object.description.split('|')[4])
            template_accession = re.sub(r'TEMPLATE_ACCESSION: ', '', seqio_object.description.split('|')[3])
            self.ref_all_reads = self.ref_all_reads.append(pd.DataFrame({'Sequence': seq,
                                                   'ORF_ID': idtoknow,
                                                   'ORF_SIZE': length,
                                                   'GENE_ID': gene_id,
                                                   'TEMPLATE_ACCESSION': template_accession},
                                                   index=[count]))
            count += 1
        return self.ref_all_reads

    def __repr__(self):
        return 'This is a Pandas DataFrame'

    def __str__(self):
        return self.__repr__()



class Reads():
    '''
    This is to take the MinIon Reads and then convert them into a DataFrame,
    which has attributes containing,Sequence, Read ID, Length of ID, and what
    pore/channel was used.
    '''

    def __init__(self):
        self.reads_dataframe = pd.DataFrame()

    def add_to_df(self, file):
        count = 0
        ref = SeqIO.parse(file, format='fasta')
        for seqio_object in ref:
            seq = str(seqio_object.seq)
            id_read = seqio_object.id
            order_read = re.sub(r'read=', '', seqio_object.description).split(' ')[2]
            channel = re.sub(r'ch=', '', seqio_object.description).split(' ')[3]
            length = len(seq)
            self.reads_dataframe = self.reads_dataframe.append(pd.DataFrame({'Sequence': seq,
                                                               'Read_ID': id_read,
                                                               'Length': length,
                                                               'Channel_Pore': channel,
                                                               'Read_Order': order_read},
                                                               index=[count]))
            count += 1
        return self.reads_dataframe

    def __repr__(self):
        return 'DataFrame of all pore reads.'
#----------------------------------------------------------------------------
#Note: Find out direction of the sequence that is being read. Like 5' from 3'

"""
Set up new Backbone DataFrame as our Blast database
"""

backbone_3p = 'ATATCGGCATAGTATAATACGACAAGGTGAGGAACTAAACCCGCGCCATGGCCAAGCCTTTGTCTCAAGAAGAATCCACCCTCATTGAAAGAGCAACGGCTACAATCAACAGCATCCCCATCTCTGAAGACTACAGCGTCGCCAGCGCAGCTCTCTCTAGCGACGGCCGCATCTTCACTGGTGTCAATGTATATCATTTTACTGGGGGACCTTGTGCAGAACTCGTGGTGCTGGGCACTGCTGCTGCTGCGGCAGCTGGCAACCTGACTTGTATCGTCGCGATCGGAAATGAGAACAGGGGCATCTTGAGCCCCTGCGGACGGTGCCGACAGGTGCTTCTCGATCTGCATCCTGGGATCAAAGCCATAGTGAAGGACAGTGATGGACAGCCGACGGCAGTTGGGATTCGTGAATTGCTGCCCTCTGGTTATGTGTGGGAGGGCTAAACCGGTCAGCGCGTCTGGAACAATCAACCTCTGGATTACAAAATTTGTGAAAGATTGACTGGTATTCTTAACTATGTTGCTCCTTTTACGCTATGTGGATACGCTGCTTTAATGCCTTTGTATCATGCTATTGCTTCCCGTATGGCTTTCATTTTCTCCTCCTTGTATAAATCCTGGTTGCTGTCTCTTTATGAGGAGTTGTGGCCCGTTGTCAGGCAACGTGGCGTGGTGTGCACTGTGTTTGCTGACGCAACCCCCACTGGTTGGGGCATTGCCACCACCTGTCAGCTCCTTTCCGGGACTTTCGCTTTCCCCCTCCCTATTGCCACGGCGGAACTCATCGCCGCCTGCCTTGCCCGCTGCTGGACAGGGGCTCGGCTGTTGGGCACTGACAATTCCGTGGTGTTGTCGGGGAAGCTGACGTCCTTTCCATGGCTGCTCGCCTGTGTTGCCACCTGGATTCTGCGCGGGACGTCCTTC'
backbone_5p = 'TTGATATCCAGCACGACTACAAAGACCATGACGGTGATTATAAAGATCATGACATCGATTACAAGGATGACGATGACAAGTAATGGCCGCAGCCTCGAGCAGCGATCGCGCGGGATCCGCGTCTAGCCAGTAGGTCCACTATGAGT'

backbone_df = pd.DataFrame()
backbone_df = backbone_df.append(pd.DataFrame({'Sequence': backbone_3p,
                                              'GENE_ID': "3'"},
                                             index=[0]))
backbone_df = backbone_df.append(pd.DataFrame({'Sequence': backbone_5p,
                                              'GENE_ID': "5'"},
                                             index=[1]))

#----------------------------------------------------------------------------
"""
Program running section
"""





new = References()
# reference_fasta_file = 'horf81_cloneInfo20120427.fasta'
Reference_blast = new.to_df(#reference_fasta_file)
