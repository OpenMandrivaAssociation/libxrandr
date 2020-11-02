# Wine uses libxrandr
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 2
%define libname %mklibname xrandr %{major}
%define devname %mklibname xrandr -d
%if %{with compat32}
%define lib32name libxrandr%{major}
%define dev32name libxrandr-devel
%endif

# 32-bit gcc LTO is broken (leads to unresolved
# symbols when building wine), but no harm done
# because we manually add -flto for the 64-bit
# build
%global _disable_lto 1
%global optflags %{optflags} -O3

Summary:	X RandR Library
Name:		libxrandr
Version:	1.5.2
Release:	4
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXrandr-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xrender) >= 0.9.0.2
%if %{with compat32}
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libXrender)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

%description
X RandR Library.

%package -n %{libname}
Summary:	X RandR Library
Group:		Development/X11

%description -n %{libname}
X RandR main library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	X RandR Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
X RandR main library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXrandr-%{version} -p1
export CONFIGURE_TOP="`pwd`"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
CFLAGS="%{optflags} -flto" LDFLAGS="%{ldflags} -flto" %configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXrandr.so.%{major}*

%files -n %{devname}
%{_libdir}/libXrandr.so
%{_libdir}/pkgconfig/xrandr.pc
%{_includedir}/X11/extensions/Xrandr.h
%{_mandir}/man3/XRR*.3*
%{_mandir}/man3/Xrandr.3*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXrandr.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXrandr.so
%{_prefix}/lib/pkgconfig/xrandr.pc
%endif
