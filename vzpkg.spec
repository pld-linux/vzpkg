Summary:	OpenVZ template management tools
Name:		vzpkg
Version:	2.7.0
Release:	18
Source0:	http://download.openvz.org/template/utils/vzpkg/2.7.0-18/src/%{name}-%{version}-18.tar.bz2
# Source0-md5:	3ce22962f7b1c82252948e7365ebc89f
License:	QPL
Group:		Applications/System
URL:		http://openvz.org/
Requires:	coreutils
Requires:	gawk
Requires:	procmail
Requires:	sed
Requires:	vzctl >= 2.7.0-23
Requires:	vzyum >= 2.4.0-5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# strip fails to strip pre-packaged binaries from different arch
%define	no_install_post_strip	1

%description
OpenVZ template management tools are used for software installation
inside Virtual Private Servers.

%prep
%setup -q -n %{name}-%{version}-%{release}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS TODO
%attr(755,root,root) %{_bindir}/vzpkgcache
%attr(755,root,root) %{_bindir}/vzyum
%attr(755,root,root) %{_bindir}/vzrpm
%attr(755,root,root) %{_bindir}/vzpkgadd
%attr(755,root,root) %{_bindir}/vzpkgrm
%attr(755,root,root) %{_bindir}/vzpkgls
%attr(755,root,root) %{_bindir}/vzosname
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/functions
%attr(755,root,root) %{_datadir}/%{name}/cache-os
%attr(755,root,root) %{_datadir}/%{name}/myinit.*
%{_mandir}/man8/vzpkgcache.8.*
%{_mandir}/man8/vzyum.8.*
%{_mandir}/man8/vzrpm.8.*
