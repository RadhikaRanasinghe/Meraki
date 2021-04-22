cmake_minimum_required(VERSION 3.17)
project(DetectTest)

set(CMAKE_CXX_STANDARD 14)


# add libs you need
set(OpenCV_DIR "C:/opencv/build/x64/vc15/lib")
find_package( OpenCV REQUIRED )
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

file(GLOB srcs *.cpp *.c)
file(GLOB hdrs *.hpp *.h)

# linking
add_executable(DetectTest  extractFeats.cpp)
target_link_libraries(DetectTest ${OpenCV_LIBS})
