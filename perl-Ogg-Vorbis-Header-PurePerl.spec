#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Ogg
%define	pnam	Vorbis-Header-PurePerl
Summary:	Ogg::Vorbis::Header::PurePerl - An object-oriented interface to Ogg Vorbis information.
Summary(pl):	Ogg::Vorbis::Header::PurePerl - zorientowany obiektowo interfejs do odzczytywania informacji Ogg Vorbis
Name:		perl-Ogg-Vorbis-Header-PurePerl
Version:	0.07
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cadb2cde88dd815323015154dd3ced40
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended to be a drop in replacement for
Ogg::Vorbis::Header, implemented entirely in Perl. It provides an
object-oriented interface to Ogg Vorbis information and comment
fields. (NOTE: This module currently supports only read operations).

%description -l pl
Ten modu³ w za³o¿eniu ma byæ w ca³o¶ci zaimplementowanym w Perlu
zamiennikiem dla Ogg::Vorbis::Header. Dostarcza zorientowanego
obiektowo interfejsu do pól informacji i komentarzy Ogg Vorbis.
(INFORMACJA: Na chwilê obecn± ten modu³ obs³uguje tylko operacje
odczytu).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{perl_vendorlib}/Ogg/Vorbis/Header/ogginfo.pl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Ogg/Vorbis/Header
%attr(755,root,root) %{_bindir}/ogginfo.pl
%{perl_vendorlib}/Ogg/Vorbis/Header/*.pm
%{_mandir}/man3/*
