# AutomatedEdit
Project for automating editing down MMA Videos and creating scripts that make my life better


## MKVSplitter
This tool pulls data from the UFC PPV Fight Card that the user inputs and displays the main card results, location and even pulls the backdrop image and displays it as the background while you enter your split times.

Start the 
## Card Information Input

![Front Page Banner](https://res.cloudinary.com/handwrittenjello/image/upload/v1565807832/Input_Page.png "Front Page Banner")

## Fight Input Page
![User Input Page](https://res.cloudinary.com/handwrittenjello/image/upload/v1565476624/Data_Entry_Page.png "User Input Page")

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
2. Run Input.py
	-At the bottom of the page, the previous 15 cards are displayed
	For:
	-PPV: Enter the ppv number `241`
	-UFC on ESPN: enter the name of the card as it appears `Covington vs. Lawler`
	-UFC Fight Night: enter the name of the card as it appears `de Randamie vs. Ladd`
3. Enter the times of the fights into the user input (hhmmss)
4. Enter the filename of the card
5. Hit submit!
6. MKVSPlit will now run MKVMerge inthe background with the perscribed timeslots
7. The files will be renamed based on the fightcard information with the naming convention UFC (Card) - (Winner) vs (Loser)




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

