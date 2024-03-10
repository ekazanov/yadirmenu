#! /usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = "Evgeny Kazanov"

import sys
from yadirmenu.yadirmenu import menu_obj_fabric
from yadirmenu.yadirmenu import ProcessMenu

def main():
    MENU_TYPE = 'MenuConsole'
    MENU_TYPE = 'MenuConsoleDialog'
    # MENU_TYPE = 'MenuTk'

    menu_obj = menu_obj_fabric(MENU_TYPE)
    menu_path = "/home/evgeny/projects/132_yadirmenu/src/menu_test"
    process_menu = ProcessMenu(menu_root_path=menu_path,
                           menu_object=menu_obj)

    sys.exit(0)
