import sys
import os
import glob
import fileinput
from re import sub
from dotenv import dotenv_values
import time

menu_path = "/home/evgeny/projects/132_dirmenu/src/menu_test"


class MenuBase:

    def menu(self, title: str,
                  menu_data: list[tuple[str, str]])->int:
        tags = []
        self.title = title
        self.menu_data = menu_data
        for tag, _  in menu_data:
            tags.append(tag)
        tags.append('0')
        while True:
            user_input = self.draw_menu()
            if user_input not in tags:
                continue
            return int(user_input)


class MenuTk(MenuBase):

    def __init__(self):
        self.return_tag = '0'

    def draw_menu(self):
        from pymenu import Action
        from pymenu import ButtonsFabric
        WIDTH = 50
        HEIGHT = 1
        BG = "white"
        FG = "black"
        XPOZ = 400
        YPOZ = 100
        self.bf = ButtonsFabric(xpoz=XPOZ,ypoz=YPOZ,width=WIDTH,height=HEIGHT,
                   bg=BG,fg=FG)
        self.bf.use_return = False
        self.bf.title = self.title
        for tag, text in self.menu_data:
            action_obj = Action(tag, self.bf, self)
            self.bf.add_button(text, action_obj.do_action)
        action_obj = Action('0', self.bf, self)
        self.bf.add_button('Exit', action_obj.do_action)
        self.bf.finalize()
        self.bf.root.destroy()
        print(f"self.return_tag = {self.return_tag}")
        return self.return_tag


class MenuConsoleDialog(MenuBase):

    def __init__(self):
        from dialog import Dialog
        self.d_obj = Dialog(dialog="dialog")
        self.title = ""
        self.menu_data = []

    def draw_menu(self):
        code, tag = self.d_obj.menu(self.title, choices=self.menu_data)
        if code == "cancel":
            return '0'
        return tag

class MenuConsole(MenuBase):

    def __init__(self):
        self.title = ""
        self.menu_data = []

    def clear_screen(self):
        print("\033[H\033[2J", end="")

    def draw_menu(self):
        self.clear_screen()
        print(f"\n\t\t{self.title}")
        print("\t--------------------")
        for tag, item_name in self.menu_data:
            print(f"\t{tag}: {item_name}")
        print("\t--------------------")
        user_input = input("\tEnter a number or 'q' to quit: \n")
        if user_input == 'q':
            self.clear_screen()
            return '0'
        return user_input


class ProcessMenu:

    def __init__(self, menu_root_path: str, menu_object):
        self.menu_root_path = menu_root_path
        self.menu_obj = menu_object
        # "" If it is menu root dir
        # "parent dir" if it is not
        self.menu_parent_dir = ""
        # [(item_type, tag, item_name, file_name)]
        # - dir path - "d" in case of submenu or parent dir, "f" if file
        # tag - number (int)
        # Item name
        self.menu_data = []
        self.title = "Menu system"
        meta = self.read_meta(self.menu_root_path)
        self.title = meta.get("TITLE", "Menu")
        self.read_menu_dir(self.menu_root_path)
        while True:
            menu_data = []
            for _, tag, item_name, _ in self.menu_data:
                menu_data.append((str(tag), item_name))
            tag = self.menu_obj.menu(self.title, menu_data)
            if tag == 0:
                sys.exit(0)
            else:
                self.action(tag)

    def remove_number_from_menu_item(self, menu_item):
        corrected_item = sub('^[0-9][0-9]_', "", menu_item)
        return corrected_item

    def get_menu_item_from_file(self, fname):
        item_name = ""
        prefix = "#MENU_ITEM_NAME="
        for line in fileinput.input([fname]):
            line = line.strip()
            if line.startswith(prefix):
                item_name = line.replace(prefix, "").strip("\"")
        if not item_name:
            item_name = fname.rsplit(os.sep, 1)[-1]
            item_name = self.remove_number_from_menu_item(item_name)
        return item_name

    def get_menu_item_from_dir(self, dname):
        meta = self.read_meta(dname)
        dir_item_name = dname.rsplit(os.sep, 1)[-1]
        item_name = meta.get("ITEM_NAME", dir_item_name)
        return item_name

    def read_menu_dir(self, menu_dir, first_tag=1):
        fnames_arr = glob.glob(os.path.join(menu_dir, "*"))
        fnames_arr.sort()
        # Create a self.menu_data for a current path
        tag = first_tag
        for fname in fnames_arr:
            item_type = ""
            item_name = ""
            if os.path.isdir(fname):
                item_type = "d"
                item_name = self.get_menu_item_from_dir(fname)
                item_name = self.remove_number_from_menu_item(item_name)
                item_name = "-> " + item_name
            else:
                item_type = "f"
                item_name = self.get_menu_item_from_file(fname)
            item_name = self.remove_number_from_menu_item(item_name)
            data_element = (item_type, tag, item_name, fname)
            self.menu_data.append(data_element)
            tag += 1

    def read_meta(self, dir_path):
        meta = dotenv_values(os.path.join(dir_path, ".META"))
        return meta

    def change_current_dir(self, tag):
        menu_data_element = self.menu_data[int(tag) - 1]
        _, tag, _, file_name = menu_data_element
        meta = self.read_meta(file_name)
        self.title = meta.get("TITLE", "NoMenuTitle")
        self.menu_data = []
        if file_name == self.menu_root_path:
            self.menu_parent_dir = ""
        else:
            self.menu_parent_dir, _ = os.path.split(file_name)
        if self.menu_parent_dir:
            data_element = ("d", 1, "..", self.menu_parent_dir)
            self.menu_data.append(data_element)
            self.read_menu_dir(file_name, first_tag=2)
        else:
            self.read_menu_dir(file_name, first_tag=1)

    def action(self, tag):
        menu_data_element = self.menu_data[int(tag) - 1]
        item_type, tag, _, file_name = menu_data_element
        if item_type == "d":
            self.change_current_dir(tag)
        if item_type == "f":
            os.system(file_name)
            time.sleep(5)


def menu_obj_fabric(menu_class):
    if menu_class == 'MenuConsole':
        return MenuConsole()
    if menu_class == 'MenuConsoleDialog':
        return MenuConsoleDialog()
    if menu_class == 'MenuTk':
        return MenuTk()
    return None


# MENU_TYPE = 'MenuConsole'
# MENU_TYPE = 'MenuConsoleDialog'
MENU_TYPE = 'MenuTk'

menu_obj = menu_obj_fabric(MENU_TYPE)
process_menu = ProcessMenu(menu_root_path=menu_path,
                           menu_object=menu_obj)

sys.exit(0)
