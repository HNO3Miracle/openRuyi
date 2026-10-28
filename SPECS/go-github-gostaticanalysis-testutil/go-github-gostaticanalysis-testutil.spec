# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testutil
%define go_import_path  github.com/gostaticanalysis/testutil

Name:           go-github-gostaticanalysis-testutil
Version:        0.6.1
Release:        %autorelease
Summary:        Test utilities for Go static analysis packages
License:        MIT
URL:            https://github.com/gostaticanalysis/testutil
#!RemoteAsset:  sha256:23d4db8b6e047d92517c2b2cce5bf20ded7c02096bc81ee944c40297024f9d24
Source0:        https://github.com/gostaticanalysis/testutil/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Module operations must remain enabled when the caller uses GOPATH mode.
Patch2000:      2000-enable-module-mode-for-go-subprocesses.patch

BuildRequires:  go >= 1.24.1
BuildRequires:  go-rpm-macros
# Keep the dependencies of the issue00023 regression fixture as well as
# the root module's direct, indirect, and test dependencies.
BuildRequires:  go(cel.dev/expr)
BuildRequires:  go(filippo.io/edwards25519)
BuildRequires:  go(github.com/antlr4-go/antlr/v4)
BuildRequires:  go(github.com/cubicdaiya/gonp)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/fatih/structtag)
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/google/cel-go)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/jackc/pgpassfile)
BuildRequires:  go(github.com/jackc/pgservicefile)
BuildRequires:  go(github.com/jackc/pgx/v5)
BuildRequires:  go(github.com/jackc/puddle/v2)
BuildRequires:  go(github.com/jinzhu/inflection)
BuildRequires:  go(github.com/josharian/mapfs)
BuildRequires:  go(github.com/josharian/txtarfs)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/ncruces/go-strftime)
BuildRequires:  go(github.com/newmo-oss/gotestingmock)
BuildRequires:  go(github.com/otiai10/copy)
BuildRequires:  go(github.com/otiai10/mint)
BuildRequires:  go(github.com/pganalyze/pg_query_go/v5)
BuildRequires:  go(github.com/pingcap/errors)
BuildRequires:  go(github.com/pingcap/failpoint)
BuildRequires:  go(github.com/pingcap/log)
BuildRequires:  go(github.com/pingcap/tidb/pkg/parser)
BuildRequires:  go(github.com/remyoudompheng/bigfft)
BuildRequires:  go(github.com/riza-io/grpc-go)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/sqlc-dev/sqlc)
BuildRequires:  go(github.com/stoewer/go-strcase)
BuildRequires:  go(github.com/tenntenn/golden)
BuildRequires:  go(github.com/tenntenn/modver)
BuildRequires:  go(github.com/tenntenn/text/transform)
BuildRequires:  go(github.com/tetratelabs/wazero)
BuildRequires:  go(github.com/wasilibs/go-pgquery)
BuildRequires:  go(github.com/wasilibs/wazero-helpers)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/mod/modfile)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/text/transform)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/analysis)
BuildRequires:  go(golang.org/x/tools/go/analysis/analysistest)
BuildRequires:  go(golang.org/x/tools/txtar)
BuildRequires:  go(google.golang.org/genproto/googleapis/api)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(modernc.org/libc)
BuildRequires:  go(modernc.org/mathutil)
BuildRequires:  go(modernc.org/memory)
BuildRequires:  go(modernc.org/sqlite)

# Export the source module roots and every installed Go package.
Provides:       go(github.com/gostaticanalysis/testutil) = %{version}

Requires:       go(github.com/otiai10/copy)
Requires:       go(github.com/tenntenn/modver)
Requires:       go(github.com/tenntenn/text/transform)
Requires:       go(golang.org/x/mod/modfile)
Requires:       go(golang.org/x/text/transform)
Requires:       go(golang.org/x/tools/go/analysis)
Requires:       go(golang.org/x/tools/go/analysis/analysistest)
Requires:       go(golang.org/x/tools/txtar)

%description
Test utilities for Go static analysis packages. This package contains the
complete upstream repository sources and tests.

# Keep fixture module operations offline and use the installed Go toolchain.
%check -p
export GOPROXY=off
export GOSUMDB=off
export GOTOOLCHAIN=local

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
