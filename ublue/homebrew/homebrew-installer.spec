%global debug_package %{nil}

Name:           homebrew-installer
Version:        0.1.0
Release:        1%{?dist}
Summary:        Homebrew installer for Universal Blue systems

License:        BSD-2-Clause
URL:            https://github.com/ublue-os/packages
VCS:            {{{ git_dir_vcs }}}
Source:         {{{ git_dir_pack }}}

BuildRequires:  bubblewrap
BuildRequires:  ruby
BuildRequires:  sudo
Recommends:     ruby
Recommends:     gcc

%description
Homebrew installer for Universal Blue systems

%prep
{{{ git_dir_setup_macro }}}

%build
curl --retry 3 -Lo /tmp/brew-install https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh
chmod +x /tmp/brew-install
mkdir -p /tmp/fakehome
echo "root:x:0:0:root:/root:/bin/bash" > /tmp/fakepasswd
bwrap --unshare-all --share-net \
	--ro-bind /usr /usr \
	--ro-bind /lib /lib \
	--ro-bind /lib64 /lib64 \
	--ro-bind /tmp/fakepasswd /etc/passwd \
	--ro-bind /etc /etc \
	--bind /tmp /tmp \
	--bind /bin /bin \
	--bind /tmp/fakehome /home \
	--dev /dev \
	--proc /proc \
	--uid 0 \
	--gid 0 \
	/usr/bin/bash -c "touch /.dockerenv ; env --ignore-environment HOME=/home/linuxbrew NONINTERACTIVE=1 /tmp/brew-install"

mkdir -p %{buildroot}%{_datadir}
tar --zstd -cvf homebrew.tar.zst /tmp/fakehome/linuxbrew &>/dev/null

%install
install -Dm0755 homebrew.tar.zst %{buildroot}%{_datadir}/homebrew.tar.zst

%files
%{_datadir}/homebrew.tar.zst

%changelog
%autochangelog
