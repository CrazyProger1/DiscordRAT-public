rmdir dist  /S /Q

pyinstaller -F -w main.py
copy "config.cnf" "dist/config.cnf"


rmdir build  /S /Q
del main.spec