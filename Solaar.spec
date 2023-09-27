#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : Solaar
Version  : 1.1.10
Release  : 28
URL      : https://github.com/pwr/Solaar/archive/1.1.10/Solaar-1.1.10.tar.gz
Source0  : https://github.com/pwr/Solaar/archive/1.1.10/Solaar-1.1.10.tar.gz
Summary  : Linux device manager for Logitech receivers, keyboards, mice, and tablets.
Group    : Development/Tools
License  : GPL-2.0
Requires: Solaar-data = %{version}-%{release}
Requires: Solaar-license = %{version}-%{release}
Requires: Solaar-python = %{version}-%{release}
Requires: Solaar-python3 = %{version}-%{release}
Requires: pyudev
BuildRequires : buildreq-distutils3
BuildRequires : pypi(dbus_python)
BuildRequires : pypi(evdev)
BuildRequires : pypi(psutil)
BuildRequires : pypi(python_xlib)
BuildRequires : pypi(pyudev)
BuildRequires : pypi(pyyaml)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Solaar application icon drawn by me, roughly guided by Logitech's Unifying logo.

%package data
Summary: data components for the Solaar package.
Group: Data

%description data
data components for the Solaar package.


%package extras
Summary: extras components for the Solaar package.
Group: Default

%description extras
extras components for the Solaar package.


%package license
Summary: license components for the Solaar package.
Group: Default

%description license
license components for the Solaar package.


%package python
Summary: python components for the Solaar package.
Group: Default
Requires: Solaar-python3 = %{version}-%{release}
Provides: solaar-python

%description python
python components for the Solaar package.


%package python3
Summary: python3 components for the Solaar package.
Group: Default
Requires: python3-core
Provides: pypi(solaar)
Requires: dbus-python
Requires: pypi(dbus_python)
Requires: pypi(evdev)
Requires: pypi(psutil)
Requires: pypi(python_xlib)
Requires: pypi(pyudev)
Requires: pypi(pyyaml)

%description python3
python3 components for the Solaar package.


%prep
%setup -q -n Solaar-1.1.10
cd %{_builddir}/Solaar-1.1.10
pushd ..
cp -a Solaar-1.1.10 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695831590
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
mkdir -p %{buildroot}/usr/share/package-licenses/Solaar
cp %{_builddir}/Solaar-%{version}/COPYING %{buildroot}/usr/share/package-licenses/Solaar/4cc77b90af91e615a64ae04893fdffa7939db84c || :
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
## install_append content
install -Dm0644 rules.d/42-logitech-unify-permissions.rules %{buildroot}%/usr/lib/udev/rules.d/42-logitech-unify-permissions.rules
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/metainfo/io.github.pwr_solaar.solaar.metainfo.xml
/usr/share/solaar/icons/solaar-symbolic.svg
/usr/share/solaar/udev-rules.d/42-logitech-unify-permissions.rules

%files extras
%defattr(-,root,root,-)
/usr/bin/solaar
/usr/share/applications/solaar.desktop
/usr/share/icons/hicolor/scalable/apps/solaar.svg
/usr/share/solaar/icons/light_000.png
/usr/share/solaar/icons/light_020.png
/usr/share/solaar/icons/light_040.png
/usr/share/solaar/icons/light_060.png
/usr/share/solaar/icons/light_080.png
/usr/share/solaar/icons/light_100.png
/usr/share/solaar/icons/light_unknown.png
/usr/share/solaar/icons/solaar-attention.svg
/usr/share/solaar/icons/solaar-init.svg
/usr/share/solaar/icons/solaar.svg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Solaar/4cc77b90af91e615a64ae04893fdffa7939db84c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
