# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           api
%define go_import_path  k8s.io/api
%define upstream_version  1.36.0-alpha2

Name:           go-k8s-api
Version:        1.36.0~alpha2
Release:        %autorelease
Summary:        The canonical location of the Kubernetes API definition.
License:        Apache-2.0
URL:            https://github.com/kubernetes/api
#!RemoteAsset:  sha256:16b686cba723e99ae024d8dd896a2211ee3b7d4ed836c4de6b03bc54181a2296
Source0:        https://github.com/kubernetes/api/archive/refs/tags/kubernetes-%{upstream_version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(k8s.io/api) = %{version}

Requires:       go(github.com/fxamacker/cbor/v2)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/modern-go/concurrent)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(github.com/x448/float16)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/text)
Requires:       go(gopkg.in/inf.v0)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kube-openapi)
Requires:       go(k8s.io/utils)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)

%description
| ⚠️ **This is an automatically published **staged repository
 | (https://git.k8s.io/kubernetes/staging#external-repository-staging-
 | area)**
 | for Kubernetes**. Contributions, including issues and pull requests,
 | should be made to the main Kubernetes repository:
 | https://github.com/kubernetes/kubernetes
 | (https://github.com/kubernetes/kubernetes). This repository is read-
 | only
 | for importing, and not used for direct contributions. See
 | CONTRIBUTING.md (/CONTRIBUTING.md) for more details.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
