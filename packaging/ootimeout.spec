Name:           ootimeout
Version:        0.1.0
Release:        1%{?dist}
Summary:        Strict capability timer killing runaway tasks with grace periods and exit propagation.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ootimeout
Source0:        ootimeout-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ootimeout is a sovereign, capability-bounded DEADLINE GUARD written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ootimeout
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ootimeout-uninstall

%files
/usr/bin/ootimeout
/usr/bin/ootimeout-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
