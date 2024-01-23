# NetEase Cloud Music Data Analysis
NetEase Cloud Music Data Analysis is a program that can crawl and analyze NetEase Cloud song single comment areas or tags to generate visual information charts or word clouds.


## Function Characteristics

The main part of the program is GUI.py, which has the following functionalities:
1.	Scraping popular playlists and saving the information to a text file in the same directory.

2.	Analyzing the style tags of the popular playlists and generating visualizations in the form of bar charts and pie charts.

3.	Filtering playlists based on user-inputted style tags to find playlists that match the criteria.

4.	Scraping the names and IDs of all songs within a single playlist.

5.	Scraping and retrieving the hot comments for each song.

6.	Analyzing the popular comments by using the Jieba word segmentation tool to tokenize the comments, performing word frequency analysis, and generating a word cloud visualization.

7.	Scraping the popular singles of a singer along with their IDs.

8.	Implementing web page redirection to a personal leaderboard page.

9.	Implementing the scraping and downloading of all free songs within a playlist. 



## Install

1. Download or clone the project locally.
2. Install the required dependency libraries:
io, jason, sys, tkinter, jieba, collections, matplotlib, subprocess, requests, beautifulSoup4, urllib, lxml

## Usage Method
The beginning of the program is TheGUI.py, which includes the use of most functions. If you want to use certain functions separately, you can also run their separate Python files

(The download song function is not included in GUI.py, and the program DownloadSongs. py needs to be run separately.)

On the GUI operation page, the user is required to provide a playlist ID or artist ID, which can be accessed by opening the browser

## Attention
The GUI interface is not yet complete and prone to bugs, especially after clicking the return button

So it is not recommended to use all functions at once. You can stop running first and then run again

## Work demonstration video
https://www.bilibili.com/video/BV13X4y1p74N

