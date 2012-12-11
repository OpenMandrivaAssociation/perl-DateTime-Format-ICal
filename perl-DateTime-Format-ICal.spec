%define upstream_name    DateTime-Format-ICal
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Parse and format iCal datetime and duration strings
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Event::ICal)
BuildRequires:	perl(DateTime::Set)
BuildRequires:	perl(DateTime::TimeZone)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module understands the ICal date/time and duration formats, as defined
in RFC 2445. It can be used to parse these formats in order to create the
appropriate objects.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 653403
- rebuild for updated spec-helper

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 542995
- import perl-DateTime-Format-ICal


* Thu May 06 2010 cpan2dist 0.09-1mdv
- initial mdv release, generated with cpan2dist
