%define	name	dvdbackup
%define	version 0.4
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	DVD-Video creation framework
License: 	GPLv3
Group:		Archiving/Cd burning
URL:		http://sourceforge.net/projects/dvdbackup/
Source:		http://downloads.sourceforge.net/dvdbackup/%{name}-%{version}.tar.bz2
BuildRequires:	libdvdread-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
DVD-Create will not just offer a free DVD Authoring solutions for Linux and
Unix. DVD-Create offers you a framework that enables you to write DVD creation,
editing, and backup software without needing to know all the secretes of
DVD-Video.

%prep
%setup -q

%build
%configure2_5x

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS README INSTALL COPYING AUTHORS ABOUT-NLS ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/dvdbackup.1*
