' info.vbs
Dim objWMIService, colItems, objItem
Dim cores, threads

Set objWMIService = GetObject("winmgmts:\\.\root\CIMV2")
Set colItems = objWMIService.ExecQuery("Select * from Win32_Processor")

For Each objItem in colItems
    cores = objItem.NumberOfCores
    threads = objItem.NumberOfLogicalProcessors
Next

MsgBox "Hi! This is your computer's core number: " & cores & vbCrLf & "Thread number: " & threads, vbInformation, "Core and Thread Info"
