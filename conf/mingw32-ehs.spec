%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}
%define __debug_install_post %{_mingw32_debug_install_post}

%define xname ehs

Summary: Embedded HTTP server
Name:    mingw32-%{xname}
Version: 1.5.0
Release: 104
License: LGPL
Group: Development/Libraries
URL: http://sourceforge.net/projects/ehs/
Source0: %{xname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 49
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-pthreads
BuildRequires:  mingw32-boost-static
BuildRequires:  mingw32-pcre

%description
Embedded HTTP Server (EHS) is a C++ class which can be inherited from in order
to give HTTP server functionality to any class or application. It supports form
data via POST or GET, and uploads via multi-part form attachments.

%package devel
Summary: Embedded HTTP server
Group: Development/Libraries

%description devel
Embedded HTTP Server (EHS) is a C++ class which can be inherited from in order
to give HTTP server functionality to any class or application. It supports form
data via POST or GET, and uploads via multi-part form attachments.

This package contains the development headers as well as a static library.

%{_mingw32_debug_package}

%prep
%setup -q -n %{xname}-%{version}

%build
%{_mingw32_configure} --enable-static --enable-shared \
    --with-dllpath=/usr/i686-pc-mingw32/sys-root/mingw/bin \
    --program-transform-name=s/i686-pc-mingw32-//
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_mingw32_bindir}/*.dll

%files devel
%defattr(644, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README ehs_development_guide.txt doc/html
%{_mingw32_bindir}/*.exe
%{_mingw32_libdir}/*
%{_mingw32_includedir}/%{xname}

%changelog
