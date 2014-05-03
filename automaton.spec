Name:           automaton
Version:        0.1.0
Release:        1%{?dist}
Summary:        Run Puppet classes as if they were scripts

Group:          Utilities
License:        BSD
URL:            http://github.com/jcmcken/automaton
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       hiera
Requires:       puppet
Requires:       jgen

%description
Run Puppet classes as if they were scripts

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT/%{_sbindir}
%{__install} -m 0755 automaton $RPM_BUILD_ROOT/%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md
%doc LICENSE
%attr(0755,root,root) %{_sbindir}/automaton

%changelog
* Sat May 03 2014 Jon McKenzie - 0.1.0
- Initial RPM release
