# $Id$
# Authority: dag
# Upstream: Dug Song <dugsong$monkey,org>

%{?dist: %{expand: %%define %dist 1}}

Summary: Fragrouter is a network intrusion detection evasion toolkit
Name: fragrouter
Version: 1.6
Release: 0.2
License: BSD
Group: Applications/Internet
URL: http://www.monkey.org/~dugsong/fragrouter/

Source: fragrouter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: byacc, flex, libpcap
%{?fc6:BuildRequires:libpcap-devel}

%description
Fragrouter is a network intrusion detection evasion toolkit. It
implements most of the attacks described in the Secure Networks
"Insertion, Evasion, and Denial of Service: Eluding Network Intrusion
Detection" paper of January 1998.

This program was written in the hopes that a more precise testing
methodology might be applied to the area of network intrusion
detection, which is still a black art at best.

Conceptually, fragrouter is just a one-way fragmenting router - IP
packets get sent from the attacker to the fragrouter, which transforms
them into a fragmented data stream to forward to the victim.

%prep
%setup

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e 's|\$\(man8dir\)|\$(mandir)/man8|' Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CREDITS LICENSE README TODO VERSION
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.6-0.2
- Rebuild for Fedora Core 5.

* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Initial package. (using DAR)
