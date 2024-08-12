%undefine _debugsource_packages
# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/linuxdeepin/go-x11-client

#gometa

Name:           golang-github-linuxdeepin-go-x11-client
Version:        1.0.2
Release:        2
Summary:        A X11 client Go bindings for Deepin Desktop Environment
License:        GPLv3
URL:            %{gourl}
Source0:        https://github.com/linuxdeepin/go-x11-client/archive/refs/tags/%{version}/go-x11-client-%{version}.tar.gz
BuildRequires:	compiler(golang)

%description
%{summary}.

%package devel
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  golang
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  golang(golang.org/x/text/encoding/charmap)
BuildRequires:  golang(github.com/stretchr/testify/assert)

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%autosetup -p1 -n go-x11-client-%{version}

export GOPATH=$(pwd)/.godeps:$(pwd)/gopath

GOPATH=/usr/share/gocode make

%install
#make_install
%goinstall

%if %{with check}
%check
%gochecks
%endif

%files
#doc README
%license LICENSE
%{_datadir}/gocode/src/github.com/linuxdeepin/go-x11-client/
