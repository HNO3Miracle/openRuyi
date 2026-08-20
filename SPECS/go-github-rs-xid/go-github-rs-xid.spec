# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xid
%define go_import_path  github.com/rs/xid

Name:           go-github-rs-xid
Version:        1.6.0
Release:        %autorelease
Summary:        Globally unique identifier generator for Go
License:        MIT
URL:            https://github.com/rs/xid
#!RemoteAsset:  sha256:dd4293a4934a37e6f4a1a31e3aa7d5c7dc2be23853697587774ca922b76a3822
Source0:        https://github.com/rs/xid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/rs/xid) = %{version}

%description
Xid generates compact, sortable, globally unique identifiers without shared
coordination.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
