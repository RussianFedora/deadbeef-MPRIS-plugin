%global gitcommit cc52a4a
%global gitcommit_full cc52a4aa7da0c859fd46720b53866a68e1495cd6
%global date 20141002

Name:           deadbeef-MPRIS-plugin
Version:        2.1
Release:        1.%{date}git%{gitcommit}%{?dist}
Summary:        MPRIS plugin of DeaDBeeF music player

License:        GPLv3
URL:            http://kernelhcy.github.io/DeaDBeeF-MPRIS-plugin/
Source0:        https://github.com/ihacklog/DeaDBeeF-MPRIS-plugin/tarball/%{gitcommit_full}

BuildRequires:  autoconf
BuildRequires:  deadbeef-devel
Requires:       deadbeef


%description
The MPRIS plugin for DeaDBeeF music player.

%prep
%setup -q -n ihacklog-DeaDBeeF-MPRIS-plugin-%{gitcommit}


%build
autoreconf
%configure
make %{?_smp_mflags}


%install
%make_install
rm %{buildroot}%{_libdir}/deadbeef/mpris.*a


%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/deadbeef/mpris.*


%changelog
* Thu Oct  2 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.1-1.20141002gitcc52a4a.R
- Initial release for fedora
