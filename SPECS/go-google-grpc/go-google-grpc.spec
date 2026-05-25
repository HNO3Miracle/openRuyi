# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           grpc
%define go_import_path  google.golang.org/grpc
%define upstream_version  1.82.0-dev
# The upstream archive contains sibling Go modules. GOPATH-mode %gocheck would
# otherwise scan those module trees and pull in their separate Google Cloud,
# OpenCensus, and example dependency chains from the main grpc package.
# go-google-grpc and go-spiffe also mutually import each other's source packages;
# keep the runtime Requires on go-spiffe, but avoid a clean-project BuildRequires
# cycle and skip only grpc packages that directly need go-spiffe in %check. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/cmd/protoc-gen-go-grpc*
    %{go_import_path}/credentials/tls/certprovider*
    %{go_import_path}/credentials/xds*
    %{go_import_path}/examples*
    %{go_import_path}/gcp/observability*
    %{go_import_path}/internal/credentials/spiffe*
    %{go_import_path}/internal/credentials/xds*
    %{go_import_path}/internal/xds/balancer/clusterimpl*
    %{go_import_path}/internal/xds/bootstrap*
    %{go_import_path}/internal/xds/server*
    %{go_import_path}/interop/observability*
    %{go_import_path}/interop/xds*
    %{go_import_path}/security/advancedtls*
    %{go_import_path}/stats/opencensus*
    %{go_import_path}/test/tools*
    %{go_import_path}/xds*
}

Name:           go-google-grpc
Version:        1.82.0~dev
Release:        %autorelease
Summary:        Go implementation of gRPC
License:        Apache-2.0
URL:            https://github.com/grpc/grpc-go
#!RemoteAsset:  sha256:907c7003d53833492a87c98c1dbb3daf8806c5ff84a28029383d23cde25bf7e5
Source0:        https://github.com/grpc/grpc-go/archive/v%{upstream_version}.tar.gz#/%{_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# advancedtls FileWatcherCRLProvider fails in OBS with Go/OpenSSL certificate
# chain validation reporting "no unrevoked chains found: map[2:1]".
# - HNO3Miracle
Patch2000:      2000-skip-advancedtls-filewatcher-crl-provider-test.patch
# Go 1.26 vet reports %q argument type mismatches in several upstream grpc
# tests; keep tests enabled but disable vet. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/envoyproxy/go-control-plane)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/envoy)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/ratelimit)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/golang/glog)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/detectors/gcp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/oauth2/google)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gonum.org/v1/gonum)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(google.golang.org/grpc) = %{version}

Requires:       go(cel.dev/expr)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/cncf/xds/go)
Requires:       go(github.com/envoyproxy/go-control-plane)
Requires:       go(github.com/envoyproxy/go-control-plane/envoy)
Requires:       go(github.com/envoyproxy/go-control-plane/ratelimit)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/golang/glog)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
Requires:       go(github.com/spiffe/go-spiffe/v2)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib/detectors/gcp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/oauth2/google)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(gonum.org/v1/gonum)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/protobuf)

%description
grpc provides the Go implementation of gRPC.

# examples, stats/opencensus, security/advancedtls, and gcp/observability are
# nested Go modules packaged separately. Remove them from the main package to
# avoid file ownership conflicts while keeping the rest of grpc available.
%install -a
rm -rf %{buildroot}%{go_sys_gopath}/%{go_import_path}/examples \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/stats/opencensus \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/security/advancedtls \
       %{buildroot}%{go_sys_gopath}/%{go_import_path}/gcp/observability

%files
%doc CONTRIBUTING.md
%doc README.md
%license LICENSE
%license NOTICE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
