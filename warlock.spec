#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : warlock
Version  : 1.3.0
Release  : 26
URL      : http://pypi.debian.net/warlock/warlock-1.3.0.tar.gz
Source0  : http://pypi.debian.net/warlock/warlock-1.3.0.tar.gz
Summary  : Python object model built on JSON schema and JSON patch.
Group    : Development/Tools
License  : Apache-2.0
Requires: warlock-python
Requires: jsonpatch
Requires: jsonschema
Requires: six
BuildRequires : jsonpatch
BuildRequires : jsonpointer
BuildRequires : jsonschema
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : warlock

%description
# Warlock
[![Build Status](https://travis-ci.org/bcwaldon/warlock.svg?branch=master)](https://travis-ci.org/bcwaldon/warlock)

%package python
Summary: python components for the warlock package.
Group: Default

%description python
python components for the warlock package.


%prep
%setup -q -n warlock-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503083095
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
export SOURCE_DATE_EPOCH=1503083095
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
