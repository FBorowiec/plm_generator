load("@rules_python//python:defs.bzl", "py_test")

py_test(
    name = "logger_test",
    srcs = ["logger_test.py"],
    deps = [
        "//logger",
        "//third_party:freezegun",
        "//third_party:testing.postgresql",
    ],
)
