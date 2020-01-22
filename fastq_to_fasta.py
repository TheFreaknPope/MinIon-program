import os
import re

bash_command = "/Users/andrewpowers/Documents/seqtk/./seqtk seq -a {} > /Users/andrewpowers/Documents/server/fasta_pass/{}"

def file_name_search():
    """
    Look through a directory, taking file names to use for the output files.
    """
    directory = "/Users/andrewpowers/Documents/server/fastq_pass"

    for file in os.listdir(directory):
          output_file = re.sub('fastq', 'fasta', file)
          os.system(bash_command.format(directory+"/"+file, output_file))
          print('File {} converted to fasta.'.format(file))
    print('Conversion Done.')

file_name_search()
