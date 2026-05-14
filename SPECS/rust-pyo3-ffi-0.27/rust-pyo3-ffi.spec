# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-ffi
%global full_version 0.27.2
%global pkgname pyo3-ffi-0.27

Name:           rust-pyo3-ffi-0.27
Version:        0.27.2
Release:        %autorelease
Summary:        Rust crate "pyo3-ffi"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:1c85c9cbfaddf651b1221594209aed57e9e5cff63c4d11d1feead529b872a089
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.177
Requires:       crate(pyo3-build-config-0.27/default) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(pyo3-ffi) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "pyo3-ffi"

%package     -n %{name}+abi3
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-build-config-0.27/abi3) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(%{pkgname}/abi3)

%description -n %{name}+abi3
This metapackage enables feature "abi3" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py310
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py310"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py311)
Requires:       crate(pyo3-build-config-0.27/abi3-py310) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(%{pkgname}/abi3-py310)

%description -n %{name}+abi3-py310
This metapackage enables feature "abi3-py310" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py311
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py311"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py312)
Requires:       crate(pyo3-build-config-0.27/abi3-py311) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(%{pkgname}/abi3-py311)

%description -n %{name}+abi3-py311
This metapackage enables feature "abi3-py311" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py312
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py312"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py313)
Requires:       crate(pyo3-build-config-0.27/abi3-py312) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(%{pkgname}/abi3-py312)

%description -n %{name}+abi3-py312
This metapackage enables feature "abi3-py312" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py313
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py313"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py314)
Requires:       crate(pyo3-build-config-0.27/abi3-py313) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(%{pkgname}/abi3-py313)

%description -n %{name}+abi3-py313
This metapackage enables feature "abi3-py313" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py314
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py314"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3)
Requires:       crate(pyo3-build-config-0.27/abi3-py314) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(%{pkgname}/abi3-py314)

%description -n %{name}+abi3-py314
This metapackage enables feature "abi3-py314" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py37
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py37"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py38)
Requires:       crate(pyo3-build-config-0.27/abi3-py37) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(%{pkgname}/abi3-py37)

%description -n %{name}+abi3-py37
This metapackage enables feature "abi3-py37" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py38
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py38"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py39)
Requires:       crate(pyo3-build-config-0.27/abi3-py38) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(%{pkgname}/abi3-py38)

%description -n %{name}+abi3-py38
This metapackage enables feature "abi3-py38" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py39
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py39"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py310)
Requires:       crate(pyo3-build-config-0.27/abi3-py39) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(%{pkgname}/abi3-py39)

%description -n %{name}+abi3-py39
This metapackage enables feature "abi3-py39" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+extension-module
Summary:        Python-API bindings for the PyO3 ecosystem - feature "extension-module"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-build-config-0.27/extension-module) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(%{pkgname}/extension-module)

%description -n %{name}+extension-module
This metapackage enables feature "extension-module" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generate-import-lib
Summary:        Python-API bindings for the PyO3 ecosystem - feature "generate-import-lib"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-build-config-0.27/generate-import-lib) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
Provides:       crate(%{pkgname}/generate-import-lib)

%description -n %{name}+generate-import-lib
This metapackage enables feature "generate-import-lib" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
