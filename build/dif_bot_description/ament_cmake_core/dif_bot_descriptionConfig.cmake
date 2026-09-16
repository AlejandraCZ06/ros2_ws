# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_dif_bot_description_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED dif_bot_description_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(dif_bot_description_FOUND FALSE)
  elseif(NOT dif_bot_description_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(dif_bot_description_FOUND FALSE)
  endif()
  return()
endif()
set(_dif_bot_description_CONFIG_INCLUDED TRUE)

# output package information
if(NOT dif_bot_description_FIND_QUIETLY)
  message(STATUS "Found dif_bot_description: 0.0.0 (${dif_bot_description_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'dif_bot_description' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT dif_bot_description_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(dif_bot_description_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${dif_bot_description_DIR}/${_extra}")
endforeach()
