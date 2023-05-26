'''
https://github.com/Cyan4973/xxHash
https://pypi.org/project/xxhash/
'''
import os
import re
import xxhash
h64 = xxhash.xxh64()
for archive in os.listdir():
  if re.search("(zip|rar|7z)$", archive):
    i = 0
    with open(archive, 'rb') as bf:
      while True:
        data = bf.read(1048576) # 2**20
        if data:
          h64.update(data)
          if i % 100 == 0:
            print('.', end='', flush=True)
          i += 1
        else:
          break
    print("\n", h64.hexdigest(), archive)
    h64.reset()
