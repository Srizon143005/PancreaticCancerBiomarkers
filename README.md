<h1>Pancreatic Cancer Biomarkers Identification</h1>
<p>Pancreatic cancer is right now the forth largest cause of cancer-related deaths. Within 2030 it'll be at second place just behind lung cancer as it's common for both male and female. Early diagnosis is one good solution for pancreatic cancer patients. This repository contains all the necessary files and codes for identification of progonstic biomarkers for pancreatic cancer. It may get updated in future depending on more advanced researches.</p>


<h2><b>Getting Started</b></h2>
<p>To use the codes and relevent files, first we need some datasets and some tools in which you can run these codes. <a href="#DataCollection"><b>Data Collection Section</b></a> describes from where data can be collected &amp; <a href="#Installation"><b>Installation Section</b></a> describes where to get the desired tools. Finally, <a href="#WorkingProcess"><b>Working Process Section</b></a> describes through which sequence the work has been done.</p>


<h2 id="DataCollection"><b>Data Collection</b></h2>
<p>Three mRNA microarray datasets (GSE15471, GSE16515 &amp; GSE28725) and one microRNA expression dataset (GSE41372) have been used for this experiment. All these datasets were downloaded from <a href="https://www.ncbi.nlm.nih.gov/geo/"><b>GEO</b></a>. Although the datasets are included in this repository under the folder '<b>Main Data</b>', you can still download it from the given links and also find out data description for each dataset.</p>

<a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE15471"><b>GSE15471</b></a>,
<a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE16515"><b>GSE16515</b></a>,
<a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE28725"><b>GSE28725</b></a>,
<a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE41372"><b>GSE41372</b></a>


<h2 id="Installation"><b>Installation</b></h2>
<p>For implementing Student's T-Test, R language &amp; RStudio platform have been used. For additional comparing and counting jobs, Python has been used. Pandas package was used to read csv files. RStudio is available in <a href="https://www.rstudio.com/products/rstudio/download/"><b>RStudio Official Website</b></a>. Anaconda software can be downloaded from <a href="https://www.anaconda.com/distribution/"><b>Anaconda Official Website</b></a> as well. Moreover, Pandas Library was intalled by writing following command in Anaconda Prompt:</p>

<code>
    conda install -c anaconda pandas
</code>


<h2 id="WorkingProcess"><b>Working Process</b></h2>
<p>The following steps were followed:</p>
<ol>
    <li>For each dataset, get the processed data from <a href="https://www.ncbi.nlm.nih.gov/geo/geo2r"><b>GEO2R</b></a>, run R code to evaluate adjusted P-values and select the desired genes. All files can be found in the corresponding folders.</li>
    <li>For each selected microRNA, get target genes using miRecords online tool.</li>
    <li>Now run Python files located in '<b>Python Codes To Compare and Select DEGs, DEMs, Common DEGs among Target Genes</b>' floder to get the desired biomarkers.</li>
</ol>


<h2><b>Conclusion</b></h2>
<p>In this experiment we tried to select potential biomarkers for pancreatic cancer &amp; selected two biomarkers in the process.</p>
