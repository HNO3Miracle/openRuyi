# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cos-tools
%define go_import_path  cos.googlesource.com/cos/tools.git
%define commit_id       ad81f54f364a837faa7576f1cb373a3a2c780f15

Name:           go-cos.googlesource-cos-tools
Version:        0+git20261023.ad81f54
Release:        %autorelease
Summary:        Container-Optimized OS tooling and support libraries
License:        Apache-2.0
URL:            https://cos.googlesource.com/cos/tools
#!RemoteAsset:  sha256:46852b3d8869516485d651ca0740fa73257ffe9a1b0217b843912b3de1e54453
Source0:        https://cos.googlesource.com/cos/tools/+archive/%{commit_id}.tar.gz#/tools-%{commit_id}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Gitiles archives contain the repository files without a top-level directory.
BuildOption(prep):  -c -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(cloud.google.com/go)
BuildRequires:  go(cloud.google.com/go/auth)
BuildRequires:  go(cloud.google.com/go/auth/oauth2adapt)
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/iam)
BuildRequires:  go(cloud.google.com/go/kms)
BuildRequires:  go(cloud.google.com/go/logging)
BuildRequires:  go(cloud.google.com/go/longrunning)
BuildRequires:  go(cloud.google.com/go/monitoring)
BuildRequires:  go(cloud.google.com/go/secretmanager)
BuildRequires:  go(cloud.google.com/go/storage)
BuildRequires:  go(github.com/GoogleCloudPlatform/cloudsql-proxy)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric)
BuildRequires:  go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping)
BuildRequires:  go(github.com/Microsoft/go-winio)
BuildRequires:  go(github.com/Microsoft/hcsshim)
BuildRequires:  go(github.com/anchore/go-struct-converter)
BuildRequires:  go(github.com/andygrunwald/go-gerrit)
BuildRequires:  go(github.com/beevik/etree)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cncf/xds/go)
BuildRequires:  go(github.com/containerd/cgroups/v3)
BuildRequires:  go(github.com/containerd/containerd/api)
BuildRequires:  go(github.com/containerd/containerd/v2)
BuildRequires:  go(github.com/containerd/continuity)
BuildRequires:  go(github.com/containerd/errdefs)
BuildRequires:  go(github.com/containerd/errdefs/pkg)
BuildRequires:  go(github.com/containerd/fifo)
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/containerd/platforms)
BuildRequires:  go(github.com/containerd/plugin)
BuildRequires:  go(github.com/containerd/ttrpc)
BuildRequires:  go(github.com/containerd/typeurl/v2)
BuildRequires:  go(github.com/cpuguy83/go-md2man/v2)
BuildRequires:  go(github.com/distribution/reference)
BuildRequires:  go(github.com/envoyproxy/go-control-plane/envoy)
BuildRequires:  go(github.com/envoyproxy/protoc-gen-validate)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-jose/go-jose/v4)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/glog)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/golang/mock)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-querystring)
BuildRequires:  go(github.com/google/s2a-go)
BuildRequires:  go(github.com/google/subcommands)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/googleapis/enterprise-certificate-proxy)
BuildRequires:  go(github.com/googleapis/gax-go/v2)
BuildRequires:  go(github.com/gorilla/securecookie)
BuildRequires:  go(github.com/gorilla/sessions)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/julienschmidt/httprouter)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/moby/locker)
BuildRequires:  go(github.com/moby/sys/mountinfo)
BuildRequires:  go(github.com/moby/sys/sequential)
BuildRequires:  go(github.com/moby/sys/signal)
BuildRequires:  go(github.com/moby/sys/user)
BuildRequires:  go(github.com/moby/sys/userns)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/opencontainers/runtime-spec)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/planetscale/vtprotobuf)
BuildRequires:  go(github.com/russross/blackfriday/v2)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/smartystreets/assertions)
BuildRequires:  go(github.com/smartystreets/goconvey)
BuildRequires:  go(github.com/spdx/tools-golang)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/spiffe/go-spiffe/v2)
BuildRequires:  go(github.com/urfave/cli/v2)
BuildRequires:  go(github.com/xrash/smetrics)
BuildRequires:  go(go.chromium.org/luci)
BuildRequires:  go(go.opencensus.io)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/detectors/gcp)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/sdk)
BuildRequires:  go(go.opentelemetry.io/otel/sdk/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/api)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(cos.googlesource.com/cos/tools.git) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/changelog-webapp/controllers) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_dkms/actions) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_gpu_driver_builder/internal/builder) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_gpu_driver_builder/internal/config) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_gpu_installer/deviceinfo) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_gpu_installer/features) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_gpu_installer/internal/commands) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_gpu_installer/internal/installer) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_gpu_installer/internal/signing) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_gpu_installer/versions) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_image_analyzer/internal/binary) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_image_analyzer/internal/input) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_image_analyzer/internal/output) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_image_analyzer/internal/packagediff) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_image_analyzer/internal/utilities) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/cmd/cos_kernel/actions) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/changelog) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/config) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/containers) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/cos) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/cosboot) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/dkms) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/fakes) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/findbuild) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/fs) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/gce) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/gcs) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/git) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/gpubuild) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/gpuconfig) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/gpuconfig/pb) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/kernel) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/modules) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/nodeprofiler/cloudlogger) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/nodeprofiler/profiler) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/nodeprofiler/utils) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/oempreloader) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/ovaconverter) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/preloader) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/provisioner) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/tools) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/tools/partutil) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/tools/partutil/partutiltest) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/tools/sbomutil) = %{version}
Provides:       go(cos.googlesource.com/cos/tools.git/src/pkg/utils) = %{version}

