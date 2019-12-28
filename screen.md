# Screen 
It is a terminal multiplixer for linux. It helps users to have multiple screens and windows running on the terminal. Users can switch easliy between screens and windows.
[https://www.youtube.com/watch?v=I4xVn6Io5Nw]

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

## Create a new window
> Ctrl+a + c

## List windows
> Ctrl+a + w

## switch between windows
### get next window
> Ctrl+a + n
### get previous window
> Ctrl+a + p
### get specific window
> Ctrl+a + windows_number
### show all windows to select from
> Ctrl+a + "

## rename window
> Ctrl+a + A
## kill screen window[will kill the screen if this is the last window]
> Ctrl+a + k

## show windows side by side
### divide screen vertically 
> Ctrl+a + |
### divide screen horizontally
> Ctrl+a + S
### move between panes
> Ctrl+a + Tab
### list windows to select from
> Ctrl+a + w
### close a panes
> Ctrl+a + X

## lock screen
> Ctrl+a + x

## help
> screen ?