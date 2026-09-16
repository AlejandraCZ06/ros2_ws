#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to tutorial_interfaces__srv__Hypotenuse_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Hypotenuse_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub a: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub b: f64,

}



impl Default for Hypotenuse_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::Hypotenuse_Request::default())
  }
}

impl rosidl_runtime_rs::Message for Hypotenuse_Request {
  type RmwMsg = super::srv::rmw::Hypotenuse_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        a: msg.a,
        b: msg.b,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      a: msg.a,
      b: msg.b,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      a: msg.a,
      b: msg.b,
    }
  }
}


// Corresponds to tutorial_interfaces__srv__Hypotenuse_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Hypotenuse_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub c: f64,

}



impl Default for Hypotenuse_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::Hypotenuse_Response::default())
  }
}

impl rosidl_runtime_rs::Message for Hypotenuse_Response {
  type RmwMsg = super::srv::rmw::Hypotenuse_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        c: msg.c,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      c: msg.c,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      c: msg.c,
    }
  }
}






#[link(name = "tutorial_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__tutorial_interfaces__srv__Hypotenuse() -> *const std::ffi::c_void;
}

// Corresponds to tutorial_interfaces__srv__Hypotenuse
#[allow(missing_docs, non_camel_case_types)]
pub struct Hypotenuse;

impl rosidl_runtime_rs::Service for Hypotenuse {
    type Request = Hypotenuse_Request;
    type Response = Hypotenuse_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__tutorial_interfaces__srv__Hypotenuse() }
    }
}


