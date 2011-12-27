%define major 2
%define libxrandr %mklibname xrandr %{major}
%define develname %mklibname xrandr -d

Name: libxrandr
Summary:  X RandR Library
Version: 1.3.2
Release: 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXrandr-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxrender-devel >= 0.9.0.2
BuildRequires: x11-proto-devel >= 7.4-16mdv2009.1
BuildRequires: x11-util-macros >= 1.0.1

%description
X RandR Library

%package -n %{libxrandr}
Summary:  X RandR Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxrandr}
X RandR Library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxrandr} = %{version}
Provides: libxrandr-devel = %{version}-%{release}
Obsoletes: %{_lib}xrandr2-devel
Obsoletes: %{_lib}xrandr2-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXrandr-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxrandr}
%{_libdir}/libXrandr.so.%{major}*

%files -n %{develname}
%{_libdir}/libXrandr.so
%{_libdir}/pkgconfig/xrandr.pc
%{_includedir}/X11/extensions/Xrandr.h
%{_mandir}/man3/XRR*.3*
%{_mandir}/man3/Xrandr.3*

