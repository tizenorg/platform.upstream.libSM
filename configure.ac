#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.60)
AC_INIT([libSM],
        1.1.1,
        [https://bugs.freedesktop.org/enter_bug.cgi?product=xorg],
        libSM)

AC_CONFIG_SRCDIR([Makefile.am])
AM_INIT_AUTOMAKE([foreign dist-bzip2])

AM_MAINTAINER_MODE

# Require xorg-macros 1.3 or later: XORG_DEFAULT_OPTIONS
m4_ifndef([XORG_MACROS_VERSION],
	  [m4_fatal([must install xorg-macros 1.3 or later before running autoconf/autogen])])
XORG_MACROS_VERSION(1.3)

AM_CONFIG_HEADER([config.h])

# Checks for programs.
AC_PROG_LIBTOOL
AC_PROG_CC

XORG_DEFAULT_OPTIONS

# Checks for pkg-config packages
PKG_CHECK_MODULES(SM, [ice >= 1.0.5] xproto)
AC_SUBST(SM_CFLAGS)
AC_SUBST(SM_LIBS)

PKG_CHECK_MODULES(XTRANS, xtrans)
AC_SUBST(XTRANS_CFLAGS)
AC_SUBST(XTRANS_LIBS)

# Checks for libraries.

# Checks for header files.
AC_HEADER_STDC

# Needed to check for TCP & IPv6 support and set flags appropriately
XTRANS_CONNECTION_FLAGS

AC_ARG_WITH(libuuid, AC_HELP_STRING([--with-libuuid], [Build with libuuid support for client IDs]))

AC_CHECK_FUNCS([uuid_create], [], [
    if test x"$with_libuuid" != xno && test x"$have_system_uuid" != xyes; then
        PKG_CHECK_MODULES(LIBUUID, uuid, [HAVE_LIBUUID=yes], [HAVE_LIBUUID=no])
    fi
    if test x"$with_libuuid" = xyes && test x"$HAVE_LIBUUID" = xno; then
        AC_MSG_ERROR([requested libuuid support but uuid.pc not found])
    fi
])

AM_CONDITIONAL(WITH_LIBUUID, test x"$HAVE_LIBUUID" = xyes)

# Documentation is currently a single troff document
AC_PATH_PROGS([GROFF], [groff], [none], [$PATH:/usr/gnu/bin])

AC_MSG_CHECKING([whether to build documentation])
AC_ARG_ENABLE(docs, AC_HELP_STRING([--enable-docs],
				   [Enable building of Xaw documentation]),
	      [build_docs="${enableval}"], [build_docs="auto"])

if test "x${build_docs}" = xauto; then
    if test "x${GROFF}" = xnone ; then
	build_docs=no
    else
	build_docs=yes
    fi
fi
AC_MSG_RESULT([${build_docs}])
if test "x${build_docs}" = xyes && test "x${GROFF}" = xnone ; then
    AC_MSG_ERROR([can't build documentation without groff])
fi

AM_CONDITIONAL(BUILD_DOCS, [test x$build_docs = xyes])


AC_OUTPUT([Makefile
	   doc/Makefile
	   src/Makefile
	   sm.pc])
