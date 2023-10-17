# Reddit Comments

This is a program to download the HTML page of a URL to a txt file as well as save the comments of a reddit post to a txt.

## How to Use

Before you run the program, you may optionally change the names of the raw and processed output file. In run.py change:
```python
    rawFileName = 'HTMLOutput.txt'
    processedFileName = 'comments.txt'
```

Additionally, make sure to download the environment from requirements.yaml to make sure you have the appropriate libraries.

For this program, run in the terminal using python passing the reddit URL you wish to download as an argument ex: `python run.py https://old.reddit.com/r/mtg/comments/16msc6b/finished_a_game_at_130000_and_still_won_it/`

Also, make sure you ran the run.py with the old.reddit link. Otherwise the comments will not be in the file and it won't work.

## Sample Output

The attached CS325_p3/Data/raw/HTMLOutput.txt is a sample output using the url https://old.reddit.com/r/mtg/comments/16msc6b/finished_a_game_at_130000_and_still_won_it/

The attached CS325_p3/Data/processed/comments.txt is a sample output using the url https://old.reddit.com/r/mtg/comments/16msc6b/finished_a_game_at_130000_and_still_won_it/
