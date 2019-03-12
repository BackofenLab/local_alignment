# Structure scoring effects for sankoff-like alignments

The idea is to invetigate structure scoring effects in sankoff-like alignments for local alignments. Local sequence alignments is known to have a negative expacted score. This negativ expacted score for randon sequences is needed to find the correct alignment boundarys and avoid any alignment-length score dependencies. 
Since the sturcture contribution for the score is almost always positive the score alignment-length dependence and the correct boundary detection would need to be investigated. 
This investigation is implemented by using a state of the art sankoff-like alignment LocARNA as a representatvie.

