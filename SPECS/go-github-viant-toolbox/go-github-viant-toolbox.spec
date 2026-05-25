# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           toolbox
%define go_import_path  github.com/viant/toolbox

Name:           go-github-viant-toolbox
Version:        0.39.0
Release:        %autorelease
Summary:        Toolbox - go utility library
License:        Apache-2.0
URL:            https://github.com/viant/toolbox
#!RemoteAsset:  sha256:1614ed65aee9c027abf45aa37f1969842e0b081d4a1edc888a8551bc167fd1d1
Source0:        https://github.com/viant/toolbox/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Patch0:         2000-fix-non-constant-fmt-errorf.patch
Patch1:         2001-fix-time-format-test-12-hour-layout.patch
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n toolbox-%{version}
# TestCase_To currently expects VendorId, but current toolbox conversion
# returns Vendorid.
# TestLogger leaves a goroutine that calls os.Exit(0), which Go treats as
# "unexpected call to os.Exit(0) during test" in OBS.
BuildOption(check):  -skip 'TestCase_To|TestLogger'
# GCP storage/KMS backends require the large Google Cloud client stack; gojay
# only needs toolbox core/data/url, so keep those optional backend packages out
# of %check and hard dependencies.
%define go_test_exclude_glob %{shrink:
    github.com/viant/toolbox/kms/gcp
    github.com/viant/toolbox/storage/gs
}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/aws-sdk-go)
BuildRequires:  go(github.com/go-errors/errors)
BuildRequires:  go(github.com/lunixbochs/vtclean)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/viant/xunsafe)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/viant/toolbox) = %{version}

Requires:       go(github.com/aws/aws-sdk-go)
Requires:       go(github.com/go-errors/errors)
Requires:       go(github.com/lunixbochs/vtclean)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/viant/xunsafe)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/oauth2)
Requires:       go(gopkg.in/yaml.v2)

%description
Toolbox - go utility library

This library is compatible with Go 1.8+

Please refer to CHANGELOG.md (/CHANGELOG.md) if you encounter breaking

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE.txt
%license NOTICE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
