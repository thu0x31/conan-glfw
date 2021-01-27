from conans import ConanFile, CMake

class GlfwProject(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "glfw/3.3.2"
    generators = "cmake"
    # default_options = {
    #         "poco:shared": True,
    #         "openssl:shared": True
    #     }

    def build(self):
        cmake = CMake(self)
        cmake.definitions = {
            "CMAKE_C_COMPILER": "/usr/bin/clang",
            "CMAKE_CXX_COMPILER": "/usr/bin/clang++"
        }
        cmake.configure()
        cmake.build()