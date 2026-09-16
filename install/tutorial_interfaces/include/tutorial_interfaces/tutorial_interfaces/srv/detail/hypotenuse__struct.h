// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:srv/Hypotenuse.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/srv/hypotenuse.h"


#ifndef TUTORIAL_INTERFACES__SRV__DETAIL__HYPOTENUSE__STRUCT_H_
#define TUTORIAL_INTERFACES__SRV__DETAIL__HYPOTENUSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Hypotenuse in the package tutorial_interfaces.
typedef struct tutorial_interfaces__srv__Hypotenuse_Request
{
  double a;
  double b;
} tutorial_interfaces__srv__Hypotenuse_Request;

// Struct for a sequence of tutorial_interfaces__srv__Hypotenuse_Request.
typedef struct tutorial_interfaces__srv__Hypotenuse_Request__Sequence
{
  tutorial_interfaces__srv__Hypotenuse_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__srv__Hypotenuse_Request__Sequence;

// Constants defined in the message

/// Struct defined in srv/Hypotenuse in the package tutorial_interfaces.
typedef struct tutorial_interfaces__srv__Hypotenuse_Response
{
  double c;
} tutorial_interfaces__srv__Hypotenuse_Response;

// Struct for a sequence of tutorial_interfaces__srv__Hypotenuse_Response.
typedef struct tutorial_interfaces__srv__Hypotenuse_Response__Sequence
{
  tutorial_interfaces__srv__Hypotenuse_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__srv__Hypotenuse_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  tutorial_interfaces__srv__Hypotenuse_Event__request__MAX_SIZE = 1
};
// response
enum
{
  tutorial_interfaces__srv__Hypotenuse_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/Hypotenuse in the package tutorial_interfaces.
typedef struct tutorial_interfaces__srv__Hypotenuse_Event
{
  service_msgs__msg__ServiceEventInfo info;
  tutorial_interfaces__srv__Hypotenuse_Request__Sequence request;
  tutorial_interfaces__srv__Hypotenuse_Response__Sequence response;
} tutorial_interfaces__srv__Hypotenuse_Event;

// Struct for a sequence of tutorial_interfaces__srv__Hypotenuse_Event.
typedef struct tutorial_interfaces__srv__Hypotenuse_Event__Sequence
{
  tutorial_interfaces__srv__Hypotenuse_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__srv__Hypotenuse_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__SRV__DETAIL__HYPOTENUSE__STRUCT_H_
