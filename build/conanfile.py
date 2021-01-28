from conans import ConanFile, CMake

class GlfwProject(ConanFile):
    name = "GlfwProject"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = [
            "glfw/3.3.2",
        ]

    # TODO: install_folder & build_folder

    # $conan build .
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()