Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "path\to\your\screenshot.bat\file" & Chr(34), (0)
Set WshShell = Nothing