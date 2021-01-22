project(testglfwprj)
cmake_minimum_required(VERSION 3.19)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_basic_setup(TARGETS)

add_executable(glfwTest ${CMAKE_BINARY_DIR}/../src/main.cpp)
target_link_libraries(glfwTest CONAN_PKG::glfw)