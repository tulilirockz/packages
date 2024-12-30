%global debug_package %{nil}

Name:           ublue-setup-services
Version:        0.1.0
Release:        1%{?dist}
Summary:        Universal Blue setup services

License:        Apache-2.0
URL:            https://github.com/ublue-os/packages
VCS:            {{{ git_dir_vcs }}}
Source:         {{{ git_dir_pack }}}

BuildRequires:  systemd-rpm-macros

%description
Universal Blue setup scripts

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p %{buildroot}{%{_libexecdir},%{_unitdir},%{_sysconfdir}/{polkit-1/{rules.d,actions},profile.d}}
install -Dm0755 ./src/scripts/* %{buildroot}%{_libexecdir}
install -Dpm0644 ./src/services/* %{buildroot}%{_unitdir}
install -Dpm0644 ./src/polkit/*.rules %{buildroot}%{_sysconfdir}/polkit-1/rules.d
install -Dpm0644 ./src/polkit/*.policy %{buildroot}%{_sysconfdir}/polkit-1/actions
install -Dpm0755 ./src/profile/* %{buildroot}%{_sysconfdir}/profile.d

%post
%systemd_post ublue-user-setup.service
%systemd_post ublue-system-setup.service

%preun
%systemd_preun ublue-user-setup.service
%systemd_preun ublue-system-setup.service

%files
%{_libexecdir}/ublue-*
%{_libexecdir}/check-*
%{_sysconfdir}/polkit-1/rules.d/*
%{_sysconfdir}/polkit-1/actions/*
%{_sysconfdir}/profile.d/*
%{_unitdir}/*.service

%changelog
%autochangelog
