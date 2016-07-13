if not exist .\output\java mkdir .\output\java
for /r .\input\ %%h in (*) do .\bin\protoc.exe .\input\%%~nh.proto --java_out=.\output\java