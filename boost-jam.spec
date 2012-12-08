Summary:	Build tool for Boost libraries
Name:		boost-jam
Version:	3.1.18
Release:	%mkrel 2
URL:		http://www.boost.org/
Source0:	http://download.sourceforge.net/boost/%{name}-%{version}.tgz
License: 	Boost
Group: 		Development/Other
Buildrequires:	byacc
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Boost Jam is a build tool based on FTJam, which in turn is based on 
Perforce Jam. It contains significant improvements made to facilitate
its use in the Boost Build System, but should be backward compatible 
with Perforce Jam.

Authors:
	Perforce Jam : Cristopher Seiwald
	FT Jam       : David Turner
	Boost Jam    : David Abrahams

%prep
%setup -q

%build
export CC="%{__cc}"
export CFLAGS="%{optflags}"
./build.sh cc

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 755 bin.linux*/bjam %{buildroot}%{_bindir}/bjam

%files
%defattr(-,root,root)
%defattr(0644,root,root,0755)
%doc LICENSE_1_0.txt *.css *.html *.png images jam
%attr(0755,root,root) %{_bindir}/bjam

%clean
%{__rm} -rf %{buildroot}


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.1.18-2mdv2011.0
+ Revision: 663330
- mass rebuild

* Sun Jul 25 2010 Matthew Dawkins <mattydaw@mandriva.org> 3.1.18-1mdv2011.0
+ Revision: 559693
- new version 3.1.18

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1.17-3mdv2010.1
+ Revision: 522256
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 3.1.17-2mdv2010.0
+ Revision: 413180
- rebuild

* Tue Dec 23 2008 Funda Wang <fwang@mandriva.org> 3.1.17-1mdv2009.1
+ Revision: 317919
- new version 3.1.17

* Sun May 25 2008 Funda Wang <fwang@mandriva.org> 3.1.16-1mdv2009.0
+ Revision: 211103
- New version 3.1.16

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jun 18 2007 Emmanuel Andry <eandry@mandriva.org> 3.1.14-1mdv2008.0
+ Revision: 41104
- New version


* Thu Nov 16 2006 Lenny Cartier <lenny@mandriva.com> 3.1.13-1mdv2007.0
+ Revision: 84805
- Updated to 3.1.13
- Import boost-jam

