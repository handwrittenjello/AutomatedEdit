# AutomatedEdit
Project for automating editing down MMA Videos and creating scripts that make my life better


## MKVSplitter
This tool pulls data from the UFC PPV Fight Card that the user inputs and displays the main card results, location and even pulls the backdrop image and displays it as the background while you enter your split times.

## Front Banner
![Front Page Banner](https://res.cloudinary.com/handwrittenjello/image/upload/v1565476624/Front_Page_Banner.png "Front Page Banner")

## User Input Page
![User Input Page](https://res.cloudinary.com/handwrittenjello/image/upload/v1565476624/Data_Entry_Page.png "User Input Page")

### How to use MKV Splitter

## Prerequisites

Python 3
- `pip3 install subprocess`
- `pip3 install webbrowser`
- `pip3 install flask`
- `pip3 install requests`
- `pip3 install numpy`
- `pip3 install os`
- `pip3 install tmdbv3api`
- `pip3 install urllib`
- `pip3 install bs4`
- `pip3 install pandas`
- `pip3 install mkvmerge`


## How to use MKV Split
1. Move .mkv file to /flask
2. Run MKVSplit.py
3. Enter the card number and MKVSplit.py will pull the card information
4. Navigate to localhost:5000
5. Enter Filename in the input field
6. Enter the times of the fights into the user input (hhmmss)
7. Hit submit!
8. MKVSPlit will now run MKVMerge inthe background with the perscribed timeslots
9. The files will be renamed based on the fightcard information with the naming convention UFC (Card) - (Winner) vs (Loser)


# Batch Transcoding
The `batchEncodeWindows.py` file will scan your directory tree for **ALL** video files to transcode using HandbrakeCLI.  It uses a preset handbrake output template.  It will then move your files to a specific directory.

## Prerequisites
- `pip3 install os`
- `pip3 install subprocess`
- `pip3 install sys`
- `pip3 install shutil`
- HandbrakeCLI

## Set Up

1.  Set your root directory 
2.  Export your Handbrake preset temoplate file to `.`
3.  Update filename in script
4.  Add destination folder

Be mindful of the `/`'s and the `\`'s

![Transcode](https://res.cloudinary.com/handwrittenjello/image/upload/v1565526935/Handbrake_Instructions.jpg "Transcode")

