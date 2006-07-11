#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Filter
%define		pnam	Template
Summary:	perl(Filter::Template)
Name:		perl-Filter-Template
Version:	1.02
Release:	0.1
# note if it is "same as perl"
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	15aa7b46d94c2dcd9fe0acc8914943df
# most of CPAN modules have generic URL (substitute pdir and pnam here)
URL:		http://search.cpan.org/dist/Filter-Template
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
#BuildRequires:	perl-
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
perl(Filter::Template)


%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Filter/Template.pm
%dir %{perl_vendorlib}/Filter/Template
%{perl_vendorlib}/Filter/Template/UseBytes.pm
%{_mandir}/man3/*
