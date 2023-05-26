# checksum

`xxHash` is an Extremely fast, non cryptographic Hash algorithm by Yann Collet and used by Wabbajack.  
https://github.com/Cyan4973/xxHash  

I used pyinstaller to make a Windows 10 xxhash64.exe inside the xxhash64.zip file.  
https://pypi.org/project/xxhash/  

note: you probably need to 'unblock' it after downloading the zip. 

The program options are:  
  -s sort the filenames descending by size  
  -l use append to create a log  
     note: you may want to delete the log before you re-run the program  

# sample output
```
F:\Wabbajack\Downloads_Skyrim>xxhash64.exe   
.   
26692bf09d2c365b Blackreach Sun-40045-1-4-1609918363.7z   
.   
33fe1f43a6a340f0 Chisel 1K-47534-1-0-1616687625.7z   
...........   
f51cfd431560f2c0 Northfires Windhelm-44099-1-1610046665.rar   
```
