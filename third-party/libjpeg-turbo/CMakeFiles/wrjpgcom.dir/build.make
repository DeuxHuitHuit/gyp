# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.9

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.9.1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.9.1/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo

# Include any dependencies generated for this target.
include CMakeFiles/wrjpgcom.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/wrjpgcom.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/wrjpgcom.dir/flags.make

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o: CMakeFiles/wrjpgcom.dir/flags.make
CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o: wrjpgcom.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o"
	/Users/xiangshouding/Applications/Xcode-beta.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o   -c /Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo/wrjpgcom.c

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/wrjpgcom.dir/wrjpgcom.c.i"
	/Users/xiangshouding/Applications/Xcode-beta.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo/wrjpgcom.c > CMakeFiles/wrjpgcom.dir/wrjpgcom.c.i

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/wrjpgcom.dir/wrjpgcom.c.s"
	/Users/xiangshouding/Applications/Xcode-beta.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo/wrjpgcom.c -o CMakeFiles/wrjpgcom.dir/wrjpgcom.c.s

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o.requires:

.PHONY : CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o.requires

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o.provides: CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o.requires
	$(MAKE) -f CMakeFiles/wrjpgcom.dir/build.make CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o.provides.build
.PHONY : CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o.provides

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o.provides.build: CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o


# Object files for target wrjpgcom
wrjpgcom_OBJECTS = \
"CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o"

# External object files for target wrjpgcom
wrjpgcom_EXTERNAL_OBJECTS =

wrjpgcom: CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o
wrjpgcom: CMakeFiles/wrjpgcom.dir/build.make
wrjpgcom: CMakeFiles/wrjpgcom.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable wrjpgcom"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/wrjpgcom.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/wrjpgcom.dir/build: wrjpgcom

.PHONY : CMakeFiles/wrjpgcom.dir/build

CMakeFiles/wrjpgcom.dir/requires: CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o.requires

.PHONY : CMakeFiles/wrjpgcom.dir/requires

CMakeFiles/wrjpgcom.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/wrjpgcom.dir/cmake_clean.cmake
.PHONY : CMakeFiles/wrjpgcom.dir/clean

CMakeFiles/wrjpgcom.dir/depend:
	cd /Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo /Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo /Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo /Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo /Users/xiangshouding/Work/nodejs/gyp/third-party/libjpeg-turbo/CMakeFiles/wrjpgcom.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/wrjpgcom.dir/depend

