from conans import ConanFile, CMake

class GlfwProject(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "glfw/3.3.2"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()