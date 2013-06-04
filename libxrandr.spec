%define major 2
%define libxrandr %mklibname xrandr %{major}
%define develname %mklibname xrandr -d

Name:		libxrandr
Summary:	X RandR Library
Version:	1.4.1
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXrandr-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xrender) >= 0.9.0.2
BuildRequires:	x11-proto-devel >= 7.4-16mdv2009.1
BuildRequires:	x11-util-macros >= 1.0.1

%description
X RandR Library.

%package -n %{libxrandr}
Summary:	X RandR Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}-%{release}

%description -n %{libxrandr}
X RandR main library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxrandr} = %{version}-%{release}
Provides:	libxrandr-devel = %{version}-%{release}
Obsoletes:	%{_lib}xrandr2-devel < %{version}
Obsoletes:	%{_lib}xrandr2-static-devel
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
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

%files -n %{libxrandr}
%{_libdir}/libXrandr.so.%{major}*

%files -n %{develname}
%{_libdir}/libXrandr.so
%{_libdir}/pkgconfig/xrandr.pc
%{_includedir}/X11/extensions/Xrandr.h
%{_mandir}/man3/XRR*.3*
%{_mandir}/man3/Xrandr.3*


%changelog
* Thu Aug 16 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.0-1
+ Revision: 814977
- spec file clean
- update to new version 1.4.0

* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3.2-3
+ Revision: 783373
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.3.2-2
+ Revision: 745744
- rebuild
- disabled static build
- removed major from devel pkg
- removed .la files
- cleaned up spec
- employed major macro

* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.2-1
+ Revision: 699277
- update to new version 1.3.2

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-3
+ Revision: 660304
- mass rebuild

* Fri Oct 29 2010 Thierry Vignaud <tv@mandriva.org> 1.3.1-2mdv2011.0
+ Revision: 589852
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-3mdv2010.1
+ Revision: 520971
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3.0-2mdv2010.0
+ Revision: 425934
- rebuild

* Fri Mar 06 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.3.0-1mdv2009.1
+ Revision: 349899
- New version 1.3.0
- Remove patch 1 (applied upstream)

* Sun Feb 01 2009 Colin Guthrie <cguthrie@mandriva.org> 1.2.99.4-2mdv2009.1
+ Revision: 336203
- Apply upstream fix for bug that is highlighted in latest cmd line RC

* Wed Dec 17 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.99.4-1mdv2009.1
+ Revision: 315243
- New version: 1.2.99.4

* Sat Dec 13 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.99.3-1mdv2009.1
+ Revision: 313928
- New version 1.2.99.3

* Tue Dec 02 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.91-1mdv2009.1
+ Revision: 309222
- New version: 1.2.91

* Tue Jul 15 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.3-1mdv2009.0
+ Revision: 236192
- Update to version 1.2.3

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2.2-4mdv2009.0
+ Revision: 223083
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.
    - Update BuildRequires and rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.2.2-2mdv2008.1
+ Revision: 150869
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Sep 06 2007 Colin Guthrie <cguthrie@mandriva.org> 1.2.2-1mdv2008.0
+ Revision: 81013
- New upstream release: 1.2.2 (consolidates patch already applied)

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension

* Wed Jul 11 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.2.1-3mdv2008.0
+ Revision: 51289
- There was one more place where crtc width was being wrongly set as the crtc
  height. Updating patch

* Tue Jul 03 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.2.1-2mdv2008.0
+ Revision: 47575
- Fix a bug on notifying CRTC changes: the width was being set to the height value


* Mon Mar 05 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.2.1-1mdv2007.0
+ Revision: 133294
- new version (1.2.1)
- remove dont_use_delete patch: applied upstream

* Wed Feb 28 2007 Colin Guthrie <cguthrie@mandriva.org> 1.2.0-2mdv2007.1
+ Revision: 127210
- Upstream patch to avoid use of C++ reserved words (delete)

* Tue Feb 27 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.2.0-1mdv2007.1
+ Revision: 126717
- new upstream release: 1.2.0 supporting the version 1.2 of the X RandR extension
- rebuild to fix cooker uploading
- X11R7.1
- increment release
- fixed more dependencies
- Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

