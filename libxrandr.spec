%define libxrandr %mklibname xrandr 2
Name: libxrandr
Summary:  X RandR Library
Version: 1.2.1
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXrandr-%{version}.tar.bz2
Patch0: libxrandr-1.2.1-fix_crtc_change_width_report.patch
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxrender-devel >= 0.9.0.2
BuildRequires: x11-proto-devel >= 1.2.0-10mdv2007.1
BuildRequires: x11-util-macros >= 1.0.1

%description
X RandR Library

#-----------------------------------------------------------

%package -n %{libxrandr}
Summary:  X RandR Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxrandr}
X RandR Library

#-----------------------------------------------------------

%package -n %{libxrandr}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxrandr} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxrandr-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxrandr}-devel
Development files for %{name}

%pre -n %{libxrandr}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxrandr}-devel
%defattr(-,root,root)
%{_libdir}/libXrandr.so
%{_libdir}/libXrandr.la
%{_libdir}/pkgconfig/xrandr.pc
%{_includedir}/X11/extensions/Xrandr.h
%{_mandir}/man3/XRR*.3*
%{_mandir}/man3/Xrandr.3*

#-----------------------------------------------------------

%package -n %{libxrandr}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxrandr}-devel = %{version}
Provides: libxrandr-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxrandr}-static-devel
Static development files for %{name}

%files -n %{libxrandr}-static-devel
%defattr(-,root,root)
%{_libdir}/libXrandr.a

#-----------------------------------------------------------

%prep
%setup -q -n libXrandr-%{version}
%patch0 -p1 -b .crtc_width

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxrandr}
%defattr(-,root,root)
%{_libdir}/libXrandr.so.2
%{_libdir}/libXrandr.so.2.*


