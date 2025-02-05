%define _disable_rebuild_configure 1

Summary:	DVD-Video creation framework
Name:		dvdbackup
Version:	0.4.2
Release:	6
License: 	GPLv3
Group:		Archiving/Cd burning
Url:		https://sourceforge.net/projects/dvdbackup/
Source0:	http://downloads.sourceforge.net/dvdbackup/%{name}-%{version}.tar.xz
Patch0:   dvdbackup-dvdread-6.1.patch

BuildRequires:	pkgconfig(dvdread)

%description
DVD-Create will not just offer a free DVD Authoring solutions for Linux and
Unix. DVD-Create offers you a framework that enables you to write DVD creation,
editing, and backup software without needing to know all the secretes of
DVD-Video.

%prep
%setup -q
%autopatch -p0

%build
%configure

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README INSTALL COPYING AUTHORS ABOUT-NLS ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/dvdbackup.1*

