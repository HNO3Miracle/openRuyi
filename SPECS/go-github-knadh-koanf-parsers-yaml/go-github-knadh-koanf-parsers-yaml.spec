# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           yaml
%define go_import_path  github.com/knadh/koanf/parsers/yaml

Name:           go-github-knadh-koanf-parsers-yaml
Version:        1.1.1
Release:        %autorelease
Summary:        YAML parser for Koanf
License:        MIT
URL:            https://github.com/knadh/koanf
#!RemoteAsset:  sha256:98f5720931cf855ae852759a3259f15c05b9c3f931bafab86bed698204298598
Source0:        https://github.com/knadh/koanf/archive/refs/tags/parsers/yaml/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(go.yaml.in/yaml/v3)

%description
This package provides the YAML parser module for Koanf.

%install
pushd parsers/yaml
%buildsystem_golangmodules_install
popd

%check
pushd parsers/yaml
%buildsystem_golangmodules_check
popd

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
