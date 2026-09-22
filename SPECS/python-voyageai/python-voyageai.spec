# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname voyageai

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        The official Python client for the Voyage AI API
License:        MIT
URL:            https://www.voyageai.com
#!RemoteAsset:  sha256:ed2775fe9faeb96cc2b3931edc35d76185d19f34f1523d1f70535f0451126ae9
Source0:        https://files.pythonhosted.org/packages/source/v/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Remove langchain-text-splitters deps to avoid deep dependency chains
Patch2000:      2000-remove-langchain-deps.patch

BuildOption(install):  voyageai

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(tenacity)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(aiolimiter)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(tokenizers)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The official Python client for Voyage AI, providing access to cutting-edge
embedding models and rerankers for retrieval-augmented generation (RAG) and
other AI applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
