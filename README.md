# conan glfw

### gcc
```
$cd build
$conan install . --profile ./profiles/gcc
$cmake . -DCMAKE_C_COMPILER=/usr/bin/gcc -DCMAKE_CXX_COMPILER=/usr/bin/g++
$cmake --build .
```
### clang
```
$cd build
$conan install . --profile ./profiles/clang
$cmake . -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++
$cmake --build .
```
