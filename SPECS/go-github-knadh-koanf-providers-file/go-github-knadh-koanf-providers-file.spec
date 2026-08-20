# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           file
%define go_import_path  github.com/knadh/koanf/providers/file

Name:           go-github-knadh-koanf-providers-file
Version:        1.2.1
Release:        %autorelease
Summary:        File provider for Koanf
License:        MIT
URL:            https://github.com/knadh/koanf
#!RemoteAsset:  sha256:fb34589db8c7e1001b39820389cb2297488045399c6c491feab4ebb468c57546
Source0:        https://github.com/knadh/koanf/archive/refs/tags/providers/file/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/fsnotify/fsnotify)

%description
This package provides the file provider module for Koanf.

%install
pushd providers/file
%buildsystem_golangmodules_install
popd

%check
pushd providers/file
%buildsystem_golangmodules_check
popd

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
