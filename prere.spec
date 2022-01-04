Name:           prere
Version:        0.0.5
Release:        1%{?dist}
Summary:        Utility to capture run data on shutdown
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       systemd
Requires:       bash

%description
Just a small little thing to save us from manually capturing (or just
forgetting to capture) run data before rebooting.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/dsio/%{name}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
cp %{name}.sh $RPM_BUILD_ROOT/opt/dsio/%{name}
cp %{name}.service $RPM_BUILD_ROOT%{_unitdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
/opt/dsio/%{name}
/opt/dsio/%{name}/%{name}.sh
%{_unitdir}/%{name}.service

%post
systemctl daemon-reload
systemctl enable %{name}.service
systemctl start %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
* Tue Dec  8 2021 Aaron C Thompson <aaron.c.thompson@jpl.nasa.gov> - 0.0.5
- Script now saves ALL run state logs under better names.
* Tue Dec  8 2021 Aaron C Thompson <aaron.c.thompson@jpl.nasa.gov> - 0.0.4
- Script now saves run state logs under better names.
* Tue Dec  8 2021 Aaron C Thompson <aaron.c.thompson@jpl.nasa.gov> - 0.0.3
- Fixing systemd unit for real this time, I promise
* Tue Dec  8 2021 Aaron C Thompson <aaron.c.thompson@jpl.nasa.gov> - 0.0.2
- Fixing systemd unit (text, not being enabled after install) properly
- Fixing uninstall
* Tue Dec  8 2021 Aaron C Thompson <aaron.c.thompson@jpl.nasa.gov> - 0.0.1
- First version being packaged
