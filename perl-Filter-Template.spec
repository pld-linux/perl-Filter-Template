#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Filter
%define		pnam	Template
Summary:	Filter::Template - source filter for inline code templates
Summary(pl.UTF-8):	Filter::Template - filtr kodu źródłowego dla szablonów kodu inline
Name:		perl-Filter-Template
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Filter/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ea654b36d5de0f1167566690e6fce108
URL:		http://search.cpan.org/dist/Filter-Template/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filter::Template is a Perl source filter that provides simple inline
source code templates. Inlined source code can be significantly faster
than subroutines, especially for small-scale functions like accessors
and mutators. On the other hand, they are more difficult to maintain
and use. Choose your trade-offs wisely.

%description -l pl.UTF-8
Filter::Template to filtr kodu źródłowego Perla udostępniający proste
szablony kodu źródłowego inline. Kod źródłowy inline może być znacząco
szybszy niż podprocedury, zwłaszcza dla małych funkcji takich jak
accessor czy mutator. Z drugiej strony są one dużo trudniejsze w
utrzymywaniu i używaniu. Trzeba dokonać mądrego wyboru.

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
