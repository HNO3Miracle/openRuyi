# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           utils
%define go_import_path  k8s.io/utils
%define commit_id ff6756f316d28f49a7aab7ba7dddb0e526a1e35b

Name:           go-k8s-utils
Version:        0+git20260507.ff6756f
Release:        %autorelease
Summary:        Go library for k8s.io/utils
License:        Apache-2.0
URL:            https://github.com/kubernetes/utils
#!RemoteAsset:  sha256:0882bdac456bcf478979c8fec6ae802f29c531a4b317b2286f569f0c84887fa2
Source0:        https://github.com/kubernetes/utils/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# TestLogIfLong is timing-sensitive and did not emit the expected trace log in OBS.
%define go_test_exclude k8s.io/utils/trace

BuildRequires:  go
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go-k8s-klog-v2
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go-rpm-macros

Provides:       go(k8s.io/utils) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/go-logr/logr)
Requires:       go(k8s.io/klog/v2)

%description
This package provides the Go library k8s.io/utils.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
