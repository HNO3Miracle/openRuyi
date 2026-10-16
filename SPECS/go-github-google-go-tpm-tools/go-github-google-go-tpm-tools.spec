# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-tpm-tools
%define go_import_path  github.com/google/go-tpm-tools
# Install the complete source tree, but defer TPM simulator integration tests.
%define go_test_exclude_glob %{go_import_path}*

Name:           go-github-google-go-tpm-tools
Version:        0.4.11
Release:        %autorelease
Summary:        TPM 2.0 support libraries, simulator, and attestation helpers
License:        Apache-2.0 AND BSD-2-Clause
URL:            https://github.com/google/go-tpm-tools
#!RemoteAsset:  sha256:050823ea0aa7bcc14a31f090ffb79bbb9ec5d96fadbb0094e63e75636b67fbe9
Source0:        https://github.com/google/go-tpm-tools/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
Provides:       go(github.com/google/go-tpm-tools) = %{version}
Provides:       go(github.com/google/go-tpm-tools/agent) = %{version}
Provides:       go(github.com/google/go-tpm-tools/client) = %{version}
Provides:       go(github.com/google/go-tpm-tools/cmd) = %{version}
Provides:       go(github.com/google/go-tpm-tools/keymanager) = %{version}
Provides:       go(github.com/google/go-tpm-tools/launcher) = %{version}
Provides:       go(github.com/google/go-tpm-tools/launcher/image/measure) = %{version}
Provides:       go(github.com/google/go-tpm-tools/proto/attest) = %{version}
Provides:       go(github.com/google/go-tpm-tools/proto/tpm) = %{version}
Provides:       go(github.com/google/go-tpm-tools/server) = %{version}
Provides:       go(github.com/google/go-tpm-tools/simulator) = %{version}
Provides:       go(github.com/google/go-tpm-tools/verifier) = %{version}

Requires:       pkgconfig(libcrypto)
Requires:       go(buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go)
Requires:       go(buf.build/go/protovalidate)
Requires:       go(cel.dev/expr)
Requires:       go(cloud.google.com/go)
Requires:       go(cloud.google.com/go/auth)
Requires:       go(cloud.google.com/go/auth/oauth2adapt)
Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(cloud.google.com/go/confidentialcomputing)
Requires:       go(cloud.google.com/go/logging)
Requires:       go(cloud.google.com/go/longrunning)
Requires:       go(cos.googlesource.com/cos/tools.git)
Requires:       go(cyphar.com/go-pathrs)
Requires:       go(github.com/AdaLogics/go-fuzz-headers)
Requires:       go(github.com/AdamKorcz/go-118-fuzz-build)
Requires:       go(github.com/GoogleCloudPlatform/confidential-space/server)
Requires:       go(github.com/GoogleCloudPlatform/key-protection-module)
Requires:       go(github.com/GoogleCloudPlatform/key-protection-module/keymanager/attestation_service)
Requires:       go(github.com/Microsoft/go-winio)
Requires:       go(github.com/Microsoft/hcsshim)
Requires:       go(github.com/NVIDIA/go-nvml)
Requires:       go(github.com/antlr4-go/antlr/v4)
Requires:       go(github.com/cenkalti/backoff/v4)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/containerd/cgroups/v3)
Requires:       go(github.com/containerd/containerd)
Requires:       go(github.com/containerd/containerd/api)
Requires:       go(github.com/containerd/containerd/v2)
Requires:       go(github.com/containerd/continuity)
Requires:       go(github.com/containerd/errdefs)
Requires:       go(github.com/containerd/errdefs/pkg)
Requires:       go(github.com/containerd/fifo)
Requires:       go(github.com/containerd/go-cni)
Requires:       go(github.com/containerd/log)
Requires:       go(github.com/containerd/platforms)
Requires:       go(github.com/containerd/ttrpc)
Requires:       go(github.com/containerd/typeurl/v2)
Requires:       go(github.com/containernetworking/cni)
Requires:       go(github.com/coreos/go-systemd/v22)
Requires:       go(github.com/cyphar/filepath-securejoin)
Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/distribution/reference)
Requires:       go(github.com/docker/go-events)
Requires:       go(github.com/felixge/httpsnoop)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-logr/stdr)
Requires:       go(github.com/godbus/dbus/v5)
Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/golang-jwt/jwt/v4)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/golang/protobuf)
Requires:       go(github.com/google/cel-go)
Requires:       go(github.com/google/gce-tcb-verifier)
Requires:       go(github.com/google/gce-tcb-verifier/gcetcbendorsement)
Requires:       go(github.com/google/go-attestation)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/go-configfs-tsm)
Requires:       go(github.com/google/go-eventlog)
Requires:       go(github.com/google/go-nvattest-tools)
Requires:       go(github.com/google/go-sev-guest)
Requires:       go(github.com/google/go-tdx-guest)
Requires:       go(github.com/google/go-tpm)
Requires:       go(github.com/google/logger)
Requires:       go(github.com/google/s2a-go)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/googleapis/enterprise-certificate-proxy)
Requires:       go(github.com/googleapis/gax-go/v2)
Requires:       go(github.com/inconshreveable/mousetrap)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/mdlayher/socket)
Requires:       go(github.com/mdlayher/vsock)
Requires:       go(github.com/moby/locker)
Requires:       go(github.com/moby/sys/mountinfo)
Requires:       go(github.com/moby/sys/sequential)
Requires:       go(github.com/moby/sys/signal)
Requires:       go(github.com/moby/sys/user)
Requires:       go(github.com/moby/sys/userns)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(github.com/opencontainers/runtime-spec)
Requires:       go(github.com/opencontainers/selinux)
Requires:       go(github.com/petermattis/goid)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/pmezard/go-difflib)
Requires:       go(github.com/sasha-s/go-deadlock)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/stretchr/testify)
Requires:       go(go.opencensus.io)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
Requires:       go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/otel/metric)
Requires:       go(go.opentelemetry.io/otel/trace)
Requires:       go(go.uber.org/multierr)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/time)
Requires:       go(google.golang.org/api)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/api)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description
Go-TPM tools provides client and server libraries for TPM 2.0 operations,
attestation verification, and a software TPM simulator. This source package
also includes the agent, launcher, key manager, verifier, and command modules.

# All nested module paths match their directories below the root module.
# The standard GOPATH install and check therefore cover the complete tree.

%files
%doc README.md simulator/README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
