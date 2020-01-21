# MinIon-program

<h1> MinIon Process Flow </h1>

<h3>Description</h3>

</p>Taking Fastaq file outputs from the MinIon sequencer, and making them readable and easy to process. So that data analysis can be carried out on them.</p>

<h3>Work Flow Theory</h3>
<ul>
<li>Take the fastaq output, convert them to fasta.</li>
<li>Create a database used to blast against.</li>
<li>Convert all the files into pandas DataFrames.</li>
<li>Figure out which directiong the sequence is being read from. </li>
<li>Figure out which parts are backbone and which are of the genes of interest. </li>
</ul>
