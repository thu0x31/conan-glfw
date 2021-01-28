from conans import ConanFile, CMake

class GlfwProject(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "glfw/3.3.2"
    generators = "cmake"
    build_dir = "ConanInstallFiles/"

    def requirements(self):
        self.requires("glfw/3.3.2")

    # $conan build .
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()