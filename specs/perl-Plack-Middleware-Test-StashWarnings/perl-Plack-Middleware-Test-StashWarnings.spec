# $Id$
# Authority: shuff
# Upstream: Shawn M Moore <sartak$bestpractical,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Plack-Middleware-Test-StashWarnings

%define perl_prefix %{buildroot}%{_prefix}

Summary: Test a Plack application's warnings
Name: perl-Plack-Middleware-Test-StashWarnings
Version: 0.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Plack-Middleware-Test-StashWarnings/

Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALEXMV/Plack-Middleware-Test-StashWarnings-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl >= 5.8.1
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(Plack::Request)
BuildRequires: perl(Plack::Test)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.1
Requires: perl(Plack)
Requires: perl(Storable)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

%description
Plack::Middleware::Test::StashWarnings is a Plack middleware component to
record warnings generated by your application so that you can test them to make
sure your application complains about the right things.

%prep
%setup -n %{real_name}-%{version}

# fix problem with modules generated by older versions of Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{perl_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Plack/Middleware/Test/StashWarnings.pm
#%{perl_vendorlib}/Plack/Middleware/Test/StashWarnings/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/*/.packlist

%changelog
* Mon Aug 20 2012 Steve Huff <shuff@vecna.org> - 0.06-1
- Initial package.
