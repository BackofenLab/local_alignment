# Global and local alignment benchmarksets

All benchmarksets used to study the locality dilemma of Sankoff-like RNAalignments are repesented in this folder. In this study 3 respectively 5 benchmarksets where used. 
- Global alignment benchmark set:\
	1.) [BRAliBase](./BRALIBASEk2.tar.gz) a well establisched global alignment benchmark set published by Wilm et al. 2006 [doi:10.1186/1748-7188-1-19](https://almob.biomedcentral.com/articles/10.1186/1748-7188-1-19). Here you find the pairwiese subset (k2) of the BRAliBase. \
	2.) [shuffled ncRNAs data set](BRALIBASE-SHUFFLED.tar.gz) is produced by applying FASTA-shuffle-letters from the MEME \suite (Baileyet al., 2009) to all k2 sequences of the BRAliBase.\
- Artificial  data  set:\
	3.) [Artificial  data  set](./DB_random_seq_with_14000seq_and100seqlength0_5gc_content.tar.gz) a dataset of random sequences. This dataset contains 7000 FastA files as input for pairwiese alignments.\
- Local alignment benchmark set:\
	4.) [LocalBRAliBase](20150522_ModifiedBralibaseCon100.tar.gz) The LocalBRAliBase is a local alignment benchmark set constructed through us by extending the ncRNAs of the BRAliBase by its shuffled genomic context\
	5.) [shuffled LocalBRAliBase](20150522_ModifiedBralibaseShuffledCon100.tar.gz) The LocalBRAliBase dataset was also shuffled to construct random sequences, which should not be aligned.\
