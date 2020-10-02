# ABSOLUTE -> An absolute import specifies the resource to be imported using its full path from the project's root folder.
#This is somewhat similar to its file path, but we use a dot (.) instead of slash (/)

from package1 import modele1
from package.module2 import function1
from package2.subpackage1.module5 import function2


#RELATIVE -> A relative import specifies the resource to be imported relative to the current location- that is,
# the location where the import statement is. 

from .some_module import some_class
# .. two dots mean that it is in the parent directory of the current location
from ..some_package import some_function
# . single dot means package is in the same directory 
from . import some_class
