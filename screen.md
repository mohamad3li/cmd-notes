# Screen 
It is a terminal multiplixer for linux. It helps users to have multiple screens and windows running on the terminal. Users can switch easliy between screens and windows.

## Installation
To install screen on Ubuntu, we need to run the following command line
> apt-get screen

## Start new screen
> screen [-S screen_name]

## List running screens
> screen -ls

## Detach from screen session
> Ctrl+a + d

## Retach to screen
> screen -r [screen_name|process_number]

## send command to a screen
> screen -X -S [screen_name|process_number] [command|e.g quit]

## kill screen window
>Ctrl+a + k