# Structure scoring effects for sankoff-like alignments

The idea is to invetigate structure scoring effects in sankoff-like alignments for local alignments. Local sequence alignments is known to have a negative expacted score. This negativ expacted score for randon sequences is needed to find the correct alignment boundarys and avoid any alignment-length score dependencies. 
Since the sturcture contribution for the score is almost always positive the score alignment-length dependence and the correct boundary detection would need to be investigated. 
This investigation is implemented by using a state of the art sankoff-like alignment LocARNA as a representatvie.

![grapical abstaract](./figure/graphical-abstract.svg)

This reposetory contains:
- [Local alignment benchmarksets](./benchmark_sets)
- [Some test data to quickliy check code using a local benchmankset](./test_data)
- [A analysis of free enegrys of random an ncRNAs](./FreeEnergy_analysis)
- [Notebooks for plotting the results](./analysis_notebooks)
- [analysiz data for different parameter combinations](./data)
- [Figures used in the publication](./figure)
- [Shuffeling lib](./lib)
- [Skripts](./skripts)
