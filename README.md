# All the Chandlers

Wikipedia lists sixteen Chandler locations in the United States. ([link](https://en.wikipedia.org/wiki/Chandler#Places)) Being interested in all things Chandler, I of course would like to visit them all. What's the fastest way? Hmm. Well, thankfully each page has a Latitude/Longitude combination listed. Scrape those, and check for the fastest combination? Why not?

# Naive Algorithm

Unforunately, the laws of computational complexity really came back to bite me here, with increasingly large numbers taking increasingly long amounts of time. Using the super-sophisticated method of commenting out some of the places and then running `time python3 chandler.py` I checked out times for some of the computations, listed below. I am not holding out for sixteen to finish before I die.

Number of Places | Time to Compute (seconds)
--- | ---
8 | 0.092
9 | 4.997
10 | 62.22
11 | 715.22

#### Implemented Caching of `distance_between`

Number of Places | Time to Compute (seconds)
--- | ---
9  | 1.287
10 | 15.476
11 | 180.30