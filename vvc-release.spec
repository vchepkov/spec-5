Name:           vvc-release       
Version:        5 
Release:        3
Summary:        VVC Repository Configuration

Group:          System Environment/Base 
License:        BSD
URL:            http://www.chepkov.com/rpms/

Source0:        VVC-GPG-KEY
Source1:        vvc.repo	

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     	noarch
Requires:      	redhat-release >= %{version}

%description
This repository holds all RPM's built by Vadym Chepkov <vvc@chepkov.com>
This package contains the repository GPG key as well as configuration for the Yum

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
%{__install} -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/VVC-GPG-KEY

# yum
%{__install} -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
%{__install} -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/*

%changelog
* Sat Aug 04 2012 Vadym Chepkov <vchepkov@gmail.com> - 5-3
- add extra repository

* Mon May 17 2010 Vadym Chepkov <vvc@chepkov.com> - 5-2
- Updated PGP key

* Sat Jan 16 2010 Vadym Chepkov <vvc@chepkov.com> - 5-1
- Use macros for files section
- strip trailing / in baseurl

* Sat Jan 17 2009 Vadym Chepkov <vvc@chepkov.com> - 5-0
- Initial verison
