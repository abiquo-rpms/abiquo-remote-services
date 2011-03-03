%define abiquo_basedir /opt/abiquo

Name:     abiquo-remote-services
Version: 1.7
Release:  11%{?dist}%{?buildstamp}
Summary:  Abiquo Remote Services
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  README 
Source1:  abiquo.properties.remoteservices
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-vsm abiquo-ssm abiquo-nodecollector abiquo-am abiquo-virtualfactory libvirt-client dhcp redis nfs-utils abiquo-server-tools

%description
Next Generation Cloud Management Solution

This package installs Abiquo Remote Services components.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}/
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/config/examples/
cp ../SOURCES/README $RPM_BUILD_ROOT/%{_docdir}/%{name}/
cp %{SOURCE1} $RPM_BUILD_ROOT/%{abiquo_basedir}/config/examples/


%clean
rm -rf $RPM_BUILD_ROOT

%post
# Add dhcpd conf
cat > /etc/dhcpd.conf <<EOF
ddns-update-style interim;

omapi-port 7911;

subnet 0.0.0.0 netmask 0.0.0.0 {
	default-lease-time 60000;
	max-lease-time 720000;
	option subnet-mask 255.255.255.0;
	option domain-name-servers 8.8.8.8;
}

EOF

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/README
%{abiquo_basedir}/config/examples/abiquo.properties.remoteservices

%changelog
* Thu Mar 03 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-11
- add default storagemanager properties

* Wed Jan 26 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-10
- depend on abiquo-server-tools

* Mon Jan 24 2011 Sergio Rubio <srubio@abiquo.com> 1.7-9
- moved properties template to /opt/abiquo/config/examples

* Mon Jan 24 2011 Sergio Rubio <srubio@abiquo.com> 1.7-8
- fixes in files section

* Mon Jan 24 2011 Sergio Rubio <srubio@abiquo.com> 1.7-7
- fixed files section

* Mon Jan 24 2011 Sergio Rubio <srubio@abiquo.com> 1.7-6
- moved properties template to /usr/share/doc

* Wed Jan 19 2011 Sergio Rubio <srubio@abiquo.com> 1.7-5
- updated default properties

* Tue Jan 18 2011 Sergio Rubio <srubio@abiquo.com> 1.7-4
- updated default properties

* Fri Jan 14 2011 Sergio Rubio <srubio@abiquo.com> 1.7-3
- updated properties template

* Mon Jan 10 2011 Sergio Rubio <srubio@abiquo.com> 1.7-2
- add missing rabbitmq properties
- add nfs-utils to requires

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Tue Oct 06 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-2
- added redis dep

* Tue Oct 05 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1
- Updated to upstream 1.6.8

* Thu Sep 02 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- updated to 1.6.5

* Fri Jul 09 2010 Sergio Rubio srubio@abiquo.com 1.6-3
- Added dhcp dep
- config dhcpd in %post

* Fri Jul 09 2010 Sergio Rubio srubio@abiquo.com 1.6-2
- Added buildstamp to the package

* Mon Jul 05 2010 Sergio Rubio srubio@abiquo.com 1.6-1
- Updated to upstream 1.6

* Wed May 26 2010 Sergio Rubio srubio@abiquo.com 1.5.1
- Initial Release
