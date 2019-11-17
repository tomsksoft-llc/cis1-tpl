from conans import ConanFile
from conans import CMake


class Cis1Tpl(ConanFile):
    name = "cis1_tpl"
    version = "0.0.3"
    description = "TMP helpers and reflection."
    author = "MokinIA <mia@tomsksoft.com>"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
    exports = []
    exports_sources = ["CMakeLists.txt", "include/*", "src/*"]
    requires = ("boost_system/1.69.0@bincrafters/stable",
                "boost_asio/1.69.0@bincrafters/stable",
                "rapidjson/1.1.0@bincrafters/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("libcis1_tpl.a", dst="lib", src="lib")
        self.copy("libcis1_tpl.lib", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["cis1_tpl"]
