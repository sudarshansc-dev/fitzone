$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\Desktop\NOVA.lnk")
$Shortcut.TargetPath = "$env:USERPROFILE\NOVA\project\start_nova.bat"
$Shortcut.WorkingDirectory = "$env:USERPROFILE\NOVA\project"
$Shortcut.IconLocation = "$env:USERPROFILE\NOVA\project\nova_icon.ico"
$Shortcut.Description = "NOVA Voice Assistant"
$Shortcut.Save()
Write-Host "NOVA shortcut created on your Desktop!" -ForegroundColor Green
