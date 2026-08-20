# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ole
%define go_import_path  github.com/go-ole/go-ole

Name:           go-github-go-ole-go-ole
Version:        1.2.6
Release:        %autorelease
Summary:        Go bindings for Windows COM
License:        MIT
URL:            https://github.com/go-ole/go-ole
#!RemoteAsset:  sha256:8f8ae1e3a71c1aa16fcd59b409e498dbec41c3ed23aec81e26edea275670db60
Source0:        https://github.com/go-ole/go-ole/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/go-ole/go-ole) = %{version}

Requires:       go(golang.org/x/sys)

%description
Go OLE provides Go bindings for Windows COM using shared libraries instead of
cgo.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
