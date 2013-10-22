Smith-WatermanAlgorithm
=======================

algorithm for finding local sequence alignments

Example use
======================
from command line:

navigate to the src folder.

pass the FASTA files as arguments.


    python align.py seq1 seq2 
  

Example output
=======================
Results are saved to the results file.

    GCTACGACTCAGCTCAGTGAGCTGCATGCCTTCAAGCTTCGGGTGGAT-CCTGCCAACTT
     |  | | |      ||    |    | ||  | | |      | |     |  |     
    -CGCC-AATTTCA--AGAT-TC-T-GT-CCCAC-AACA--TCCTCGTGG--T-TCTGG-C

    TAAGATC-CT--GGC-CCACAACATGATGTTGGTAATCGCCATGTACTTCCCTGGCGAGT
     |   |   |    |    |   |         |   |  |   |        |||    
    CACTTTGT-TCCC-CG---CCG-AC--------TTCACT-C--CTG---A---GGCTCA-

    TCACTCCAGAGGTCCACCTCTCAGTTG-ACAAGTTCCTTGCGTGCCTGGCTTTGGCTCTG
    |   | |        |     ||  |   |    | | |  |   |||||| ||||  ||
    TG-TTGC-----A--ATGGA-CAAGT-TCC----T-C-TCAGCT-CTGGCTCTGGCCATG

    TCTGAGAAGTACCGCTAAA
    |||||||||||| | ||||
    TCTGAGAAGTACAGATAAA

    Score: 142
