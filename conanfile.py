from conans import ConanFile, CMake
   
class SolTwoConan(ConanFile):
  name = "sol2"
  version = "2.16.6"
  description = "Sol v2.0 - a C++ <-> Lua API wrapper with advanced features and top notch performance - is here, and it's great! Sol v2.0 - a C++ <-> Lua API wrapper with advanced features and top notch performance - is here, and it's great! "
  license="MIT"
  settings = "os", "compiler", "build_type", "arch"
  url = "https://github.com/pjohalloran/conan-sol2"

  def source(self):
    sol_filename = "sol.hpp"
    sol_url = "https://github.com/ThePhD/sol2/releases/download/v2.16.6/{}".format(sol_filename)
    tools.download(sol_url, sol_filename)

  def build(self):
       return

  def package(self):
    sol_filename = "sol.hpp"
    self.copy(sol_filename, dst="include", src=sol_filename)
