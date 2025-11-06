' processes.vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c color 0A & echo Processes Learning in Green! & timeout /t 2 > nul & color 0C & echo Processes Learning in Red! & timeout /t 2 > nul & color 0E & echo Processes Learning in Yellow! & timeout /t 2 > nul & color 0B & echo Processes Learning in Light Cyan! & timeout /t 2 > nul & color 0D & echo Processes Learning in Magenta! & timeout /t 2 > nul & color 0F & echo Done! & timeout /t 2 > nul", 1, False
