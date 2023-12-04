# Project 6 created by Alex Wernex and Zachery Linscott
This is a program to download the HTML pages of multiple URLs pointing to Reddit posts.
Each URL is read from a file that the user of the program provides a path to.

The raw HTML of each URL is then put into separate files, then from there each file
is cleaned of the HTML to extract the comments from the subreddit.

Once each file is cleaned, these comments are then stored cleanly into yet more files 
which are unique to each Reddit post.

Next, the comments files are scanned and sentiment analysis is performed on each comment.
Once the sentiments are gathered, they are also put into their own files, again unique for each
Reddit post.

Finally, each sentiment file is then put into its own bar graph where the user can visually see
the number of positive, negative, and neutral comments. These graphs appear and are stored in 
the plots folder as well, located in Data.

## How to Use

1. Ensure you are in the correct directory.

2. Make sure to download the environment from requirements.yaml to make sure you have the appropriate libraries.

3. Run in the terminal using python passing the file of urls you wish to gather comments from
4. as an argument, e.g.: `python run.py yourfilepath/yourfilename`

Also, make sure you ran the run.py with the old.reddit link for each one. Otherwise the comments will not be in the file and it won't work.

For the TA: There is no API key to download or API to worry about. We did not use OpenAI or Bard due to a myriad of issues,
including the slowness of API calls. We used the textblob library for this project which is far more lightweight.
I reached out to the professor and he said this is ok.

## Sample Output

The attached CS325_p3/Data/raw/HTMLOutput files, CS325_p3/Data/processed/comments files, CS325_p3/Data/sentiments/sentiments, and CS325_p3/Data/Plots/graphs files 
are all sample outputs.
