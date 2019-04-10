from conans import ConanFile, CMake, tools
import os, shutil

class ChaiscriptConan(ConanFile):
    name = 'chaiscript'
    version = '6.1.0'
    license = 'https://github.com/ChaiScript/ChaiScript/blob/master/license.txt'
    description = 'ChaiScript is one of the only embedded scripting language designed from the ground up to directly target C++ and take advantage of modern C++ development techniques, working with the developer like he expects it to work.'
    url = 'https://bitbucket.org/birconan/conan/issues'
    settings = []
    generators = []

    source_tag = 'v{}'.format(version)
    source_url = 'https://github.com/ChaiScript/ChaiScript.git'

    def source(self):
        git_cmd = f'git clone --depth 1 --verbose --branch {self.source_tag} {self.source_url} {self.name}'
        self.run(git_cmd)

    def configure(self):
        self.settings.clear()
        self.options.remove('static')

    def build(self):
        pass

    def package(self):
        self.copy("*.hpp", src="chaiscript/include/chaiscript", dst="include/chaiscript", keep_path=True)
