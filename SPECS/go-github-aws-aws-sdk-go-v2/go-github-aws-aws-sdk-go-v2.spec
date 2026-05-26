# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           aws-sdk-go-v2
%define go_import_path  github.com/aws/aws-sdk-go-v2
%define upstream_version  2026-05-21

Name:           go-github-aws-aws-sdk-go-v2
Version:        20260521
Release:        %autorelease
Summary:        AWS SDK for Go v2 core module
License:        Apache-2.0
URL:            https://github.com/aws/aws-sdk-go-v2
#!RemoteAsset:  sha256:68459245a574d7320592e7fd2575129de825acecfa0ab7b8f674261907c6887a
Source0:        https://github.com/aws/aws-sdk-go-v2/archive/release-%{upstream_version}.tar.gz#/%{_name}-release-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The release archive contains generated service and benchmark packages outside
# the core module surface packaged here; testing the whole archive pulls in
# unrelated v1 SDK and private smithy test helpers.
# Keep the SDK in one package. Debian and Fedora do not split aws-sdk-go-v2, and
# the upstream release archive already contains the service submodules; splitting
# them creates file ownership conflicts and unnecessary bootstrap cycles.
%define go_test_include %{shrink:
    github.com/aws/aws-sdk-go-v2
    github.com/aws/aws-sdk-go-v2/aws
    github.com/aws/aws-sdk-go-v2/aws/arn
    github.com/aws/aws-sdk-go-v2/aws/defaults
    github.com/aws/aws-sdk-go-v2/aws/middleware
    github.com/aws/aws-sdk-go-v2/aws/protocol/ec2query
    github.com/aws/aws-sdk-go-v2/aws/protocol/query
    github.com/aws/aws-sdk-go-v2/aws/protocol/restjson
    github.com/aws/aws-sdk-go-v2/aws/protocol/xml
    github.com/aws/aws-sdk-go-v2/aws/ratelimit
    github.com/aws/aws-sdk-go-v2/aws/retry
    github.com/aws/aws-sdk-go-v2/aws/retry/internal/mock
    github.com/aws/aws-sdk-go-v2/aws/signer/internal/v4
    github.com/aws/aws-sdk-go-v2/aws/signer/v4
    github.com/aws/aws-sdk-go-v2/aws/transport/http
    github.com/aws/aws-sdk-go-v2/internal/auth
    github.com/aws/aws-sdk-go-v2/internal/auth/smithy
    github.com/aws/aws-sdk-go-v2/internal/awstesting
    github.com/aws/aws-sdk-go-v2/internal/awstesting/unit
    github.com/aws/aws-sdk-go-v2/internal/awsutil
    github.com/aws/aws-sdk-go-v2/internal/context
    github.com/aws/aws-sdk-go-v2/internal/endpoints
    github.com/aws/aws-sdk-go-v2/internal/endpoints/awsrulesfn
    github.com/aws/aws-sdk-go-v2/internal/middleware
    github.com/aws/aws-sdk-go-v2/internal/protocoltest
    github.com/aws/aws-sdk-go-v2/internal/rand
    github.com/aws/aws-sdk-go-v2/internal/sdk
    github.com/aws/aws-sdk-go-v2/internal/sdkio
    github.com/aws/aws-sdk-go-v2/internal/shareddefaults
    github.com/aws/aws-sdk-go-v2/internal/strings
    github.com/aws/aws-sdk-go-v2/internal/sync/singleflight
    github.com/aws/aws-sdk-go-v2/internal/timeconv
}

BuildRequires:  go
BuildRequires:  go(github.com/aws/smithy-go)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/aws/aws-sdk-go-v2) = %{version}

Requires:       go(github.com/aws/smithy-go)

%description
This package provides AWS SDK for Go v2 core module.

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE.txt
%license NOTICE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
