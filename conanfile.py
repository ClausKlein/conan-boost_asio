#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostAsioConan(ConanFile):
    name = "boost_asio"
    version = "1.66.0"
    url = "https://github.com/bincrafters/conan-boost_asio"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["asio"]
    is_header_only = True

    def package_id_additional(self):
        self.info.header_only()

    requires = (
        "boost_package_tools/1.66.0@bincrafters/stable",
        "boost_array/1.66.0@bincrafters/stable",
        "boost_assert/1.66.0@bincrafters/stable",
        "boost_bind/1.66.0@bincrafters/stable",
        "boost_chrono/1.66.0@bincrafters/stable",
        "boost_config/1.66.0@bincrafters/stable",
        "boost_core/1.66.0@bincrafters/stable",
        "boost_coroutine/1.66.0@bincrafters/stable",
        "boost_date_time/1.66.0@bincrafters/stable",
        "boost_function/1.66.0@bincrafters/stable",
        "boost_regex/1.66.0@bincrafters/stable",
        "boost_smart_ptr/1.66.0@bincrafters/stable",
        "boost_system/1.66.0@bincrafters/stable",
        "boost_throw_exception/1.66.0@bincrafters/stable",
        "boost_type_traits/1.66.0@bincrafters/stable"
    )
        
    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "BSL-1.0"
    short_paths = True
    build_requires = "boost_generator/1.66.0@bincrafters/stable"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END
