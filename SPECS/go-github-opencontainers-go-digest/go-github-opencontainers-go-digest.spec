# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-digest
%define go_import_path  github.com/opencontainers/go-digest
%define upstream_version  1.0.0-rc1

Name:           go-github-opencontainers-go-digest
Version:        1.0.0~rc1
Release:        %autorelease
Summary:        Common digest package used across the container ecosystem
License:        Apache-2.0 AND CC-BY-SA-4.0
URL:            https://github.com/opencontainers/go-digest
#!RemoteAsset:  sha256:3f511b32c46f60482644f0ad6a345f52e672c82164bfb08274f15f7c14cd3076
Source0:        https://github.com/opencontainers/go-digest/archive/refs/tags/v%{upstream_version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-digest-%{upstream_version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/opencontainers/go-digest) = %{version}

%description
go-digest

Report Card]

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE.code
%license LICENSE.docs
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
