%global srcname hypothesis

%bcond_without python2
%bcond_without python3
%bcond_without platform_python

Name:           python-%{srcname}
Version:        3.12.0
Release:        4%{?dist}
Summary:        Library for property based testing

License:        MPLv2.0
URL:            https://github.com/HypothesisWorks/hypothesis-python
Source0:        %{url}/archive/%{version}.tar.gz#/hypothesis-%{version}.tar.gz
# disable Sphinx extensions that require Internet access
Patch0:         %{srcname}-3.12.0-offline.patch

BuildArch:      noarch

%description
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%if %{with python2}
%package     -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-sphinx
BuildRequires:  python2-enum34
Obsoletes:      python-%{srcname} < 1.11.1-1
Requires:       python2-enum34

%{?python_provide:%python_provide python2-%{srcname}}
%if ! (0%{?rhel} && 0%{?rhel} <= 7)
Suggests:       python2-numpy
Suggests:       python2-pytz
%endif

%description -n python2-%{srcname}
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.

%endif


%if %{with python3}
%package     -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
%{?python_provide:%python_provide python3-%{srcname}}
%if ! (0%{?rhel} && 0%{?rhel} <= 7)
Suggests:       python3-numpy
Suggests:       python3-pytz
%endif

%description -n python3-%{srcname}
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.

%endif

%if %{with platform_python}
%package     -n platform-python-%{srcname}
Summary:        %{summary}
BuildRequires:  platform-python-devel
BuildRequires:  platform-python-setuptools

%description -n platform-python-%{srcname}
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.
%endif


%prep
%autosetup -n %{srcname}-python-%{version} -p1

# remove shebang, mergedbs gets installed in sitelib
%{__sed} -i -e 1,2d src/hypothesis/tools/mergedbs.py


%build
%if %{with python2}
%py2_build
%if %{without python3}
PYTHONPATH=src READTHEDOCS=True sphinx-build -b man docs docs/_build/man
%endif
%endif

%if %{with python3}
%py3_build
PYTHONPATH=src READTHEDOCS=True sphinx-build-3 -b man docs docs/_build/man
%endif

%if %{with platform_python}
%platform_py_build
%endif


%install
%if %{with python2}
%py2_install
%endif

%if %{with platform_python}
%platform_py_install
%endif

%if %{with python3}
%py3_install
%endif

%{__install} -Dp -m 644 docs/_build/man/hypothesis.1 \
             $RPM_BUILD_ROOT%{_mandir}/man1/hypothesis.1


%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/*
%{_mandir}/man1/hypothesis.1*
%endif

%if %{with python3}
%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/*
%{_mandir}/man1/hypothesis.1*
%endif

%if %{with platform_python}
%files -n platform-python-%{srcname}
%license LICENSE.txt
%doc README.rst
%{platform_python_sitelib}/*
%{_mandir}/man1/hypothesis.1*
%endif


%changelog
* Thu Aug 24 2017 Miro Hrončok <mhroncok@redhat.com> - 3.12.0-4
- Rebuilt for rhbz#1484607

* Thu Aug 10 2017 Tomas Orsava <torsava@redhat.com> - 3.12.0-3
- Added the platform-python subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.12.0-1
- Update to 3.12.0
- Reenable docs in EPEL7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 3.4.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 29 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0
- Version the explicit Provides

* Wed May 04 2016 Nathaniel McCallum <npmccallum@redhat.com> - 3.1.3-1
- Update to 3.1.3
- Remove unused code
- Remove unused dependencies

* Sun Feb 14 2016 Michel Salim <salimma@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 25 2015 Michel Salim <salimma@fedoraproject.org> - 1.11.2-1
- Update to 1.11.2

* Sun Sep 20 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

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
