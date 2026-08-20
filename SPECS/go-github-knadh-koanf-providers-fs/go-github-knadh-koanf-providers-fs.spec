# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fs
%define go_import_path  github.com/knadh/koanf/providers/fs

Name:           go-github-knadh-koanf-providers-fs
Version:        1.0.1
Release:        %autorelease
Summary:        Filesystem provider for Koanf
License:        MIT
URL:            https://github.com/knadh/koanf
#!RemoteAsset:  sha256:adf77dbf2b442645a059fecd25412c75c9a574bbfe1ef3785c8355ebb5219b2f
Source0:        https://github.com/knadh/koanf/archive/refs/tags/providers/fs/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This package provides the filesystem provider module for Koanf.

%install
pushd providers/fs
%buildsystem_golangmodules_install
popd

%check
pushd providers/fs
%buildsystem_golangmodules_check
popd

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
