;!define version "1.0.1" use /D if possible to pass in version info.
!include nsDialogs.nsh
!include MUI2.nsh

Name "NCRAR ABR (auditory wave analysis suite)"
OutFile "ncrar-abr-${version}.exe"
InstallDir "$LocalAppData\NCRAR-ABR-${version}"

RequestExecutionLevel user
ShowInstDetails show

Var /global key
;Var /global start_menu_folder

!define MUI_FINISHPAGE_NOAUTOCLOSE true

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "EULA.txt"
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_LANGUAGE "English"


Section ""
	SetOutPath $INSTDIR
	File /r "dist\ncrar-abr"

    WriteUninstaller "$INSTDIR\uninstall.exe"
    ; First, create key in registry that will show up in Add/Remove programs
    StrCpy $key "Software\Microsoft\Windows\CurrentVersion\Uninstall\NCRAR-ABR-${version}"
    WriteRegStr SHCTX $key "DisplayName" "NCRAR ABR ${version}"
    WriteRegStr SHCTX $key "DisplayIcon" "$INSTDIR\ncrar-abr\ncrar_abr\ncrar-abr.ico"
    WriteRegStr SHCTX $key "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
    WriteRegStr SHCTX $key "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
    DetailPrint "Wrote uninstall information to $key"

	createShortCut "$SMPROGRAMS\NCRAR ABR ${version}.lnk" "$INSTDIR\ncrar-abr\ncrar-abr.exe" "" "$INSTDIR\ncrar-abr\ncrar_abr\abr-icon.ico"
	DetailPrint "Created shortcut $SMPROGRAMS\NCRAR ABR ${version}.lnk"
SectionEnd

Section "uninstall"
	DetailPrint "Uninstalling $INSTDIR"
    StrCpy $key "Software\Microsoft\Windows\CurrentVersion\Uninstall\NCRAR-ABR-${version}"

    ; Remove uninstaller from registry so it doesn't show up under Add/Remove programs
  	DeleteRegKey SHCTX $key
	Delete "$SMPROGRAMS\NCRAR ABR ${version}.lnk"
	rmdir /r $INSTDIR
SectionEnd
