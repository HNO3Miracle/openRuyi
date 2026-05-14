# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros-backend
%global full_version 0.27.2
%global pkgname pyo3-macros-backend-0.27

Name:           rust-pyo3-macros-backend-0.27
Version:        0.27.2
Release:        %autorelease
Summary:        Rust crate "pyo3-macros-backend"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:03b51720d314836e53327f5871d4c0cfb4fb37cc2c4a11cc71907a86342c40f9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1.0) >= 1.0.103
Requires:       crate(pyo3-build-config-0.27/default) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Requires:       crate(quote-1.0) >= 1.0.42
Requires:       crate(syn-2.0/clone-impls) >= 2.0.111
Requires:       crate(syn-2.0/derive) >= 2.0.111
Requires:       crate(syn-2.0/extra-traits) >= 2.0.111
Requires:       crate(syn-2.0/full) >= 2.0.111
Requires:       crate(syn-2.0/parsing) >= 2.0.111
Requires:       crate(syn-2.0/printing) >= 2.0.111
Requires:       crate(syn-2.0/visit-mut) >= 2.0.111
Provides:       crate(pyo3-macros-backend) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/experimental-async)
Provides:       crate(%{pkgname}/experimental-inspect)

%description
Source code for takopackized Rust crate "pyo3-macros-backend"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
