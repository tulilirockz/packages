%global debug_package %{nil}
%global vendor bluefin

Name:           bluefin-wallpapers
Version:        0.1.0
Release:        1%{?dist}
Summary:        Bluefin wallpapers

License:        CC-BY-CA
URL:            https://github.com/ublue-os/packages
VCS:           {{{ git_dir_vcs }}}
Source:        {{{ git_dir_pack }}}

%description
Bluefin wallpapers

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p -m0755 \
    %{buildroot}%{_datadir}/backgrounds/%{vendor} \
    %{buildroot}%{_datadir}/gnome-background-properties \
    %{buildroot}%{_datadir}/wallpapers/${vendor}
mv src/*.xml %{buildroot}%{_datadir}/gnome-background-properties
mv src/* %{buildroot}%{_datadir}/backgrounds/%{vendor}

%files
%attr(0755,root,root) %{_datadir}/backgrounds/%{vendor}/*
%attr(0755,root,root) %{_datadir}/gnome-background-properties/*.xml

%changelog
%autochangelog
