# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rouge_score
%global pypi_name rouge-score

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        %autorelease
Summary:        Pure Python implementation of ROUGE-1.5.5
License:        Apache-2.0
URL:            https://github.com/google-research/google-research/tree/master/rouge
#!RemoteAsset:  sha256:c7d4da2683e68c9abf0135ef915d63a46643666f848e558a1b9f7ead17ff0f04
Source0:        https://files.pythonhosted.org/packages/e2/c5/9136736c37022a6ad27fea38f3111eb8f02fe75d067f9a985cc358653102/rouge_score-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(absl-py)
BuildRequires:  python3dist(nltk)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.14.0
BuildRequires:  python3dist(wheel)

Provides:       python3-%{pypi_name}
Provides:       python3-%{pypi_name} = %{version}-%{release}

%description
rouge-score provides a pure Python implementation of ROUGE-1.5.5.

%generate_buildrequires
%pyproject_buildrequires

%check
%pyproject_check_import %{srcname}

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
