# TODO:
# - UP/SMP
# - dependencies
# - conflict with old bluez modules in kernel
Summary:	Bluetooth kernel modules
Summary(pl):	Modu造 j康ra Bluetooth
Name:		bluez-kernel
Version:	2.3
Release:	1
License:	GPL v2
Group:		Base/Kernel
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	1193a6242a0b1f607dcdde7aaeb2095c
# for 2.4.20
Source1:	http://bluez.sourceforge.net/download/hci_usb-031803.tar.gz
# Source1-md5:	d53870ee2d3b1b309364a01a799cf87e
Patch0:		%{name}-O1.patch
URL:		http://bluez.sourceforge.net/
#BuildRequires:	kernel-source >= 2.4.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluetooth kernel modules.

%description -l pl
Modu造 j康ra Bluetooth.

%package -n kernel-net-bluez
Summary:	Bluetooth kernel modules
Summary(pl):	Modu造 j康ra Bluetooth
Group:		Base/Kernel

%description -n kernel-net-bluez
Bluetooth kernel modules.

%description -n kernel-net-bluez -l pl
Modu造 j康ra Bluetooth.

%prep
%setup -q
%patch0 -p1
tar xzf %{SOURCE1} -C drivers

%build
# autoconf 2.5x uses "rm -rf core", thus removing core directory
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	DEPMOD=/bin/true

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kernel-net-bluez
%defattr(644,root,root,755)
%doc AUTHORS README doc/modules.txt
/lib/modules/*/kernel/drivers/bluetooth
/lib/modules/*/kernel/misc/*.o*
/lib/modules/*/kernel/net/bluetooth
