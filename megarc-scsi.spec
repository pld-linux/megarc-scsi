Summary:	LSI Logic MegaRAID Linux MegaRC
Name:		megarc-scsi
Version:	1.11
Release:	1
License:	LSI
Group:		Base
Source0:	http://www.lsi.com/files/support/rsa/utilities/megaconf/ut_linux_megarc_%{version}.zip
# Source0-md5:	8e82adaa6dc7abb9d69e5eabdf8455dc
URL:		http://www.lsi.com/storage_home/products_home/internal_raid/megaraid_scsi/megaraid_scsi_3200/index.html#Miscellaneous
BuildRequires:	unzip
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

%description
Tool to control MegaRAID controllers:

- MegaRAID SCSI 320-0
- MegaRAID SCSI 320-1
- MegaRAID SCSI 320-2
- MegaRAID SCSI 320-0X
- MegaRAID SCSI 320-2X
- MegaRAID SCSI 320-4X
- MegaRAID SCSI 320-2E
- MegaRAID SATA 150-4
- MegaRAID SATA 150-6
- MegaRAID SATA 300-4x
- MegaRAID SATA 300-8x

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install megarc.bin $RPM_BUILD_ROOT%{_sbindir}/megarc-scsi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc megarc *.doc *.txt
%attr(755,root,root) %{_sbindir}/*
