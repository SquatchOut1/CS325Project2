# HTMLDownload

This is a program to download the HTML page of a URL to a txt file.

## How to Use

Before you run the program, make sure to change the filepath to your desired location for the output txt file.
```python
    filepath = "INSERT YOUR PATH HERE"
```

For this program, run in the terminal using python passing the URL you wish to download as an argument ex: `python HTMLDownload.py https://www.example.com`

## Sample Output

The attached HTMLOutput is a sample output using the url https://old.reddit.com/r/mtg/comments/16msc6b/finished_a_game_at_130000_and_still_won_it/

# extract_comments

This is a program to extract the comments from a reddit page using a txt file of html as input.

## How to Use

Before you run the program, make sure to change the output filepath to your desired location for the output txt file.
```python
    outputFilePath = "INSERT YOUR PATH HERE"
```
Also, make sure you ran the HTMLDownload with the old.reddit link. Otherwise the comments will not be in the file and it won't work.

For this program, run in the terminal using python passing the HTMLOutput.txt you wish to download as an argument ex: `python extract_comments.py HTMLOutput.txt`

## Sample Output

The attached comments.txt is a sample output using the url https://old.reddit.com/r/mtg/comments/16msc6b/finished_a_game_at_130000_and_still_won_it/
