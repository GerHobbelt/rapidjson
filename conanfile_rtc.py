from conans import ConanFile


class RapidjsonConan(ConanFile):
    name = "rapidjson"
    version = "d621dc9e9c77f81e5c8a35b8dcc16dcd63351321"
    url = "https://github.com/Esri/rapidjson/tree/runtimecore"
    license = "https://github.com/Esri/rapidjson/blob/runtimecore/license.txt"
    description = "A fast JSON parser/generator for C++ with both SAX/DOM style API."

    # Use the OS default to get the right line endings
    settings = "os"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/rapidjson/"

        # headers
        self.copy("*.h*", src=base + "include", dst=relative + "include")
