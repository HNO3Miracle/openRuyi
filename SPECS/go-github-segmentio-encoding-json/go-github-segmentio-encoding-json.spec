# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           json
%define go_import_path  github.com/segmentio/encoding
%define commit_id 7d5a25dbc5da13aed3cb047a127e4d0e96f536fb

Name:           go-github-segmentio-encoding-json
Version:        0+git20260310.7d5a25d
Release:        %autorelease
Summary:        Go package containing implementations of efficient encoding, decoding, and validation APIs.
License:        MIT
URL:            https://github.com/segmentio/encoding
#!RemoteAsset:  sha256:2b6eddfbce47064dcf003dc5b982c3ccf5abecf93e19318da0dc0105bad12227
Source0:        https://github.com/segmentio/encoding/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# json/fuzz imports the historical go-fuzz corpus helper package, which is no
# longer present in the upstream corpus repository; keep normal packages tested.
%define go_test_exclude_glob github.com/segmentio/encoding/json/fuzz

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/segmentio/asm)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/segmentio/encoding) = %{version}

Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/segmentio/asm)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/protobuf)

%description

Go package containing implementations of encoders and decoders for
various data formats.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
