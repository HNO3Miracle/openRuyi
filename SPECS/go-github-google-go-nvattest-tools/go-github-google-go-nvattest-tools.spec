# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-nvattest-tools
%define go_import_path  github.com/google/go-nvattest-tools
%define commit_id       1a098bebccd3790f71e7e6403c4f15a85f0a3494

Name:           go-github-google-go-nvattest-tools
Version:        0+git20261022.1a098be
Release:        %autorelease
Summary:        NVIDIA GPU and NVSwitch attestation libraries for Go
# The NSCQ headers carry NVIDIA's notice rather than the project license.
License:        Apache-2.0 AND LicenseRef-NVIDIA-NSCQ
URL:            https://github.com/google/go-nvattest-tools
#!RemoteAsset:  sha256:6a7504503c0635d17eb346533123ea882fdec93fbbdd3792e9e1639c03478e92
Source0:        https://github.com/google/go-nvattest-tools/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  gcc
BuildRequires:  go >= 1.25
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  go(github.com/NVIDIA/go-nvml)
BuildRequires:  go(github.com/beevik/etree) >= 1.6.0
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/subcommands)
BuildRequires:  go(github.com/jonboulle/clockwork)
BuildRequires:  go(github.com/kr/text)
# go.mod uses atulpatildbz/libxml2@d06374c0f56f and
# atulpatildbz/goxmldsig@e806be5e3c3a under these original module paths.
BuildRequires:  go(github.com/lestrrat-go/libxml2)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/russellhaering/goxmldsig)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/abi) = %{version}
Provides:       go(%{go_import_path}/client) = %{version}
Provides:       go(%{go_import_path}/internal/nvnscq/pkg/nscq) = %{version}
Provides:       go(%{go_import_path}/internal/nvnscq/pkg/nscq/mock) = %{version}
Provides:       go(%{go_import_path}/mpt) = %{version}
Provides:       go(%{go_import_path}/ppcie/client) = %{version}
Provides:       go(%{go_import_path}/ppcie/server) = %{version}
Provides:       go(%{go_import_path}/proto) = %{version}
Provides:       go(%{go_import_path}/proto/nvattest) = %{version}
Provides:       go(%{go_import_path}/proto/nvocsp) = %{version}
Provides:       go(%{go_import_path}/proto/nvrim) = %{version}
Provides:       go(%{go_import_path}/server/cert) = %{version}
Provides:       go(%{go_import_path}/server/ocsp) = %{version}
Provides:       go(%{go_import_path}/server/ocsp/nvidiaocsp) = %{version}
Provides:       go(%{go_import_path}/server/rim) = %{version}
Provides:       go(%{go_import_path}/server/rim/nvidiarim) = %{version}
Provides:       go(%{go_import_path}/server/utility) = %{version}
Provides:       go(%{go_import_path}/server/validate) = %{version}
Provides:       go(%{go_import_path}/server/verify) = %{version}
Provides:       go(%{go_import_path}/spt) = %{version}
Provides:       go(%{go_import_path}/testing) = %{version}
Provides:       go(%{go_import_path}/testing/testdata) = %{version}

Requires:       pkgconfig(libxml-2.0)
Requires:       go(github.com/NVIDIA/go-nvml)
Requires:       go(github.com/beevik/etree) >= 1.6.0
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/subcommands)
Requires:       go(github.com/jonboulle/clockwork)
Requires:       go(github.com/lestrrat-go/libxml2)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/russellhaering/goxmldsig)
Requires:       go(go.uber.org/multierr)
Requires:       go(golang.org/x/crypto)
Requires:       go(google.golang.org/protobuf)

%description
Go libraries for collecting and verifying NVIDIA GPU and NVSwitch attestation
reports, certificates, measurements, and topology. The complete source tree
includes protocol types, verification helpers, command sources, and test data.

%check -a
# Go's recursive package pattern omits testdata directories, but this fixture
# package has its own tests in addition to the repository's default suite.
%go_common
%__go test %{go_test_flags_default} %{go_import_path}/testing/testdata

%files
%doc README.md
%license LICENSE
%license internal/nvnscq/pkg/nscq/nscq.h
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
