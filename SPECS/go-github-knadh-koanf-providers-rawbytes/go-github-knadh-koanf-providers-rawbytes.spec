# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rawbytes
%define go_import_path  github.com/knadh/koanf/providers/rawbytes

Name:           go-github-knadh-koanf-providers-rawbytes
Version:        1.0.1
Release:        %autorelease
Summary:        Raw byte provider for Koanf
License:        MIT
URL:            https://github.com/knadh/koanf
#!RemoteAsset:  sha256:2a678443fca9dc1749aa969abb98b3223033e430d7b81299ccd61270085d2deb
Source0:        https://github.com/knadh/koanf/archive/refs/tags/providers/rawbytes/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides a Koanf provider that loads raw byte data.

%install
install -d "%{buildroot}%{go_sys_gopath}/%{go_import_path}"
cp -a providers/rawbytes/. "%{buildroot}%{go_sys_gopath}/%{go_import_path}/"

%check
pushd providers/rawbytes
%buildsystem_golangmodules_check
popd

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
