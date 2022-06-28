cmake_minimum_required (VERSION 2.6)

project (pybind)
enable_language(C)
enable_language(CXX)

find_package(pybind11 CONFIG REQUIRED)
include_directories(${pybind11_INCLUDE_DIRS})
message([MAIN] "Found pybind11 v${pybind11_VERSION}: ${pybind11_INCLUDE_DIRS}")

MESSAGE( [Main] " pybind11_INCLUDE_DIRS = ${pybind11_INCLUDE_DIRS}")
MESSAGE( [Main] " pybind11_LIBRARIES = ${pybind11_LIBRARIES}")

#
#   # Create an extension module
#   add_library(mylib MODULE main.cpp)
#   target_link_libraries(mylib pybind11::module)
#
#   # Or embed the Python interpreter into an executable
#   add_executable(myexe main.cpp)
#   target_link_libraries(myexe pybind11::embed)

# method (1): generate `examplelib.pyd`
pybind11_add_module(examplelib example.cpp)

# method (2): generate `examplelib.dll` rename to `examplelib.pyd`
#add_library(examplelib MODULE example.cpp)
#target_link_libraries(examplelib pybind11::module)

MESSAGE( [Main] " pybind11_INCLUDE_DIRS = ${pybind11_INCLUDE_DIRS}")
MESSAGE( [Main] " pybind11_LIBRARIES = ${pybind11_LIBRARIES}")

#add_executable(cpp_use_python cpp_use_python.cpp)
#target_link_libraries(cpp_use_python PRIVATE pybind11::embed)