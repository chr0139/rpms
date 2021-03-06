# $Id$
# Authority: dag
# Upstream: GomoR <perl$gomor,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Write

Summary: Portable interface to open and send raw data to network
Name: perl-Net-Write
Version: 1.05
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Write/

Source: http://www.cpan.org/modules/by-module/Net/Net-Write-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Class::Gomor)
BuildRequires: perl(Net::Pcap) >= 0.12
BuildRequires: perl(Socket6)
Requires: perl(Class::Gomor)
Requires: perl(Net::Pcap) >= 0.12
Requires: perl(Socket6)

%filter_from_requires /^perl*/d
%filter_setup

%description
A portable interface to open and send raw data to network.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE LICENSE.Artistic MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Net::Write.3pm*
%doc %{_mandir}/man3/Net::Write::*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/Write/
%{perl_vendorlib}/Net/Write.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 1.05-2
- Disable automatic perl-dependencies

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.05-1
- Updated to version 1.05.

* Tue Jan 06 2009 Dag Wieers <cmr@financial.com> - 1.04-1
- Updated to release 1.04.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Sun Mar 16 2008 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
