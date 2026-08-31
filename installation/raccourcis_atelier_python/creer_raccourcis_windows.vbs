' =========================================================
'  Creation des raccourcis "Atelier Python" (Windows)
'  - IDLE, ouvert directement dans le dossier de l'atelier
'  - Invite de commande, ouverte dans le meme dossier
'
'  A LANCER UNE FOIS PAR POSTE : double-cliquer sur ce fichier.
'  Le dossier de travail est cree automatiquement sur le
'  Bureau de l'utilisateur si besoin :  Bureau\Atelier Python
' =========================================================

Set WshShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")

strDesktop  = WshShell.SpecialFolders("Desktop")
strWorkDir  = strDesktop & "\Atelier Python"
strWindir   = WshShell.ExpandEnvironmentStrings("%WINDIR%")

' 1) Creation du dossier de travail s'il n'existe pas encore
If Not FSO.FolderExists(strWorkDir) Then
    FSO.CreateFolder(strWorkDir)
End If

' 2) Raccourci vers IDLE (le lanceur "py" est installe par defaut
'    avec Python, dans le dossier Windows, meme si la case
'    "Add to PATH" n'a pas ete cochee)
Set oIDLE = WshShell.CreateShortcut(strDesktop & "\IDLE - Atelier.lnk")
oIDLE.TargetPath       = strWindir & "\pyw.exe"
oIDLE.Arguments        = "-m idlelib"
oIDLE.WorkingDirectory = strWorkDir
oIDLE.IconLocation     = strWindir & "\pyw.exe, 0"
oIDLE.Description      = "Ouvrir IDLE dans le dossier de l'atelier"
oIDLE.Save

' 3) Raccourci vers l'invite de commande, positionnee dans le
'    dossier de l'atelier, avec Python deja lance (py)
Set oCMD = WshShell.CreateShortcut(strDesktop & "\Terminal Python - Atelier.lnk")
oCMD.TargetPath       = strWindir & "\System32\cmd.exe"
oCMD.Arguments        = "/k py"
oCMD.WorkingDirectory = strWorkDir
oCMD.Description      = "Ouvrir une invite Python dans le dossier de l'atelier"
oCMD.Save

MsgBox "C'est fait !" & vbCrLf & vbCrLf & _
       "Deux raccourcis ont ete crees sur le Bureau :" & vbCrLf & _
       "  - IDLE - Atelier" & vbCrLf & _
       "  - Terminal Python - Atelier" & vbCrLf & vbCrLf & _
       "Dossier de travail utilise :" & vbCrLf & strWorkDir, _
       vbInformation, "Raccourcis Atelier Python"
