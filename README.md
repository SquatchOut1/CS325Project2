# Project 4 created by Alex Wernex and Zachery Linscott
This is a program to download the HTML page of a URL to a txt file as well as save the comments of a reddit post to a txt.

Afterwards, the comments of the reddit post are passed through a sentiment analysis NLP algorithm to determine if the comments
have a positive, negative, or neutral sentiment. 

The comments and the sentiment of each comment are then stored in sentiments.txt 
in CSV format.

## How to Use

Before you run the program, you may optionally change the names of the raw and processed output file. In run.py change:
```python
    rawFileName = 'HTMLOutput.txt'
    processedFileName = 'comments.txt'
```

Additionally, make sure to download the environment from requirements.yaml to make sure you have the appropriate libraries.

For this program, run in the terminal using python passing the reddit URL you wish to download as an argument ex: `python run.py https://old.reddit.com/r/mtg/comments/16msc6b/finished_a_game_at_130000_and_still_won_it/`

Also, make sure you ran the run.py with the old.reddit link. Otherwise the comments will not be in the file and it won't work.

For the TA: There is no API key to download or API to worry about. We did not use OpenAI or Bard due to a myriad of issues,
including the slowness of API calls. We used the textblob library for this project which is far more lightweight.
I reached out to the professor and he said this is ok.

## Sample Output

The attached CS325_p3/Data/raw/HTMLOutput.txt, CS325_p3/Data/processed/comments.txt, and  CS325_p3/Data/sentiments/sentiments.txt 
are all sample outputs using the url https://old.reddit.com/r/mildlyinfuriating/comments/17qr1qf/this_picture_sums_up_living_with_my_girlfriend/
