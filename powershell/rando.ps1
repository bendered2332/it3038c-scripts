﻿$RANDO=0 

$LogFile = "c:\logs\rando.log"
clear-content $LogFile
for($i=0; $i -lt 5; $i++){ 

    $RANDO=Get-Random -Maximum 1000 -Minimum 1 

    Write-Host($RANDO) 
    Add-Content $LogFile "INFO: Random number is ${RANDO}"


} 
