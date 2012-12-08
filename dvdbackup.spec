%define	name	dvdbackup
%define	version 0.4.1
%define release %mkrel 2

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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-2mdv2011.0
+ Revision: 617907
- the mass rebuild of 2010.0 packages

* Fri Jun 12 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.1-1mdv2010.0
+ Revision: 385555
- update to new version 0.4.1

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4-1mdv2010.0
+ Revision: 384050
- new version

  + Emmanuel Andry <eandry@mandriva.org>
    - rebuid for bug #47115

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2-3mdv2009.1
+ Revision: 305813
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.2-2mdv2009.0
+ Revision: 266588
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2-1mdv2009.0
+ Revision: 194234
- new version

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.1.1-3mdv2008.1
+ Revision: 140722
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-3mdv2007.0
+ Revision: 125041
- fix build

* Thu Dec 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-2mdk
- spec cleanup
- %%mkrel

* Tue Nov 30 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.1.1-1mdk 
- first Mandrake release

