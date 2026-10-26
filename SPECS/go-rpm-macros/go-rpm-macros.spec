# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# This is a personal OBS validation build for go-rpm-macros PR #2;
# it is not an official upstream 0.3 release.
%define _commit aba2d2b1fc43b82a41e4f2bc7381c8c2791367df

Name:           go-rpm-macros
Version:        0.3
Release:        %autorelease
Summary:        Go macros for openRuyi packaging
License:        MIT AND GPL-3.0-or-later
URL:            https://github.com/HNO3Miracle/go-rpm-macros/tree/aba2d2b1fc43b82a41e4f2bc7381c8c2791367df
#!RemoteAsset:  sha256:8f4e489c8eeb9efe312559cf6b03318c820664ea1d3dcd7da4976b896a2ff268
Source0:        https://github.com/HNO3Miracle/go-rpm-macros/archive/%{_commit}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package provides RPM macros for packaging Go software in openRuyi.

%prep
%autosetup -n %{name}-%{_commit}

# No build needed
%build

%install
install -D -m644 macros.golang %{buildroot}%{_rpmmacrodir}/macros.golang
install -D -m644 macros.buildsystem.golang %{buildroot}%{_rpmmacrodir}/macros.buildsystem.golang
install -D -m644 macros.buildsystem.golangmodules %{buildroot}%{_rpmmacrodir}/macros.buildsystem.golangmodules
install -D -m644 go.attr %{buildroot}%{_fileattrsdir}/go.attr
install -D -m755 go-rpm-integration %{buildroot}%{_rpmconfigdir}/go-rpm-integration

%check
bash -n go-rpm-integration

%files
%license LICENSE LICENSE.GPL-3.0-or-later
%doc LICENSES.md
%{_rpmmacrodir}/macros.golang
%{_rpmmacrodir}/macros.buildsystem.golang
%{_rpmmacrodir}/macros.buildsystem.golangmodules
%{_fileattrsdir}/go.attr
%{_rpmconfigdir}/go-rpm-integration

%changelog
%autochangelog
