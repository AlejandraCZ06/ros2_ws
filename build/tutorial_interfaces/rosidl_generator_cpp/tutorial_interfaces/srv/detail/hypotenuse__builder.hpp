// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:srv/Hypotenuse.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "tutorial_interfaces/srv/hypotenuse.hpp"


#ifndef TUTORIAL_INTERFACES__SRV__DETAIL__HYPOTENUSE__BUILDER_HPP_
#define TUTORIAL_INTERFACES__SRV__DETAIL__HYPOTENUSE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/srv/detail/hypotenuse__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace srv
{

namespace builder
{

class Init_Hypotenuse_Request_b
{
public:
  explicit Init_Hypotenuse_Request_b(::tutorial_interfaces::srv::Hypotenuse_Request & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::srv::Hypotenuse_Request b(::tutorial_interfaces::srv::Hypotenuse_Request::_b_type arg)
  {
    msg_.b = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::srv::Hypotenuse_Request msg_;
};

class Init_Hypotenuse_Request_a
{
public:
  Init_Hypotenuse_Request_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Hypotenuse_Request_b a(::tutorial_interfaces::srv::Hypotenuse_Request::_a_type arg)
  {
    msg_.a = std::move(arg);
    return Init_Hypotenuse_Request_b(msg_);
  }

private:
  ::tutorial_interfaces::srv::Hypotenuse_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::srv::Hypotenuse_Request>()
{
  return tutorial_interfaces::srv::builder::Init_Hypotenuse_Request_a();
}

}  // namespace tutorial_interfaces


namespace tutorial_interfaces
{

namespace srv
{

namespace builder
{

class Init_Hypotenuse_Response_c
{
public:
  Init_Hypotenuse_Response_c()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::tutorial_interfaces::srv::Hypotenuse_Response c(::tutorial_interfaces::srv::Hypotenuse_Response::_c_type arg)
  {
    msg_.c = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::srv::Hypotenuse_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::srv::Hypotenuse_Response>()
{
  return tutorial_interfaces::srv::builder::Init_Hypotenuse_Response_c();
}

}  // namespace tutorial_interfaces


namespace tutorial_interfaces
{

namespace srv
{

namespace builder
{

class Init_Hypotenuse_Event_response
{
public:
  explicit Init_Hypotenuse_Event_response(::tutorial_interfaces::srv::Hypotenuse_Event & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::srv::Hypotenuse_Event response(::tutorial_interfaces::srv::Hypotenuse_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::srv::Hypotenuse_Event msg_;
};

class Init_Hypotenuse_Event_request
{
public:
  explicit Init_Hypotenuse_Event_request(::tutorial_interfaces::srv::Hypotenuse_Event & msg)
  : msg_(msg)
  {}
  Init_Hypotenuse_Event_response request(::tutorial_interfaces::srv::Hypotenuse_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_Hypotenuse_Event_response(msg_);
  }

private:
  ::tutorial_interfaces::srv::Hypotenuse_Event msg_;
};

class Init_Hypotenuse_Event_info
{
public:
  Init_Hypotenuse_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Hypotenuse_Event_request info(::tutorial_interfaces::srv::Hypotenuse_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_Hypotenuse_Event_request(msg_);
  }

private:
  ::tutorial_interfaces::srv::Hypotenuse_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::srv::Hypotenuse_Event>()
{
  return tutorial_interfaces::srv::builder::Init_Hypotenuse_Event_info();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__SRV__DETAIL__HYPOTENUSE__BUILDER_HPP_
