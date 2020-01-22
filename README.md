# MinIon-program

<h1> MinIon Process Flow </h1>

<h3>Description</h3>

</p>Taking Fastaq file outputs from the MinIon sequencer. Creating Panda's DataFrames. For downstream data analysis.</p>

<h3>Packages Needed</h3>
<p>You will need to download and install these packages, if you would like to run the program.</p>
<ul>
  <li>Seqtk https://github.com/lh3/seqtk.git made by: lh3</li>
</ul>

<h3>Files</h3>
<h5>fastq_to_fasta.py</h5>
<p>This is used to convert any fastq files into fasta files, you will need to replace:
  <ol>
    <li><code>bash_command</code> with the relavent directories of where seqtk is located, and the directory that holds the fastq files.</li>
    <li><code>directory</code> with the relavent directory you want the files to be outputed to.</li>
  </ol>
  

<h3>Work Flow Theory</h3>
<ul>
  <li>Take the fastaq output, convert them to fasta.</li>
  <li>Create a database used to blast against.</li>
  <li>Convert all the files into pandas DataFrames.</li>
  <li>Figure out which directiong the sequence is being read from. </li>
  <li>Figure out which parts are backbone and which are of the genes of interest. </li>
</ul>
