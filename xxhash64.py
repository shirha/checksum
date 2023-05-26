'''
https://github.com/Cyan4973/xxHash
https://pypi.org/project/xxhash/
pyinstaller xxhash64.py -F --onefile
'''
import sys
import os
import re
import xxhash
h64 = xxhash.xxh64()


list_of_files = filter( 
  lambda x: 
    os.path.isfile(x) and 
    re.search("(zip|rar|7z)$", x), 
  os.listdir() )

if '-s' in sys.argv:
  list_of_files = sorted( 
    list_of_files, 
    key=lambda x: 
      os.stat(x).st_size, 
    reverse=True )
  
for archive in list_of_files:
  i = 0
  with open(archive, 'rb') as bf:
    size = os.stat(archive).st_size
    x = 0
    while(size > 1024):
      size /= 1024
      x += 1

    while True:
      data = bf.read(1048576) # 2**20
      if data:
        h64.update(data)
        if i % 100 == 0:
          print('.', end='', flush=True)
        i += 1
      else:
        print()
        break

  o = f"{h64.hexdigest()} {size:6.1f}{['B ','KB','MB','GB','TB'][x]} {archive}"
  print(o)

  if '-l' in sys.argv:
    with open('xxhash64.log', 'a') as log:
      log.write(o + "\n")

  h64.reset()
