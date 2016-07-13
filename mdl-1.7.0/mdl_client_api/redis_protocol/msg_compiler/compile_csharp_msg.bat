if not exist .\output\csharp mkdir .\output\csharp
for /r .\input\ %%h in (*) do .\bin\csharp\protogen.exe -i:.\input\%%~nh.proto -o:.\output\csharp\%%~nh.cs