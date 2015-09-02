%global pkgname hypothesis

Name:           python-%{pkgname}
Version:        1.11.0
Release:        1%{?dist}
Summary:        A library for property based testing

License:        MPLv2.0
URL:            https://github.com/DRMacIver/hypothesis
Source0:        https://github.com/DRMacIver/hypothesis/archive/v%{version}.tar.gz#/hypothesis-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python-sphinx
# Test dependencies
BuildRequires:  numpy
BuildRequires:  pytest
BuildRequires:  pytz
#BuildRequires:  python-django
BuildRequires:  python-flake8
#BuildRequires:  python3-django
BuildRequires:  python3-flake8
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-pytz

Provides:       python2-%{pkgname} = %{version}-%{release}
# needed only by hypothesis-extras
Suggests:       numpy
# fake-factory not packaged yet
# Suggests:       python2-fake-factory
Suggests:       pytz
# Django support requires fake-factory
# TODO - update to python2-django once available
# Enhances:       python-django

%description
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%package     -n python3-%{pkgname}
Summary:        A library for property based testing
# needed only by hypothesis-extras
# fake-factory not packaged yet
# Suggests:       python3-fake-factory
Suggests:       python3-numpy
Suggests:       python3-pytz
# Django support requires fake-factory
# Enhances:       python3-django


%description -n python3-%{pkgname}
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%prep
%setup -qc
mv %{pkgname}-%{version} python2
# remove shebang, mergedbs gets installed in sitelib
%{__sed} -i -e 1,2d python2/src/hypothesis/tools/mergedbs.py
# remove Django tests for now
rm -rf python2/tests/django
# remove fakefactory tests, not packaged yet
rm -rf python2/tests/fakefactory
# remove slow tests
rm -rf python2/tests/nocover

cp -a python2 python3
# remove py2-specific tests
rm -rf python3/tests/py2


%build
pushd python2
%{__python2} setup.py build
(cd docs && READTHEDOCS=True make man)
popd

pushd python3
%{__python3} setup.py build
popd


%install
# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
pushd python3
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd

pushd python2
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{__install} -Dp -m 644 docs/_build/man/hypothesis.1 \
             $RPM_BUILD_ROOT%{_mandir}/man1/hypothesis.1
popd


%check
# Tests are still flaky
pushd python2
#{__python2} setup.py test
popd

pushd python3
# Python3 tests seem to fail on ARM builder at the moment
popd


%files
%license python2/LICENSE.txt
%doc python2/README.rst
%{python2_sitelib}/*
%{_mandir}/man1/hypothesis.1*

%files -n python3-%{pkgname}
%license python3/LICENSE.txt
%doc python3/README.rst
%{python3_sitelib}/*


%changelog
* Wed Sep  2 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-3
- Re-disable tests for now

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-2
- Disable Python3 tests - need debugging on ARM builders

* Mon Aug 31 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-1
- Update to 1.10.6
- Enable tests

* Fri Aug  7 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.0-1
- Update to 1.10

* Wed Jul 29 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-2
- Remove she-bang from tools/mergedbs.py
- Include manpage

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-1
- Update to 1.8.5
- Make Python3 build unconditional

* Thu Jul 23 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.2-1
- Initial package
