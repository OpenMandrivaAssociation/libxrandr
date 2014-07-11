%define major 2
%define libname %mklibname xrandr %{major}
%define devname %mklibname xrandr -d

Summary:	X RandR Library
Name:		libxrandr
Version:	1.4.2
Release:	7
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXrandr-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xrender) >= 0.9.0.2

%description
X RandR Library.

%package -n %{libname}
Summary:	X RandR Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
X RandR main library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxrandr-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXrandr-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXrandr.so.%{major}*

%files -n %{devname}
%{_libdir}/libXrandr.so
%{_libdir}/pkgconfig/xrandr.pc
%{_includedir}/X11/extensions/Xrandr.h
%{_mandir}/man3/XRR*.3*
%{_mandir}/man3/Xrandr.3*

