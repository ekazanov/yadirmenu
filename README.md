# Yadirmenu

## What the "Yadirmenu" name means:

"Yadirmenu" stands for "Yet Another Dirmenu."

## Why:

The goal of creating Yadirmenu was to provide a simple menu interface
that can be run on different platforms as a frontend for user scripts
and/or documents.

Currently, Yadirmenu can be used on the following platforms:

-   Linux
-   Termux (Terminal for Android)
-   Possibly Windows (although it has not been tested)


## What:

Yadirmenu is designed to create a menu for a set of user scripts and
documents. Given a directory tree, Yadirmenu generates a menu where
directories are represented as submenus and scripts are represented as
menu items.

With this menu, users can:

-   Navigate through menus and submenus.
-   Execute scripts represented as menu items.
-   Exit the menu.

## How:

### Yadirmenu working logic

The user creates a directory containing subdirectories for submenus
and scripts for menu items.

To run Yadirmenu, the user executes the command, specifying the menu
directory and interface type:

    yadirmenu --menu_dir "/path/to/menu/dir" --interface "Interface type"

where "Interface type" can be one of:

-   "MenuConsole": It uses the old, reliable plain console print/read interface.
-   "MenuConsoleDialog": It utilizes the console "Dialog" library.
-   "MenuTk": It employs the Tkinter Python GUI library.

### Customization Options

Yadirmenu offers customization options to tailor the menu appearance
and item names according to user preferences. These options are
defined within special files named ".META" located within each
directory.

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

## Requirements

### Python ###

-   python3
-   pythondialog
-   python-dotenv

### System ###

For MenuDialog the "dialog" package must be installed.

On Ubuntu one can install it using:

    apt-get install dialog

## Installation (using virtualenv)

    mkdir yadirmenu
    cd yadirmenu
    git clone https://github.com/ekazanov/yadirmenu.git
    python3 -m venv ./venv
    source ./venv/bin/activate
    python3 -m pip install --upgrade pip
    cd yadirmenu; pip install .

## Installation (termux)

    cd ~
    pkg install python
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    mkdir tmp
    cd tmp
    git clone https://github.com/ekazanov/yadirmenu.git
    python3 -m pip install --upgrade pip
    cd yadirmenu; pip install .
    rm -rf yadirmenu

## Invocation

    cd yadirmenu
    source ./venv/bin/activate
    yadirmenu --menu_dir "/path/to/menu/dir" --interface "Interface type"

## Usage Tips

### Linux

On Linux, I bind a script starting Yadirmenu to some shortcut keys. My
favorite binding keys are "Alt-Ctrl-1". On Linux, I use the "MenuTk"
interface type.

### Termux

On Termux, I use a TermuxWidget to run the Termux console and a
"Yadirmenu". On Termux, I use the “MenuDialog” interface type.
