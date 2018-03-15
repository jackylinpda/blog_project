@echo off
cd C:\Users\bluewings\
call .\ENV2.7\Scripts\activate.bat
cd .\PycharmProjects\blog_project
fab deploy
pause

