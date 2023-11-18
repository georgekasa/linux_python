# linux_python
Using PyPDF2, I have "translated" the cat and grep command to read pdf's via python


how to use cat_pdf:
python3 cat_pdf.py /home/gkasap/Desktop/very_good_2012-06-15_Armin_Tavakol_MSc_Thesis_DCO.pdf
Text extracted from the PDF:
 Digitally Controlled Oscillator for
WiMAX in 40 nm
Master’s Thesis
Armin TavakolDigitally Controlled Oscillator for
WiMAX in 40 nm
THESIS
..... (will print the whole pdf)

how to use grep_pdf:
############################################################
python3 grep_pdf.py 2 3 "background" .
python3 grep_pdf.py before(2) after(3) (search word)"background" (current directory and the subdirectories or could be this a specific path).


/home/gkasap/Documents/Python/razavi2016.pdf
methods. In this article, we study 
the properties of this logic family.
background
In the early 1980s, the design of high-
speed digital CMOS circuits faced 
some interesting challenges. One 
################################################################################

python3 grep_pdf.py "background" .
/home/gkasap/Documents/Python/razavi2016.pdf
background
################################################################################
/home/gkasap/Documents/Python/projects/isbn9789526056388.pdf
thesis fundamentals but to provide sufﬁcient background for the rest of
################################################################################


