# rpmlint error
%define	debug_package %{nil}

Summary:	Build tool for Boost libraries
Name:		boost-jam
Version:	3.1.18
Release:	4
License:	Boost
Group:		Development/Other
URL:		http://www.boost.org/
Source0:	http://download.sourceforge.net/boost/%{name}-%{version}.tgz
Buildrequires:	byacc

%description
Boost Jam is a build tool based on FTJam, which in turn is based on 
Perforce Jam. It contains significant improvements made to facilitate
its use in the Boost Build System, but should be backward compatible 
with Perforce Jam.

%prep
%setup -q

%build
export CC="%{__cc}"
export CFLAGS="%{optflags}"
./build.sh cc

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 bin.linux*/bjam %{buildroot}%{_bindir}/bjam

%files
%doc LICENSE_1_0.txt *.css *.html *.png images jam
%{_bindir}/bjam

