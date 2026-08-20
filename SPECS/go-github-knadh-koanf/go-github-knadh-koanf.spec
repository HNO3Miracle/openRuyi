# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           koanf
%define go_import_path  github.com/knadh/koanf
# Current godotenv and go-toml output differs from the v1.5.0 golden files.
%define go_test_exclude %{shrink:
    %{go_import_path}/parsers/dotenv
    %{go_import_path}/parsers/toml
}

Name:           go-github-knadh-koanf
Version:        1.5.0
Release:        %autorelease
Summary:        Extensible configuration management library for Go
License:        MIT
URL:            https://github.com/knadh/koanf
#!RemoteAsset:  sha256:e451f971636d67fbc5dbf84850f2ea5d20cda3bf24646e727b60bed878c5f28a
Source0:        https://github.com/knadh/koanf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/fatih/structs)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/hashicorp/consul/api)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/hashicorp/vault/api)
BuildRequires:  go(github.com/hjson/hjson-go/v4)
BuildRequires:  go(github.com/joho/godotenv)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/npillmayer/nestext)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/rhnvrm/simples3)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.etcd.io/etcd/client/v3)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/fatih/structs)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/hashicorp/consul/api)
Requires:       go(github.com/hashicorp/hcl)
Requires:       go(github.com/hashicorp/vault/api)
Requires:       go(github.com/hjson/hjson-go/v4)
Requires:       go(github.com/joho/godotenv)
Requires:       go(github.com/mitchellh/copystructure)
Requires:       go(github.com/mitchellh/mapstructure)
Requires:       go(github.com/npillmayer/nestext)
Requires:       go(github.com/pelletier/go-toml)
Requires:       go(github.com/rhnvrm/simples3)
Requires:       go(github.com/spf13/pflag)
Requires:       go(go.etcd.io/etcd/client/v3)
Requires:       go(gopkg.in/yaml.v3)

%description
Koanf reads configuration from multiple sources and formats through a
lightweight, extensible Go API.

%check -a
# Compile packages excluded from runtime tests.
go test -run '^$' %{go_test_exclude}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}
%exclude %{go_sys_gopath}/%{go_import_path}/maps
%exclude %{go_sys_gopath}/%{go_import_path}/parsers/yaml
%exclude %{go_sys_gopath}/%{go_import_path}/providers/confmap
%exclude %{go_sys_gopath}/%{go_import_path}/providers/env
%exclude %{go_sys_gopath}/%{go_import_path}/providers/file
%exclude %{go_sys_gopath}/%{go_import_path}/providers/fs
%exclude %{go_sys_gopath}/%{go_import_path}/providers/rawbytes
%exclude %{go_sys_gopath}/%{go_import_path}/v2

%changelog
%autochangelog
