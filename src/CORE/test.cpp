#include <assert.h>
#include <cstddef>
#include <node_api.h>
#include <vector>
#include <Windows.h>
#include <string>
using namespace std;

static napi_value f(napi_env env, napi_callback_info info) {
  napi_status status;
  napi_value str;
  status = napi_create_string_utf8(env, "C++", 3, &str);
  assert(status == napi_ok);
  return str;
}

static napi_value g(napi_env env, napi_callback_info info) {
  napi_status status;
  size_t argc = 2;
  napi_value args[2];

  status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  
  size_t strleng;
  napi_get_value_string_utf8(env, args[0], 0, 0, &strleng);
  string p1;
  p1.reserve(strleng + 1);
  p1.resize(strleng);
  status = napi_get_value_string_utf8(env, args[0], &p1[0], p1.capacity(), nullptr);

  napi_get_value_string_utf8(env, args[1], 0, 0, &strleng);
  string p2;
  p2.reserve(strleng + 1);
  p2.resize(strleng);
  status = napi_get_value_string_utf8(env, args[1], &p2[0], p2.capacity(), nullptr);
  napi_value v;
  string dest = " #1 ["+ p1 + "] " + "#2 [" + p2 + "] ";
  napi_create_string_utf8(env,dest.c_str(), strlen(dest.c_str()+1), &v);
  return v;

}


#define DECLARE_NAPI_METHOD(name, func)                                        \
  { name, 0, func, 0, 0, 0, napi_default, 0 }

static napi_value Init(napi_env env, napi_value exports) {
  napi_status status;
  napi_property_descriptor func_f = DECLARE_NAPI_METHOD("f", f);
  status = napi_define_properties(env, exports, 1, &func_f);
  napi_property_descriptor func_g = DECLARE_NAPI_METHOD("g", g);
  status = napi_define_properties(env, exports, 1, &func_g);
  assert(status == napi_ok);
  return exports;
}

NAPI_MODULE(NODE_GYP_MODULE_NAME, Init)
