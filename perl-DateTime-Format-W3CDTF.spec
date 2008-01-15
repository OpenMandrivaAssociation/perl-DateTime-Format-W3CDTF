%define module	DateTime-Format-W3CDTF
%define name	perl-%{module}
%define version	0.04
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Parse and format W3CDTF datetime strings
License:	GPL
Group:		Development/Perl
Source:		%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/RPM4/
Buildroot:	%{_tmppath}/%{name}-root
Requires:	perl
BuildArch: noarch
BuildRequires: perl(DateTime)

%description
This module understands the W3CDTF date/time format, an ISO 8601 profile,
defined at http://www.w3.org/TR/NOTE-datetime. This format as the native
date format of RSS 1.0.

It can be used to parse these formats in order to create the appropriate
objects.

%prep
%setup -q -n %{module}-%{version}

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


