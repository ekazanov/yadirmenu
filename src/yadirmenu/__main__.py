__author__ = "Evgeny Kazanov"

import sys
import argparse

from yadirmenu.yadirmenu import menu_obj_fabric
from yadirmenu.yadirmenu import ProcessMenu

def process_args():
    choices = ["MenuConsole", "MenuConsoleDialog", "MenuTk"]
    parser = argparse.ArgumentParser(description='Roulette startegy testing program.')
    parser.add_argument('--menu_dir', "-m", type=str, required=True,
                        metavar='STRING', help="Wallet start amount")
    parser.add_argument('--interface', "-i", type=str,  required=False,
                        default="MenuConsoleDialog",
                        choices=choices,
                        metavar='STRING', help="Inteface type. Allowed values: " \
                        + ", ".join(choices))
    args = parser.parse_args()
    print(f"args = {args}")
    return args

def main():
    args = process_args()

    print("main()")
    print(f"args = {args}")
    MENU_TYPE = 'MenuConsole'
    MENU_TYPE = 'MenuConsoleDialog'
    MENU_TYPE = 'MenuTk'

    # menu_obj = menu_obj_fabric(MENU_TYPE)
    menu_obj = menu_obj_fabric(args.interface)
    menu_path = "/home/evgeny/projects/132_yadirmenu/src/menu_test"
    # process_menu = ProcessMenu(menu_root_path=menu_path,
    #                        menu_object=menu_obj)
    process_menu = ProcessMenu(menu_root_path=args.menu_dir,
                           menu_object=menu_obj)
