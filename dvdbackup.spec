%define	name	dvdbackup
%define	version 0.1.1
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	DVD-Video creation framework
License: 	GPL
Group:		Archiving/Cd burning
URL:		http://dvd-create.sourceforge.net/index.shtml
Source:		http://dvd-create.sourceforge.net/%{name}-%{version}.tar.bz2
Patch:		%{name}-0.1.1-build.patch
BuildRequires:	libdvdread-devel

%description
DVD-Create will not just offer a free DVD Authoring solutions for Linux and
Unix. DVD-Create offers you a framework that enables you to write DVD creation,
editing, and backup software without needing to know all the secretes of
DVD-Video.

%prep
%setup -q -n %{name}
%patch

%build
cd src
gcc -o dvdbackup -I%{_includedir}/dvdread -ldvdread %{optflags} dvdbackup.c

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 src/dvdbackup %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README INSTALL COPYING
%{_bindir}/%{name}


