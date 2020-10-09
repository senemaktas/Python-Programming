# find file extension

import os
# unpacking the tuple
file_name, file_extension = os.path.splitext("/home/sidney/Downloads/bio.jpg")

print(file_name)
print(file_extension)
print(os.path.splitext("/home/sidney/Downloads/bio.jpg"))


# another way to do that 
import pathlib
fileExt=pathlib.Path("/home/sidney/Downloads/bio.jpg").suffix
print(fileExt)
