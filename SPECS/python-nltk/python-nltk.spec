# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nltk

Name:           python-%{srcname}
Version:        3.9.2
Release:        %autorelease
Summary:        Natural Language Toolkit
License:        Apache-2.0
URL:            https://www.nltk.org/
#!RemoteAsset:  sha256:0f409e9b069ca4177c1903c3e843eef90c7e92992fa4931ae607da6de49e1419
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(regex) >= 2021.8.3
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname}
Provides:       python3-%{srcname} = %{version}-%{release}

%description
NLTK provides a broad collection of libraries and tools for natural language
processing.

%generate_buildrequires
%pyproject_buildrequires

%check
# Exclude modules that require external NLTK corpora or optional integrations
# during import. Keep the rest of the runtime surface under import checking.
%pyproject_check_import -e nltk.book -e nltk.langnames -e nltk.tokenize.nist -e "nltk.test*" -e "nltk.app*" -e "nltk.draw*" -e "nltk.twitter*" %{srcname}

%files -f %{pyproject_files}
%doc README.md AUTHORS.md ChangeLog SECURITY.md
%license LICENSE.txt
%{_bindir}/nltk

%changelog
%autochangelog
