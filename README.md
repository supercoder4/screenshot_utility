# Screenshot Utility
Simple yet amazing python based screenshot capture tool in the taskbar tray of your system.

When the script runs, an icon will show in the taskbar tray. Single click on this icon will capture the screenshot.

Screenshots will be saved in C:\Screenshots folder\. Captured screenshot are stored smartly in  C:\Screenshots\current_date\ where current_date is generated dynamically. The name of the screenshot is the time stamp when it was captured.

To stop the utility, right click on the icon in taskbar tray and then click on 'EXIT'.

For windows:

Create a virtual environment using commad: 
        
    python -m venv venv
        
Install required packages with:

    pip install -r requirements.txt
    
Finally run the screenshot script:
    
    python screenshot.py
    
Note:

If you want to run this script at windows startup, just put screenshot.bat file in startup folder of your computer. This will run the script automatically each time your system starts/restarts.

If you dont want the command propmt to be opened each time this script runs automatically, just put screenshot.vbs file in startup folder of your computer (also remove screenshot.bat file from startup folder if had had put it earlier).



 
    
