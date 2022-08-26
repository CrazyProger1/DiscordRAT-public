rmdir dist  /S /Q

pyinstaller -F -w main.py

rmdir build  /S /Q
del main.spec
echo [+] Succesefully built, saved to 'dist'