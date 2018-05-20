# All the Chandlers

Wikipedia lists sixteen Chandler locations in the United States. ([link](https://en.wikipedia.org/wiki/Chandler#Places)) Being interested in all things Chandler, I of course would like to visit them all. What's the fastest way? Hmm. Well, thankfully each page has a Latitude/Longitude combination listed. Scrape those, and check for the fastest combination? Why not?

Unforunately, the laws of computational complexity really came back to bite me here, with increasingly large numbers taking increasingly long amounts of time. Using the super-sophisticated method of commenting out some of the places and then running `time python3 chandler.py` I checked out times for some of the computations, listed below. I am not holding out for sixteen to finish before I die.

Number of Places | Time to Compute (seconds
--- | ---
7 | 0.092
8 | 4.997
9 | 62.22
10 | Currently running