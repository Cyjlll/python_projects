from pywinauto.application import Application
from pywinauto import application
import autoit
import time
import pywinauto
from pywinauto.keyboard import send_keys

autoit.run("notepad.exe")
autoit.win_wait_active("[CLASS:Notepad]", 3)
autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
time.sleep(3)
autoit.win_close("[CLASS:Notepad]")
autoit.control_click("[Class:#32770]", "Button2")

# app=Application(backend='uia').start('control.exe')
# app=application.Application().connect(process=11272)

# app = application.Application().start(r"notepad.exe")
# app.UntitledNotepad.draw_outline()
# # app.UntitledNotepad.menu_select("编辑 -> &R")
# app['记事本'].print_control_identifiers()
