__author__ = "Evgeny Kazanov"

import argparse
import sys

from yadirmenu.yadirmenu import ProcessMenu, menu_obj_fabric


def process_args():
    choices = ["MenuConsole", "MenuConsoleDialog", "MenuTk"]
    parser = argparse.ArgumentParser(description="Roulette startegy testing program.")
    parser.add_argument(
        "--menu_dir",
        "-m",
        type=str,
        required=True,
        metavar="STRING",
        help="Wallet start amount",
    )
    parser.add_argument(
        "--interface",
        "-i",
        type=str,
        required=False,
        default="MenuConsoleDialog",
        choices=choices,
        metavar="STRING",
        help="Inteface type. Allowed values: " + ", ".join(choices),
    )
    args = parser.parse_args()
    return args


def main():
    args = process_args()
    menu_obj = menu_obj_fabric(args.interface)
    process_menu = ProcessMenu(menu_root_path=args.menu_dir, menu_object=menu_obj)
