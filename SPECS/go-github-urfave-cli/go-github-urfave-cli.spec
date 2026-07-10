# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cli
%define go_import_path  github.com/urfave/cli

Name:           go-github-urfave-cli
Version:        1.22.17
Release:        %autorelease
Summary:        Framework for building command-line applications in Go
License:        MIT
URL:            https://github.com/urfave/cli
#!RemoteAsset:  sha256:44e20f78e0d399014591e1d0bd3c520dfff65a27ec2ad1310649eca5e56521e4
Source0:        https://github.com/urfave/cli/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/cpuguy83/go-md2man/v2)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/urfave/cli) = %{version}

Requires:       go(github.com/BurntSushi/toml)
Requires:       go(github.com/cpuguy83/go-md2man/v2)
Requires:       go(gopkg.in/yaml.v2)

%description
urfave/cli is a framework for building command-line applications in Go. It
provides commands, flags, help generation, shell completion, and alternative
configuration sources.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
