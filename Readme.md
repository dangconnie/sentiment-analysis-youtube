# Sentiment Analysis on two Youtube videos using a YT web scraper and Seance.

### Youtube Web Scraper

http://ytcomments.klostermann.ca/

GitHub repo: https://github.com/philbot9/youtube-comment-scraper

### Seance
Crossley, S. A., Kyle, K., & McNamara, D. S. (2017). Sentiment analysis and social cognition engine (SEANCE): An automatic tool for sentiment, social cognition, and social order analysis. Behavior Research Methods 49(3), pp. 803-821. doi:10.3758/s13428-016-0743-z. [article](http://www.kristopherkyle.com/uploads/1/3/9/3/13935189/crossley_kyle_mcnamara_seance_2016.pdf)
​
http://www.kristopherkyle.com/seance.html

* Seance is not for commercial use

### VADER Sentiment Analysis Tool
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
https://github.com/cjhutto/vaderSentiment#python-code-example

### Youtube Links
1.[Sleepers Awake - Bach](https://www.youtube.com/watch?v=KyWOIKCtjiw)

2.[Every Heart (instrumental)](https://www.youtube.com/watch?v=U-JG47HsYvo)



-% needs to add to 1. can be indication something is wrong in data.
-had exceptionally high value for neutral in inuComments (144). counted extra spaces, quotation marks, brackets...

### Cmd line
-Split each comment in it's own file: 
    -- $ split -a3 -l1 inuComments.json output

    --Each resulting file is named "output" + combination of 3 letters after it. Start with line 1.

    ---Syntax: split [  -l LineCount ] [ -a SuffixLength ] [ File [ Prefix ] ]

-Seance only reads .txt files so loop through each file and add .text.
    -- $ for i in *; do mv "$i" "$i.txt"; done

-Split and .txt for both inu and bach files


holding onto split comments in case i need them again so that i don't have to redo it.