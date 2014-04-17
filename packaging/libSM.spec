Name:           libSM
Version:        1.2.2
Release:        1
License:        MIT
Summary:        X Session Management library
Url:            http://xorg.freedesktop.org/
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libSM.manifest
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ice) >= 1.0.5
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)

%description
The X Session Management Protocol provides a uniform mechanism for
users to save and restore their sessions. A session is a group of X
clients (programs), each of which has a particular state. The session
is controlled by a network service called the session manager, which
issues commands to its clients on behalf of the user. These commands
may cause clients to save their state or to terminate. It is expected
that the client will save its state in such a way that the client can
be restarted at a later time and resume its operation as if it had
never been terminated.

%package devel
Summary:        Development files for the X Session Management library
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
The X Session Management Protocol provides a uniform mechanism for
users to save and restore their sessions. A session is a group of X
clients (programs), each of which has a particular state. The session
is controlled by a network service called the session manager, which
issues commands to its clients on behalf of the user. These commands
may cause clients to save their state or to terminate. It is expected
that the client will save its state in such a way that the client can
be restarted at a later time and resume its operation as if it had
never been terminated.

This package contains the development headers for the library found
in %{name}.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen --with-libuuid --docdir=%_docdir/%{name} --disable-static
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_libdir}/libSM.so.6*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/X11/*
%{_libdir}/libSM.so
%{_libdir}/pkgconfig/sm.pc
%_docdir/%{name}

%changelog
