#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-xgboost
Version  : 1.7.4
Release  : 4
URL      : https://files.pythonhosted.org/packages/5f/1f/ec8651b2c235c319e925918f355466294de8f3846d1a749898a70bfce01c/xgboost-1.7.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/1f/ec8651b2c235c319e925918f355466294de8f3846d1a749898a70bfce01c/xgboost-1.7.4.tar.gz
Summary  : XGBoost Python Package
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-xgboost-filemap = %{version}-%{release}
Requires: pypi-xgboost-lib = %{version}-%{release}
Requires: pypi-xgboost-license = %{version}-%{release}
Requires: pypi-xgboost-python = %{version}-%{release}
Requires: pypi-xgboost-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : pypi(numpy)
BuildRequires : pypi(scipy)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
======================
XGBoost Python Package
======================
|PyPI version|

%package dev
Summary: dev components for the pypi-xgboost package.
Group: Development
Requires: pypi-xgboost-lib = %{version}-%{release}
Provides: pypi-xgboost-devel = %{version}-%{release}
Requires: pypi-xgboost = %{version}-%{release}

%description dev
dev components for the pypi-xgboost package.


%package filemap
Summary: filemap components for the pypi-xgboost package.
Group: Default

%description filemap
filemap components for the pypi-xgboost package.


%package lib
Summary: lib components for the pypi-xgboost package.
Group: Libraries
Requires: pypi-xgboost-license = %{version}-%{release}
Requires: pypi-xgboost-filemap = %{version}-%{release}

%description lib
lib components for the pypi-xgboost package.


%package license
Summary: license components for the pypi-xgboost package.
Group: Default

%description license
license components for the pypi-xgboost package.


%package python
Summary: python components for the pypi-xgboost package.
Group: Default
Requires: pypi-xgboost-python3 = %{version}-%{release}

%description python
python components for the pypi-xgboost package.


%package python3
Summary: python3 components for the pypi-xgboost package.
Group: Default
Requires: pypi-xgboost-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(xgboost)
Requires: pypi(numpy)
Requires: pypi(scipy)

%description python3
python3 components for the pypi-xgboost package.


%prep
%setup -q -n xgboost-1.7.4
cd %{_builddir}/xgboost-1.7.4
pushd ..
cp -a xgboost-1.7.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678900883
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-xgboost
cp %{_builddir}/xgboost-%{version}/xgboost/LICENSE %{buildroot}/usr/share/package-licenses/pypi-xgboost/4d98c20884442064704475a2c7092515382cfe48 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/any.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/array_view.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/base.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/blockingconcurrentqueue.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/build_config_default.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/common.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/concurrency.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/concurrentqueue.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/config.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/data.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/endian.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/filesystem.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/input_split_shuffle.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/io.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/json.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/logging.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/lua.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/memory.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/memory_io.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/omp.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/optional.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/parameter.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/recordio.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/registry.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/serializer.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/strtonum.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/thread_group.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/thread_local.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/threadediter.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/timer.h
/usr/lib/python3.11/site-packages/xgboost/dmlc-core/include/dmlc/type_traits.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/base.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/c_api.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/collective/socket.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/data.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/feature_map.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/gbm.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/generic_parameters.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/global_config.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/host_device_vector.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/intrusive_ptr.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/json.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/json_io.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/learner.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/linalg.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/linear_updater.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/logging.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/metric.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/model.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/objective.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/parameter.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/predictor.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/span.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/string_view.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/task.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/tree_model.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/tree_updater.h
/usr/lib/python3.11/site-packages/xgboost/include/xgboost/version_config.h
/usr/lib/python3.11/site-packages/xgboost/rabit/include/rabit/base.h
/usr/lib/python3.11/site-packages/xgboost/rabit/include/rabit/c_api.h
/usr/lib/python3.11/site-packages/xgboost/rabit/include/rabit/internal/engine.h
/usr/lib/python3.11/site-packages/xgboost/rabit/include/rabit/internal/io.h
/usr/lib/python3.11/site-packages/xgboost/rabit/include/rabit/internal/rabit-inl.h
/usr/lib/python3.11/site-packages/xgboost/rabit/include/rabit/internal/socket.h
/usr/lib/python3.11/site-packages/xgboost/rabit/include/rabit/internal/utils.h
/usr/lib/python3.11/site-packages/xgboost/rabit/include/rabit/rabit.h
/usr/lib/python3.11/site-packages/xgboost/rabit/include/rabit/serializable.h

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-xgboost

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-xgboost/4d98c20884442064704475a2c7092515382cfe48

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
