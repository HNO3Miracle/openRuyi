# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           appengine
%define go_import_path  google.golang.org/appengine

Name:           go-google-appengine
Version:        2.0.6
Release:        %autorelease
Summary:        Go library for google.golang.org/appengine
License:        Apache-2.0
URL:            https://github.com/golang/appengine
#!RemoteAsset:  sha256:c6dff11b0af82470f79fd4a017de7b09574bfc73a0af1e65589357d22ea93f14
Source0:        https://github.com/golang/appengine/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n appengine-%{version}

BuildRequires:  go
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(google.golang.org/appengine) = %{version}

Requires:       go(github.com/golang/protobuf)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library google.golang.org/appengine.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
