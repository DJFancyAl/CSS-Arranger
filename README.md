# CSS-Arranger

## Purpose

If you've every worked on a large web project, requiring a lot of CSS, then you understand how dizzying your CSS stylesheets can become. You have elements, classes, IDs, and more that have been styled. Most of the time this will not effect the way your site or app runs. However, it can create a lot of headaches when developing, troubleshooting, or reviewing your code.

To solve this problem we have the simple __"CSS Arranger"__. This script will take your existing stylesheet and reformat it so that items are sequenced based on their type and alphabetically. So instead of having a chaotic CSS file you will have one with a clean and repeatable structure like this:

1. __IDs__

    * Element with ID = A
    * Element with ID = B
    * Element with ID = C
    
2. __Classes__

    * Element with Class = A
    * Element with Class = B
    * Element with Class = C

3. __Other Elements__

    * Element Name = A
    * Element Name = B
    * Element Name = C

Ahhhh...isn't that much neater and more organized?

## Setup

For the __CSS Arranger__ to work a couple of things must be true:

1. You must be using it on an existing _.css_ file which is filled with your styling. This script does not create any new files.
2. The CSS file must be formatted correctly (brackets must be closed, semicolons must be used, etc.) This script will not correct errors in the old stylesheet.
3. You __MUST__ create a backup of your stylesheet before running this script on it. At a minimum you should paste the contents of your stylesheet into a text file before running the script. This way you can revert to your old stylesheet if the new one is formatted incorrectly.

## Arrange Your CSS

> __If you would like to test the script then you may try it with the included _styles.css_ file first__

If you've completed the setup above, then you may proceed with rearranging your CSS stylesheet. To start the script - double click on the _Arrange_CSS.py_ file or start it from the command line using Python. Your command should look like:

`python3 Arrange_CSS.py` or `py Arrange_CSS.py`

The script should open and it will ask for your input: _File Location:_ This must be the absolute path of the CSS file your are formatting. ONLY IF YOu ARE ABSOLUTELY SURE YOU WANT TO CHANGE THE FILE then you may press _Enter_. The script will run and it will reformat your stylesheet. Open the CSS file and confirm that it is formatted correctly.
