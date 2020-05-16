#!/usr/bin/env python
import wget #import wget

#the lectures range from 1 to 24 so we loop through the range
for integer in range(1, 25):
    pdf_url = "http://web.mit.edu/6.857/OldStuff/Fall97/lectures/lecture{}.pdf".format(integer)
    download_location = "mitsec/lecture{}.pdf".format(integer)
    wget.download(pdf_url, download_location)
