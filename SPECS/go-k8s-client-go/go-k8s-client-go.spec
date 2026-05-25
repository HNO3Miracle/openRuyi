# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           client-go
%define go_import_path  k8s.io/client-go
%define upstream_version  1.36.0-alpha2

Name:           go-k8s-client-go
Version:        1.36.0~alpha2
Release:        %autorelease
Summary:        Go client for Kubernetes.
License:        Apache-2.0
URL:            https://github.com/kubernetes/client-go
#!RemoteAsset:  sha256:b5727b2717ef2f83af80607c47995d4b31874cbb0b42a886df91df58ad088328
Source0:        https://github.com/kubernetes/client-go/archive/refs/tags/kubernetes-%{upstream_version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n client-go-kubernetes-%{upstream_version}
# k8s.io/client-go/testing/internal and k8s.io/client-go/tools/cache use
# testing/synctest; OBS builds run with asynctimerchan!=0, which makes
# synctest.Run panic with "synctest.Run not supported with asynctimerchan!=0".
# k8s.io/client-go/tools/remotecommand HTTPS proxy tests fail in OBS with
# "proxy: unknown scheme: https"; keep the rest of client-go tests enabled.
%define go_test_exclude %{shrink:
    %{go_import_path}/testing/internal
    %{go_import_path}/tools/cache
    %{go_import_path}/tools/remotecommand
}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/emicklei/go-restful/v3)
BuildRequires:  go(github.com/fxamacker/cbor/v2)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/google/btree)
BuildRequires:  go(github.com/google/gnostic-models)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/josharian/intern)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/mailru/easyjson)
BuildRequires:  go(github.com/moby/spdystream)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/mxk/go-flowrate)
BuildRequires:  go(github.com/peterbourgon/diskv)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/objx)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/x448/float16)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/evanphx/json-patch.v4)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(k8s.io/api)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(k8s.io/klog/v2)
BuildRequires:  go(k8s.io/kube-openapi)
BuildRequires:  go(k8s.io/utils)
BuildRequires:  go(sigs.k8s.io/json)
BuildRequires:  go(sigs.k8s.io/randfill)
BuildRequires:  go(sigs.k8s.io/structured-merge-diff/v6)
BuildRequires:  go(sigs.k8s.io/yaml)

Provides:       go(k8s.io/client-go) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/emicklei/go-restful/v3)
Requires:       go(github.com/fxamacker/cbor/v2)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/go-openapi/jsonreference)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/google/btree)
Requires:       go(github.com/google/gnostic-models)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/gorilla/websocket)
Requires:       go(github.com/josharian/intern)
Requires:       go(github.com/json-iterator/go)
Requires:       go(github.com/mailru/easyjson)
Requires:       go(github.com/moby/spdystream)
Requires:       go(github.com/modern-go/concurrent)
Requires:       go(github.com/modern-go/reflect2)
Requires:       go(github.com/munnerz/goautoneg)
Requires:       go(github.com/mxk/go-flowrate)
Requires:       go(github.com/peterbourgon/diskv)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/x448/float16)
Requires:       go(go.yaml.in/yaml/v2)
Requires:       go(go.yaml.in/yaml/v3)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/evanphx/json-patch.v4)
Requires:       go(gopkg.in/inf.v0)
Requires:       go(gopkg.in/yaml.v3)
Requires:       go(k8s.io/api)
Requires:       go(k8s.io/apimachinery)
Requires:       go(k8s.io/klog/v2)
Requires:       go(k8s.io/kube-openapi)
Requires:       go(k8s.io/utils)
Requires:       go(sigs.k8s.io/json)
Requires:       go(sigs.k8s.io/randfill)
Requires:       go(sigs.k8s.io/structured-merge-diff/v6)
Requires:       go(sigs.k8s.io/yaml)

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
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
