%undefine _debugsource_packages
# Run tests in check section
# disable for bootstrapping
%bcond_with check

%global goipath github.com/linuxdeepin/go-x11-client

#gometa

Name:           golang-github-linuxdeepin-go-x11-client
Version:        1.0.2
Release:        1
Summary:        A X11 client Go bindings for Deepin Desktop Environment
License:        GPLv3
URL:            %{gourl}
Source0:        https://github.com/linuxdeepin/go-x11-client/archive/refs/tags/%{version}/go-x11-client-%{version}.tar.gz
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
%make_install

%if %{with check}
%check
%gochecks
%endif

%files
#doc README
%license LICENSE
%{_datadir}/gocode/src/github.com/linuxdeepin/go-x11-client/

%changelog
* Mon Nov 12 2018 mosquito <sensor.wen@gmail.com> - 0-0.8.20181112git8411934
- Update to 8411934
- New X connect failed: WindowError
  https://github.com/linuxdeepin/developer-center/issues/590

* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.7.20181104git0354113
- Update to 0354113

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 0-0.6.git71929bb
- Update to 71929bb

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 0-0.5.git70dbb86
- Update to 70dbb86

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gita10a839
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gita10a839
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 mosquito <sensor.wen@gmail.com> - 0-0.2.gita10a839
- Update to a10a839

* Sun Aug 27 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git67aca0b
- Initial package build
