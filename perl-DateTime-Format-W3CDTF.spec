%define upstream_name	 DateTime-Format-W3CDTF
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Parse and format W3CDTF datetime strings
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/RPM4/
Source0:	%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildArch:	noarch

%description
This module understands the W3CDTF date/time format, an ISO 8601 profile,
defined at http://www.w3.org/TR/NOTE-datetime. This format as the native
date format of RSS 1.0.

It can be used to parse these formats in order to create the appropriate
objects.

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 654307
- rebuild for updated spec-helper

* Mon Feb 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1
+ Revision: 636592
- update to new version 0.06

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 461270
- update to 0.05

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 406975
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.04-6mdv2009.0
+ Revision: 256560
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.04-4mdv2008.1
+ Revision: 152053
- rebuild
- rebuild

  + Pixel <pixel@mandriva.com>
    - rebuild for perl-5.10.0

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.04-1mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 18 2006 Olivier Thauvin <nanardon@mandriva.org> 0.04-1mdv2007.0
+ Revision: 85415
- buildrequires
- initial mdv package
- Create perl-DateTime-Format-W3CDTF

