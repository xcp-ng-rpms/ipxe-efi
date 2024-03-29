%global package_speccommit 2f3137d75674b279554438a869ea902943d5da06
%global usver 20180514gite7f67d5
%global xsver 1.0.3
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit e7f67d5

Name: ipxe-efi
Summary: iPXE EFI drivers
Version: 20180514gite7f67d5
Release: %{?xsrel}%{?dist}

License: GPLv2
Source0: ipxe-efi-20180514gite7f67d5.tar.gz
Patch0: 0001-efi-Exclude-link-layer-header-length-from-MaxPacketS.patch
Patch1: increase-heap-size.patch
Patch2: realtek-increase-rx-desc.patch
Patch3: efi-snp-limit-rx-queue.patch

%{?_cov_buildrequires}

BuildRequires: gcc

%description
A build of iPXE in the form of EFI NIC drivers that can be used in an
UEFI environment or embedded into OVMF.


%prep
%autosetup -p1
%{?_cov_prepare}


%build
%{?_cov_wrap} make -C src %{?_smp_mflags} bin-x86_64-efi/10ec8139.drv.efi CONFIG=qemu
%{?_cov_wrap} make -C src %{?_smp_mflags} bin-x86_64-efi/8086100e.drv.efi CONFIG=qemu


%install
install -m 755 -d %{buildroot}/%{_datadir}/ipxe
install -m 644 src/bin-x86_64-efi/10ec8139.drv.efi %{buildroot}/%{_datadir}/ipxe/10ec8139.efi
install -m 644 src/bin-x86_64-efi/8086100e.drv.efi %{buildroot}/%{_datadir}/ipxe/8086100e.efi
%{?_cov_install}


%files
%license COPYING
%license COPYING.GPLv2
%{_datadir}/ipxe

%{?_cov_results_package}


%changelog
* Thu Sep 21 2023 Ross Lagerwall <ross.lagerwall@citrix.com> - 20180514gite7f67d5-1.0.3
- CA-383067: Fix oversized TFTP block size

* Fri Feb 11 2022 Ross Lagerwall <ross.lagerwall@citrix.com> - 20180514gite7f67d5-1.0.2
- CP-38416: Enable static analysis

* Fri Dec 04 2020 Ross Lagerwall <ross.lagerwall@citrix.com> - 20180514gite7f67d5-1.0.1
- CP-35517: Bump release to rebuild

* Wed Jul 04 2018 Ross Lagerwall <ross.lagerwall@citrix.com> - 20180514gite7f67d5-1
- Package iPXE for EFI builds
