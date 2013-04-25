Summary:	Ruby client for RFC2229 "Dict" protocol
Summary(pl.UTF-8):	Klient protokołu Dict (RFC 2229) w języku Ruby
Name:		ruby-dict
Version:	0.9.4
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.caliban.org/files/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	e529fead2b5e4c5b7ff970eb58269116
URL:		http://www.caliban.org/ruby/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/DICT is an RFC 2229 compliant client-side library implementation
of the DICT protocol. It can be used to write clients that access
dictionary definitions from a set of natural language dictionary
databases.

In addition, rdict, a command-line based dictionary client built on
Ruby/DICT, is included.

%description -l pl.UTF-8
Ruby/DICT to zgodna z RFC 2229 biblioteka implementująca część
kliencką protokołu DICT. Może być używana do pisania klientów
korzystających z definicji słownikowych ze zbioru baz danych słowników
języka naturalnego.

Ponadto załączony jest rdict - działający z linii poleceń klient
słownika zbudowany w oparciu o bibliotekę Ruby/DICT.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q
mkdir bin
mv rdict bin

%build
ruby install.rb config \
	--rb-dir=%{ruby_vendorlibdir} \
	--so-dir=%{ruby_vendorarchdir}

ruby install.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

rm -r ri/{Object,String}
rm ri/cache.ri
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_bindir}}

ruby install.rb install \
	--prefix=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -a rdoc/* $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%attr(755,root,root) %{_bindir}/rdict
%{ruby_vendorlibdir}/dict.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/DICT
%{ruby_ridir}/DICTError
%{ruby_ridir}/ConnectError
%{ruby_ridir}/ProtocolError
