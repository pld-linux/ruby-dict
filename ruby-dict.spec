%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	Ruby client for RFC2229 "Dict" protocol
Name:		ruby-dict
Version:	0.9.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.caliban.org/files/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	cb6a68464d8e12a88f592be00bf5d7ca
URL:		http://www.caliban.org/ruby/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/DICT is an RFC 2229 compliant client-side library implementation of the DICT protocol. It can be used to write clients that access dictionary definitions from a set of natural language dictionary databases.

In addition, rdict, a command-line based dictionary client built on Ruby/DICT, is included. 

%prep
%setup -q

%build

mkdir bin
mv rdict bin

ruby install.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby install.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{_bindir}}

ruby install.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%attr(755,root,root) %{_bindir}/rdict
%{ruby_rubylibdir}/dict.rb
%{ruby_ridir}/DICT
%{ruby_ridir}/*Error
