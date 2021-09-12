function getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

$IP = getIP
$USER = $env:USERNAME
$NAME = $env:ComputerName
$VERSION = $HOST.Version
$DATE = Get-Date  -Format "dddd, MM/dd/yyyy"


$Body = "This machine's IP is $IP. User is $User. Hostname is $NAME. PowerShell Version $VERSION. Today's Date is $DATE."
write-host("$Body")
Send-MailMessage -To "eddieb2332@gmail.com" -From "eddieb2332@gmail.com" -Subject "IT3038c" -Body $Body -SmtpServer smtp.gmail.com -port 587 -UseSSL  -Credential (Get-Credential)