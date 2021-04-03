Gui, Add, Text, x17 y8 w120 h20, Courses: 
Gui, Add, Text, x17 yp+30 wp hp, Your Year of birth (yyyy): 
Gui, Add, Edit, xp+140 y8 w100 hp vName, Name 
Gui, Add, Edit, xp yp+30 wp hp vYear, yyyy 
Gui, Add, Button, x27 y68 w70 hp gOK, OK 
Gui, Add, Button, xp+150 yp wp hp gCancel, Cancel 
Gui, Show, x279 y217 h98 w277 
return 

Cancel: 
GuiClose: 
ExitApp 

OK:
Gui, Submit
^!s:: 
Send Hello World!
return
ExitApp
