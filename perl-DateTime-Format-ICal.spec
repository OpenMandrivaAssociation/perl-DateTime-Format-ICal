%define upstream_name    DateTime-Format-ICal
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Parse and format iCal datetime and duration strings
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Event::ICal)
BuildRequires: perl(DateTime::Set)
BuildRequires: perl(DateTime::TimeZone)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module understands the ICal date/time and duration formats, as defined
in RFC 2445. It can be used to parse these formats in order to create the
appropriate objects.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


