# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golist
%define go_import_path  pagure.io/golist

Name:           golist
Version:        0.10.4
Release:        %autorelease
Summary:        List resources required and provided by Go projects
License:        BSD-3-Clause
URL:            https://pagure.io/golist
#!RemoteAsset:  sha256:84cb1a903032523738390783ad7092bf1e0ccf8663910b0bdbd729fb9bea3245
Source0:        https://pagure.io/golist/archive/v%{version}/%{_name}-v%{version}.tar.gz
BuildSystem:    golang

BuildOption(prep):  -n %{_name}-v%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/urfave/cli)

%description
golist analyzes Go source trees and lists the packages, dependencies, tests,
and source resources they contain. It is used by Go RPM packaging automation.

%build
%{go_common}
cd %{_builddir}/go/src/%{go_import_path}
export GOFLAGS="-buildmode=pie -trimpath"
%__go build %{go_build_flags_default} -o %{_builddir}/%{_name} ./cmd/golist

%install
install -D -m 0755 %{_builddir}/%{_name} %{buildroot}%{_bindir}/%{_name}

%check
%{go_common}
cd %{_builddir}/go/src/%{go_import_path}
%__go test %{go_test_flags_default} ./...

%files
%doc NEWS.md README.md
%license LICENSE
%{_bindir}/%{_name}

%changelog
%autochangelog
