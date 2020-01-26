import os
import re

dropbox_fastq_dir = '/Users/andrewpowers/Documents/preoutput_fastq/outputSkip/'
all_relevant_fastq = []
for file in os.listdir(dropbox_fastq_dir):
    file_relevant_fastq = re.findall(r'fastq_runid_.+\.fastq', file)
    for each in file_relevant_fastq:
        all_relevant_fastq.append(each)

bash_command = "/Users/andrewpowers/Documents/seqtk/./seqtk seq -a {} > /Users/andrewpowers/Documents/output_fasta_new/{}"
def file_name_search():
    """
    Look through a directory, taking file names to use for the output files.
    """
    count = 1
    for file in all_relevant_fastq:
        output_file = re.sub('fastq', 'fasta', file)
        os.system(bash_command.format(dropbox_fastq_dir + file, output_file))
        print(f'{file} Converted')
        print(f'{count} out of {len(all_relevant_fastq)} done.')
        count += 1
    print('Conversion Done.')

file_name_search()
