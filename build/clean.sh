#!/bin/sh

cd `dirname "$0"`
SHELL_PATH=`pwd -P`
cd $SHELL_PATH

rm CMakeCache.txt
rm -r CMakeFiles/
rm Makefile
rm -r bin/
rm cmake_install.cmake
rm conan.lock
rm conanbuildinfo.cmake
rm conanbuildinfo.txt
rm conaninfo.txt
rm graph_info.json
rm -r .ninja_deps
rm -r .ninja_log
rm ninja
rm compile_commands.json
rm -r .cmake/