Requires:       go(cel.dev/expr)
Requires:       go(cloud.google.com/go)
Requires:       go(cloud.google.com/go/auth)
Requires:       go(cloud.google.com/go/auth/oauth2adapt)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(cloud.google.com/go/iam)
Requires:       go(cloud.google.com/go/kms)
Requires:       go(cloud.google.com/go/logging)
Requires:       go(cloud.google.com/go/longrunning)
Requires:       go(cloud.google.com/go/monitoring)
Requires:       go(cloud.google.com/go/secretmanager)
Requires:       go(cloud.google.com/go/storage)
Requires:       go(github.com/GoogleCloudPlatform/cloudsql-proxy)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric)
Requires:       go(github.com/GoogleCloudPlatform/opentelemetry-operations-go/internal/resourcemapping)
Requires:       go(github.com/Microsoft/go-winio)
Requires:       go(github.com/Microsoft/hcsshim)
Requires:       go(github.com/anchore/go-struct-converter)
Requires:       go(github.com/andygrunwald/go-gerrit)
Requires:       go(github.com/beevik/etree)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/cncf/xds/go)
Requires:       go(github.com/containerd/cgroups/v3)
Requires:       go(github.com/containerd/containerd/api)
Requires:       go(github.com/containerd/containerd/v2)
Requires:       go(github.com/containerd/continuity)
Requires:       go(github.com/containerd/errdefs)
Requires:       go(github.com/containerd/errdefs/pkg)
Requires:       go(github.com/containerd/fifo)
Requires:       go(github.com/containerd/log)
Requires:       go(github.com/containerd/platforms)
Requires:       go(github.com/containerd/plugin)
Requires:       go(github.com/containerd/ttrpc)
Requires:       go(github.com/containerd/typeurl/v2)
Requires:       go(github.com/cpuguy83/go-md2man/v2)
Requires:       go(github.com/distribution/reference)
Requires:       go(github.com/envoyproxy/go-control-plane/envoy)
Requires:       go(github.com/envoyproxy/protoc-gen-validate)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-jose/go-jose/v4)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/go-sql-driver/mysql)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang/glog)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/mock)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-querystring)
Requires:       go(github.com/google/s2a-go)
Requires:       go(github.com/google/subcommands)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/gorilla/securecookie)
Requires:       go(github.com/gorilla/sessions)
Requires:       go(github.com/inconshreveable/mousetrap)
Requires:       go(github.com/julienschmidt/httprouter)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/moby/locker)
Requires:       go(github.com/moby/sys/mountinfo)
Requires:       go(github.com/moby/sys/sequential)
Requires:       go(github.com/moby/sys/signal)
Requires:       go(github.com/moby/sys/user)
Requires:       go(github.com/moby/sys/userns)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(github.com/opencontainers/runtime-spec)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/planetscale/vtprotobuf)
Requires:       go(github.com/russross/blackfriday/v2)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/smartystreets/assertions)
Requires:       go(github.com/smartystreets/goconvey)
Requires:       go(github.com/spdx/tools-golang)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/spiffe/go-spiffe/v2)
Requires:       go(github.com/urfave/cli/v2)
Requires:       go(github.com/xrash/smetrics)
Requires:       go(go.chromium.org/luci)
Requires:       go(go.opencensus.io)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib/detectors/gcp)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/sdk)
Requires:       go(go.opentelemetry.io/otel/sdk/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.uber.org/atomic)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
This package contains the complete COS tools repository, including shared
libraries, image customization tooling, tests, and their supporting data.
The src directory is part of the upstream Go import paths and is retained.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
