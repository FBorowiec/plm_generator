load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "logger",
    srcs = ["logger.py"],
    deps = [
        "//config:config_handler",
        "//third_party:psycopg2",
    ],
)
