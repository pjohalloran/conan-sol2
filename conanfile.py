from conans import ConanFile, CMake, tools
   
class SolTwoConan(ConanFile):
  name = "sol2"
  version = "2.15.6"
  description = "Sol v2.0 - a C++ <-> Lua API wrapper with advanced features and top notch performance - is here, and it's great! Sol v2.0 - a C++ <-> Lua API wrapper with advanced features and top notch performance - is here, and it's great! "
  license="MIT"
  settings = "os", "compiler", "build_type", "arch"
  url = "https://github.com/pjohalloran/conan-sol2"

  def source(self):
    sol_url = "https://github.com/ThePhD/sol2/releases/download/v%s/%s" % (self.version, "sol.hpp")
    tools.download(sol_url, "sol.hpp")

  def build(self):
       return

  def package(self):
    self.copy("sol.hpp", dst="include")
