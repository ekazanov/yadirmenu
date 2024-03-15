
# Table of Contents

1.  [Yadirmenu](#orgf95e08b)
    1.  [What the "Yadirmenu" name means:](#orge66d351)
    2.  [Why:](#org7dcc0e4)
    3.  [What:](#org2f92bab)
    4.  [How:](#org2005707)
        1.  [Yadirmenu working logic](#org165791a)
        2.  [Customization Options](#org31818bb)
        3.  [Directory Metadata](#orga6d6223)
        4.  [Script Customization:](#orge9e9503)
    5.  [Requirements](#org18d4e81)
    6.  [Installation (using virtualenv)](#orgc611052)
    7.  [Invocation](#org8571146)
    8.  [Usage Tips](#org0521d85)
        1.  [Linux](#orgbbf4125)
        2.  [Termux](#org43330e5)


<a id="orgf95e08b"></a>

# Yadirmenu


<a id="orge66d351"></a>

## What the "Yadirmenu" name means:

"Yadirmenu" stands for "Yet Another Dirmenu."


<a id="org7dcc0e4"></a>

## Why:

The goal of creating Yadirmenu was to provide a simple menu interface
that can be run on different platforms as a frontend for user scripts
and/or documents.

Currently, Yadirmenu can be used on the following platforms:

-   Linux
-   Termux (Terminal for Android)
-   Possibly Windows (although it has not been tested)


<a id="org2f92bab"></a>

## What:

Yadirmenu is designed to create a menu for a set of user scripts and
documents. Given a directory tree, Yadirmenu generates a menu where
directories are represented as submenus and scripts are represented as
menu items.

With this menu, users can:

-   Navigate through menus and submenus.
-   Execute scripts represented as menu items.
-   Exit the menu.


<a id="org2005707"></a>

## How:


<a id="org165791a"></a>

### Yadirmenu working logic

The user creates a directory containing subdirectories for submenus
and scripts for menu items.

To run Yadirmenu, the user executes the command, specifying the menu
directory and interface type:

    yadirmenu --menu_dir "/path/to/menu/dir" --interface "Interface type"

where "Interface type" can be one of:

-   "MenuConsole": It uses the old, reliable plain console print/read interface.
-   "MenuDialog": It utilizes the console "Dialog" library.
-   "MenuTk": It employs the Tkinter Python GUI library.


<a id="org31818bb"></a>

### Customization Options

Yadirmenu offers customization options to tailor the menu appearance
and item names according to user preferences. These options are
defined within special files named ".META" located within each
directory.


<a id="orga6d6223"></a>

### Directory Metadata

Every directory can contain a ".META" file, which dictates the display
title and item names within the menu. The ".META" file structure is as
follows:

    TITLE="Menu/Documents"
    ITEM_NAME="Documents"

-   The "TITLE" value is used as a menu title line.
-   The "ITEM<sub>NAME</sub>" value is used as a submenumenu item name.

In the root directory the ".META" file contains the "TITLE" field
only.


<a id="orge9e9503"></a>

### Script Customization:

Script files can include a special line to customize the menu item
name:

    #MENU_ITEM_NAME="Menu item text"

-   The value of the "MENU<sub>ITEM</sub><sub>NAME</sub>" is used as a menu item name for
    the script.
-   If this line is not present, the script file name is used as the
    item name.

Naming Convention

Script and subdirectory names follow a specific format:

    "XX_script_file_name"

-   "XX" represents a number used for sorting menu items.


<a id="org18d4e81"></a>

## Requirements

-   python3
-   pythondialog
-   python-dotenv


<a id="orgc611052"></a>

## Installation (using virtualenv)

    mkdir yadirmenu
    cd yadirmenu
    git clone https://github.com/ekazanov/yadirmenu.git
    python3 -m venv ./venv
    source ./venv/bin/activate
    python3 -m pip install --upgrade pip
    cd yadirmenu; pip install .


<a id="org8571146"></a>

## Invocation

    cd yadirmenu
    source ./venv/bin/activate
    yadirmenu --menu_dir "/path/to/menu/dir" --interface "Interface type"


<a id="org0521d85"></a>

## Usage Tips


<a id="orgbbf4125"></a>

### Linux

On Linux, I bind a script starting Yadirmenu to some shortcut keys. My
favorite binding keys are "Alt-Ctrl-1". On Linux, I use the "MenuTk"
interface type.


<a id="org43330e5"></a>

### Termux

On Termux, I use a TermuxWidget to run the Termux console and a
"Yadirmenu". On Termux, I use the “MenuDialog” interface type.

