# conan glfw prj test

### gcc
```
$conan install . --profile ./profile/gcc
$cmake . -DCMAKE_C_COMPILER=/usr/bin/gcc -DCMAKE_CXX_COMPILER=/usr/bin/g++
$cmake --build .
```
### clang
```
$conan install . --profile ./profile/clang
$cmake . -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++
$cmake --build .
```