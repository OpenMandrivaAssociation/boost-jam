Summary:	Build tool for Boost libraries
Name:		boost-jam
Version:	3.1.18
Release:	%mkrel 1
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
