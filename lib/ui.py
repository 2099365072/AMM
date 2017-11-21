#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** ui.py                  user interface             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#           self.dialog.exitcodes = ("0 DIALOG_OK", "1 DIALOG_CANCEL",
#                                    "-1 DIALOG_ESC", "-1 DIALOG_ERROR",
#                                    "3 DIALOG_EXTRA", "2 DIALOG_HELP",
#                                    "4 DIALOG_ITEM_HELP")
###TODO### check Lynda vid 1203 & 1204!!!!

class UserInterface:
    def __init__(self, uiStyle="dialog"):
        self.__uiStyle = uiStyle
        if self.__uiStyle == "dialog":
            from dialog import Dialog
            self.myInterface = Dialog(dialog=self.__uiStyle,
                                      DIALOGRC="./dialog.rc",
                                      compat=self.__uiStyle, use_stdout=None,
                                      autowidgetsize=True,
                                      pass_args_via_file=True)
        else:
            raise TypeError('Other ui styles are not available yet, need to \
                            use dialog for now')
##############################################################################
    @classmethod
    def ui_builder(self, dialogtype, **kwargs):
        from collections import namedtuple
        dialogtypes = dict(message = "msgbox",
                           textbox = "textbox",
                           text_editor = "editbox_str",
                           announce = "infobox",
                           countdown = "pause",
                           progress_bar = "guage_start",
                           progress_bar_update = "guage_update",
                           progress_bar_stop = "guage_stop",
                           multi_progress_bar = "mixedguage",
                           build_list = "buildlist",
                           checklist = "checklist",
                           radiolist = "radiolist",
                           inputbox = "inputbox",
                           inputmenu = "inputmenu",
                           passwordbox = "passwordbox",
                           form = "form",
                           selectdir = "dselect",
                           selectfd = "fselect",
                           yn_question = 'yesno'
                           )
        dependencies = namedtuple('dependencies',
                                    ['name', 'text', 'title', 'path', 'ok',
                                     'cancel', 'extra', 'yes', 'no']
                                  )
    @classmethod
    def message_box(self, message, title):
        result = myInterface.msgbox(message, title)
        return result
    @classmethod
    def text_box(self, filePath):
        result = myInterface.textbox(filePath)
        return result
    @classmethod
    def text_editor(self, initialText, args, title):
        args = [None, None]
        result = myInterface.editbox_str(initialText, args, title)
        return result # returns a tuple (exitcode, text)
    @classmethod
    def announce(self, message, title):
        result = myInterface.infobox(message, title)
        return result
    @classmethod
    def countdown(self, message, timeOut, title):
        # timeOut is secs(int)
        result = myInterface.pause(message, timeOut, title)
        return result
##############################################################################

##############################################################################
    @classmethod
    def progressbar(self, bar_type, message, percent, title, **kwargs):
        pass
    @classmethod
    def progress_bar(self, message, percent, title): #
        if percent == '':
            percent = 0
        myInterface.guage_start(message, percent, title)
    @classmethod
    def progress_bar_update(self, percent, message, updateMessage=False): #
        myInterface.guage_update(percent, message, updateMessage)
        if percent == '':
            percent = 10
    @classmethod
    def progress_bar_stop(self): #
        result = myInterface.guage_stop()
        return result
    @classmethod
    def multi_progress_bar(self, message, percent, elements, title): #
        if percent == '':
            percent = 0
        result = myInterface.mixedguage(message, percent, elements, title)
        # elements[] is a list of tuples consisting of (tag, value)
        #   possible values are:
        #   a percentage (-25 equals 25%) or
        #   Succeeded, Failed, Passed, Completed, Done, Skipped,
        #   In Progress, Checked, N/A
        # ToDo:
        #   Create an Object that automatically recalculates
        #   total_progress and resends the mixedguage command
        #   whenever one of the element values (and thereby
        #   total_progress) is changed
        return result
##############################################################################

##############################################################################
    @classmethod
    def form(self, fields):
        #(fieldname, default_value, fieldlength=32)
        numfields = len(fields)
        #if numfields == 0:
        #    raise TypeError('form expected at least 1 field, got \
        #    {}.'.format(numfields)

        #except ValueError as error:
           #print("fields cannot be 0")
        #elif fieldname == 0:
        #    fieldlength = 32
        if numfields > 8: cols = 2
        else: cols = 1
        col = 1
        row = 1
        for fieldname in fields:
            if row > rows / cols:
                col = 2
                row = row - rows // cols
            elements.append(fieldname, row, col, )
##############################################################################

##############################################################################
    @classmethod
    def list_builder(self, message, items, title):
        pass
    @classmethod
    def build_list(self, message, items, title): #
        # items[(tag, item, status)]
        listheight = None
        result = myInterface.buildlist(message, listheight, items, title)
        if result[0] != "DIALOG_OK":
            print("oops, something went wrong...")
        else:
            return result[1]
    @classmethod
    def check_list(self, message, choices, title): #
        # choices[(tag, item, status)]
        listheight = None
        result = myInterface.checklist(message, listheight, choices, title)
        if result[0] != "DIALOG_OK":
            print("oops, something went wrong...")
        else:
            return result[1]
    @classmethod
    def radio_list(self, message, choices, title): #
        # choices[(tag, item)] where tag = shortname, item = description
        list_height = None
        result = myInterface.menu(message, list_height, choices, title)
        if result[0] != "DIALOG_OK":
            print("oops, something went wrong...")
        else:
            return result[1]
##############################################################################

##############################################################################
    def select_dir(self, rootDir, title):
        selectedDir = myInterface.dselect(rootDir, title)
        if debug_switch == True:
            debugLog += "selectDir returned %s and %s. \n" % (selectedDir[1],
                                                              selectedDir[2])
        return selectedDir
    def yn_question(self, question, buttons, title):
        if buttons['yes_label'] == '':
            buttons['yes_label'] = ui_language['yes']
        if buttons['no_label'] == '':
            buttons['no_label'] = ui_language['no']
        result = myInterface.yesno(question, buttons, title)
        return result
##############################################################################

def main():
    """just in case somebody wants to test this file by itself"""
    print("It works!!! ;-)")
    ###TODO### do something with the various methods/functions of this file

# standard boilerplate
if __name__ == '__main__':
    main()
