class PathUtils:
    @staticmethod
    def get_extension(filename):
        """Return a file extension (including the dot)"""
        return filename[filename.rfind("."):] if "." in filename else ""
    
    @staticmethod
    def get_directory(path):
        """Return the directory path without the filename"""
        return path[:path.rfind("/")] if "/" in path else ""

    @staticmethod
    def get_basename(path):
        """Return the file name from the directory"""
        return path[path.rfind("/"):] if "/" in path else ""

# Use the class
print(PathUtils.get_extension("image.png"))
print(PathUtils.get_extension("1.txt"))
print(PathUtils.get_extension("test"))

print(PathUtils.get_directory("/home/matt/python.txt"))
print(PathUtils.get_basename("/home/matt/python.txt"))