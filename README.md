# MinIon-program

<h1> MinIon Process Flow </h1>

<h3>Description</h3>

</p>Taking Fastaq file outputs from the MinIon sequencer. Creating Panda's DataFrames. For downstream data analysis.</p>

<h3>Packages Needed</h3>
<p>You will need to download and insteall these packages, if you would like to run the program</p>
<ul>
  <li>Seqtk https://github.com/lh3/seqtk.git made by: lh3</li>
</ul>

<h3>Work Flow Theory</h3>
<ul>
  <li>Take the fastaq output, convert them to fasta.</li>
  <li>Create a database used to blast against.</li>
  <li>Convert all the files into pandas DataFrames.</li>
  <li>Figure out which directiong the sequence is being read from. </li>
  <li>Figure out which parts are backbone and which are of the genes of interest. </li>
</ul>
