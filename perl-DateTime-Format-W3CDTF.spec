%define upstream_name	 DateTime-Format-W3CDTF
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Parse and format W3CDTF datetime strings
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/RPM4/
Source0:	%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DateTime)
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module understands the W3CDTF date/time format, an ISO 8601 profile,
defined at http://www.w3.org/TR/NOTE-datetime. This format as the native
date format of RSS 1.0.

It can be used to parse these formats in order to create the appropriate
objects.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/*/*
