"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** ui.py                  user interface             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""

class UserInterface :
    def __init__(self, uiStyle="dialog") :
        self.__uiStyle = uiStyle
        if self.__uiStyle == "dialog" :
            from dialog import Dialog
            self.myInterface = Dialog(dialog='dialog', DIALOGRC=None,
                                      compat='dialog', use_stdout=None, *,
                                      autowidgetsize=True,
                                      pass_args_via_file=None)

### multi line text boxes
    def messageBox(self, message, kwargs[dialogtitle]) :
        result = myInterface.msgbox(message, height=None, width=None, kwargs)
        return result
    def textBox(self, filePath) :
        result = myInterface.textbox(filePath, height=None, width=None)
        return result
    def scrollBox(self, message, kwargs[dialogtitle]) :
        result = myInterface.scrollbox(message, height=None, width=None,
                                       kwargs)
        return result
    def texteditor(self, initialText, args[None, None], kwargs[dialogtitle]) :
        result = myInterface.editbox_str(initialText, height=None, width=None,
                                         args, kwargs)
        return result # returns a tuple (exitcode, text)
    def tailBox(self, filePath, kwargs[dialogtitle]) :
        myInterface.tailbox(filePath, height=None, width=None, kwargs)

### Displaying transient messages
    def announce(self, message, kwargs[dialogtitle]) :
        result = myInterface.infobox(message, height=None, width=None, kwargs)
    def countdown(self, message, timeOut, kwargs[dialogtitle]) :
        # timeOut is secs(int)
        result = myInterface.pause(message, height=None, width=None,
                                   timeOut, kwargs)

### progress indicators
    def progressbar(self, message, percent=0, kwargs[dialogtitle]) :
        myInterface.guage_start(message, height=None, width=None, percent,
                                kwargs)
        """ToDo: Create ProgressBarObject to enclose guage & guageupdate
           and to automatically call guagestop at 100%"""
    def progressbarUpdate(self, percent=10, message, updateMessage=False) :
        myInterface.guage_update(percent, message, updateMessage)
    def progressbarStop(self) :
        result = myInterface.guage_stop()
        return result
    def multiProgressbar(self, message, percent=0, elements=[],
                         kwargs[dialogtitle])
        result = myInterface.mixedguage(message, height=None, width=None,
                                        percent=0, elements, kwargs)
        """elements[] is a list of tuples consisting of (tag, value)
        possible values are:
        a percentage (-25 equals 25%) or
        Succeeded, Failed, Passed, Completed, Done, Skipped,
        In Progress, Checked, N/A"""
        """>> ToDo:
        Create an Object that automatically recalculates the total
        progress and resends the mixedguage command whenever one of the
        element values is changed"""
        return result

### lists
    def buidList(self, message, listheight, items[(tag, item, status)],
                 kwargs[dialogtitle]) :
        result = myInterface.buildlist(message, None, None, listheight,
                                       items, kwargs)
##        if result[0] = not

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
    def selectDir(self, rootDir, dialogtitle) :
        selectedDir = myInterface.dselect(rootDir, height=None,
                                              width=None, title=dialogtitle)
        if debugSwitch == True :
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
    def ynQuestion(self, question, buttons[yes_label="Yes" no_label="No"]):
        self.__ynQuestion = myInterface.yesno(question, height=None,
                                              width=None, buttons)

"""
#        elif self.__uiStyle == "html" :
#            ### generate html interface (template)
#            self.output = "<html>" #etc etc
########################################################################
#           self.dialog.exitcodes = ("0 DIALOG_OK", "1 DIALOG_CANCEL",
#                                    "-1 DIALOG_ESC", "-1 DIALOG_ERROR",
#                                    "3 DIALOG_EXTRA", "2 DIALOG_HELP",
#                                    "4 DIALOG_ITEM_HELP")
