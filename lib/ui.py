"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** ui.py                  user interface             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""


class UserInterface:
    def __init__(self, uiStyle = "dialog"):
        self.__uiStyle = uiStyle
        if self.__uiStyle == "dialog":
            from dialog import Dialog
            asterisk = "*"
            self.myInterface = Dialog(dialog=self.__uiStyle, DIALOGRC=None, compat=self.__uiStyle, use_stdout=None, autowidgetsize=True, pass_args_via_file=True)

### multi line text boxes
    def messageBox(self, message, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        height = None
        width = None
        result = myInterface.msgbox(message, height, width, kwargs)
        return result
    def textBox(self, filePath):
        height = None
        width = None
        result = myInterface.textbox(filePath, height, width)
        return result
    def scrollBox(self, message, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        height = None
        width = None
        result = myInterface.scrollbox(message, height, width, kwargs)
        return result
    def texteditor(self, initialText, args, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        args = [None, None]
        height = None
        width = None
        result = myInterface.editbox_str(initialText, height, width,
                                         args, kwargs)
        return result # returns a tuple (exitcode, text)
    def tailBox(self, filePath, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        height = None
        width = None
        myInterface.tailbox(filePath, height, width, kwargs)

### Displaying transient messages
    def announce(self, message, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        height = None
        width = None
        result = myInterface.infobox(message, height, width, kwargs)
    def countdown(self, message, timeOut, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        height = None
        width = None
        # timeOut is secs(int)
        result = myInterface.pause(message, height, width, timeOut, kwargs)

### progress indicators
    def progressbar(self, message, percent, dialogtitle):
        if percent == '':
            percent = 0
        kwargs['dialogtitle'] = dialogtitle
        height = None
        width = None
        myInterface.guage_start(message, height, width, percent, kwargs)
        """ToDo: Create ProgressBarObject to enclose guage & guageupdate
           and to automatically call guagestop at 100%"""
    def progressbarUpdate(self, percent, message, updateMessage=False):
        myInterface.guage_update(percent, message, updateMessage)
        if percent == '':
            percent = 10
    def progressbarStop(self):
        result = myInterface.guage_stop()
        return result
    def multiProgressbar(self, message, percent, elements, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        height = None
        width = None
        if percent == '':
            percent = 0
        result = myInterface.mixedguage(message, height, width,
                                        percent, elements, kwargs)
        """elements[] is a list of tuples consisting of (tag, value)
        possible values are:
        a percentage (-25 equals 25%) or
        Succeeded, Failed, Passed, Completed, Done, Skipped,
        In Progress, Checked, N/A"""
        """>> ToDo:
        Create an Object that automatically recalculates total_progress
        and resends the mixedguage command whenever one of the element
        values (and thereby total_progress) is changed"""
        return result

### lists
    def buidList(self, message, listheight, items, dialogtitle):
        # items[(tag, item, status)]
        kwargs['dialogtitle'] = dialogtitle
        height = None
        width = None
        result = myInterface.buildlist(message, height, width, listheight,
                                       items, kwargs)
        if result[0] != "DIALOG_OK":
            echo("oops, something went wrong...")

#    def checkList
#    def menu
#    def radioList
#    def treeView

### Single-line input fields
#    def inputBox
#    def inputMenu
#    def passwordBox

### Forms
#    def form
#    def mixedForm
#    def PasswordForm

### Selecting files and directories
    def selectDir(self, rootDir, dialogtitle):
        kwargs['dialogtitle'] = dialogtitle
        height = None
        width = None
        selectedDir = myInterface.dselect(rootDir, height, width, kwargs)
        if debugSwitch == True:
            debugLog += "selectDir returned %s and %s. \n" % (selectedDir[1],
                                                              selectedDir[2])
        return selectedDir

#    def selectFileDir(self, rootdir, dialogtitle)
#        return result

### Date and time
#    def calendarBox
#    def timeBox

### Miscellaneous
#    def rangeBox
    def ynQuestion(self, question, buttons, dialogtitle):
        if buttons['yes_label'] == '':
            buttons['yes_label'] = ui_language['yes']
        if buttons['no_label'] == '':
            buttons['no_label'] = ui_language['no']
        kwargs['dialogtitle'] = dialogtitle
        height = None
        width = None
        self.__ynQuestion = myInterface.yesno(question, height, width, buttons)

"""
#        elif self.__uiStyle == "html" :
#            ### generate html interface (template)
#            self.output = "<html>" #etc etc
########################################################################
#           self.dialog.exitcodes = ("0 DIALOG_OK", "1 DIALOG_CANCEL",
#                                    "-1 DIALOG_ESC", "-1 DIALOG_ERROR",
#                                    "3 DIALOG_EXTRA", "2 DIALOG_HELP",
#                                    "4 DIALOG_ITEM_HELP")
"""