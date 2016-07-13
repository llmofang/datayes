if not exist .\output\python mkdir .\output\python
for /r .\input\ %%h in (*) do .\bin\protoc.exe .\input\%%~nh.proto --python_out=.\output\python